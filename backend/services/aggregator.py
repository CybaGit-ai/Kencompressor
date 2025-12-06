from __future__ import annotations

from uuid import UUID

from sqlmodel import Session, select

from backend.models import Listing, ListingIntel
from backend.services import sources


def build_intel_for_listing(listing_id: UUID, session: Session) -> dict:
    listing = session.exec(select(Listing).where(Listing.id == listing_id)).first()
    if not listing:
        raise ValueError("Listing not found")

    parcel = sources.fetch_parcel_from_ParcelMapBC(listing.lat, listing.lon)
    alr = sources.check_in_ALR(parcel)
    flood = sources.fetch_flood_hazard_from_BC_FloodHazard(listing.lat, listing.lon)
    wildfire = sources.fetch_wildfire_history_from_BC_Wildfire(listing.lat, listing.lon)
    thematic = sources.fetch_thematic_layers_from_GeoBC(listing.lat, listing.lon)
    municipal = sources.fetch_municipal_data(listing.city, listing.lat, listing.lon)
    amenities = sources.get_amenities_from_OSM(listing.lat, listing.lon)
    transit = sources.get_transit_info_from_TransLink(listing.lat, listing.lon)
    drives = sources.get_drive_times_from_OpenRouteService(listing.lat, listing.lon)
    census = sources.get_census_profile_from_StatCan(f"DA-{listing.city}-001")
    bc_stats = sources.get_bc_stats_projection(listing.city)
    fvrd = sources.get_fvrd_stats(listing.city)
    weather = sources.get_weather_from_EnvironmentCanada(listing.lat, listing.lon)
    forecast = sources.get_forecast_from_OpenWeather(listing.lat, listing.lon)
    crime = sources.get_crime_from_RCMP(listing.city)
    health = sources.get_health_data_from_FraserHealth(listing.city)
    catchments = sources.fetch_school_catchments_from_BC_SchoolLocator(listing.lat, listing.lon)
    childcare = sources.fetch_childcare_from_FraserHealth(listing.lat, listing.lon)
    river_levels = sources.get_river_levels_from_CanadaWaterOffice()
    price_history = sources.get_area_price_history(listing.city)
    dom_history = sources.get_area_dom_history(listing.city)

    intel_json = {
        "listing": {
            "id": str(listing.id),
            "mls_id": listing.external_listing_key,
            "address": listing.address,
            "lat": listing.lat,
            "lon": listing.lon,
            "price": listing.price,
            "beds": listing.beds,
            "baths": listing.baths,
            "sqft": listing.sqft,
            "lot_sqft": listing.lot_sqft,
            "property_type": listing.property_type,
            "year_built": 2005,
            "agent": {
                "id": str(listing.agent.id),
                "name": listing.agent.name,
                "phone": listing.agent.phone,
                "brokerage": listing.agent.brokerage,
            },
        },
        "metrics": {
            "scores": {
                "livability": 82,
                "transit": 65,
                "walkability": 55,
                "schools": 78,
                "environment_risk": 25,
                "investment": 74,
            },
            "market": {
                "area": listing.city,
                "median_price_area": fvrd["median_price"],
                "median_price_city": fvrd["median_price"] + 15000,
                "yoy_price_change_area": 3.2,
                "avg_days_on_market_area": fvrd["avg_dom"],
                "listing_days_on_market": 14,
                "inventory_months_area": 2.1,
                "sale_to_list_ratio_area": fvrd["sale_to_list_ratio"],
            },
            "neighbourhood": census,
            "amenities": {"within_1km": amenities},
            "routes": drives,
            "environment": {
                "in_alr": alr,
                "in_floodplain": flood["in_floodplain"],
                "distance_to_floodplain_m": flood["distance_to_floodplain_m"],
                "distance_to_recent_wildfire_km": wildfire["distance_to_recent_wildfire_km"],
            },
        },
        "time_series": {
            "area_price_history": price_history,
            "area_dom_history": dom_history,
        },
        "context": {
            "parcel": parcel,
            "municipal": municipal,
            "thematic": thematic,
            "transit": transit,
            "weather": weather,
            "forecast": forecast,
            "crime": crime,
            "health": health,
            "schools": catchments,
            "childcare": childcare,
            "river_levels": river_levels,
            "bc_stats": bc_stats,
        },
    }

    listing_intel = session.exec(select(ListingIntel).where(ListingIntel.listing_id == listing.id)).first()
    if listing_intel:
        listing_intel.intel_json = intel_json
    else:
        listing_intel = ListingIntel(listing_id=listing.id, intel_json=intel_json)
        session.add(listing_intel)
    session.commit()
    session.refresh(listing_intel)
    return intel_json
