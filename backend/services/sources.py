"""Stubbed data integration layer for Fraser Valley data sources.
Each function returns fake but realistic data to enable end-to-end flows.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Dict, List
import random


def geocode_address(address: str, city: str, region: str):
    """TEMPORARY STUB. Returns fixed Fraser Valley coordinates for now."""
    return (49.0500, -122.3000)


def fetch_parcel_from_ParcelMapBC(lat: float, lon: float) -> dict:
    """Return a simplified parcel record from ParcelMapBC."""
    return {
        "pid": "013-456-789",
        "legal_description": "LT 5 SEC 3 TWP 17 NWD PLN 12345",
        "centroid": {"lat": lat, "lon": lon},
        "lot_size_sqft": 6500,
    }


def check_in_ALR(parcel_geom: dict) -> bool:
    """Determine if parcel intersects the Agricultural Land Reserve."""
    return False


def fetch_flood_hazard_from_BC_FloodHazard(lat: float, lon: float) -> dict:
    """Return flood hazard indicators for the coordinate."""
    return {
        "in_floodplain": random.choice([True, False]),
        "distance_to_floodplain_m": random.choice([120, 350, None]),
        "nearest_river": "Fraser River",
    }


def fetch_wildfire_history_from_BC_Wildfire(lat: float, lon: float) -> dict:
    """Return recent wildfire proximity data."""
    return {
        "distance_to_recent_wildfire_km": random.choice([5.2, 12.4, 22.0, None]),
        "last_year_incidents": 2,
    }


def fetch_thematic_layers_from_GeoBC(lat: float, lon: float) -> dict:
    """Return GeoBC thematic indicators for environmental overlays."""
    return {
        "riparian_buffer_m": 35,
        "landslide_hazard": "low",
        "groundwater_zone": "moderate sensitivity",
    }


def fetch_municipal_data(city: str, lat: float, lon: float) -> dict:
    """Stub municipal GIS lookups based on city name."""
    zoning = {
        "Abbotsford": "RS3 Urban Residential",
        "Chilliwack": "R1-A One Family Residential",
        "Mission": "Urban Compact",
        "Langley": "Suburban Residential",
    }
    return {
        "source": f"{city}_OpenGIS",
        "zoning": zoning.get(city, "Residential"),
        "ocp": "Urban 3 Infill",
        "parks_within_1km": 3,
    }


def get_amenities_from_OSM(lat: float, lon: float, radius_m: int = 1000) -> dict:
    """Return amenity counts within a radius from OpenStreetMap Overpass."""
    return {
        "grocery": 2,
        "parks": 4,
        "elementary_schools": 1,
        "secondary_schools": 1,
        "bus_stops": 12,
        "daycare": 3,
        "gyms": 2,
        "restaurants": 8,
    }


def get_transit_info_from_TransLink(lat: float, lon: float) -> dict:
    """Return transit stop summaries."""
    return {"nearest_stop": "Stop 54321", "routes": ["501", "503"], "next_arrival_min": 6}


def get_drive_times_from_OpenRouteService(lat: float, lon: float) -> dict:
    """Return mock drive times in minutes to key destinations."""
    return {
        "downtown_abbotsford_drive_min": 8,
        "downtown_vancouver_drive_min": 68,
        "nearest_skytrain_drive_min": 22,
    }


def get_census_profile_from_StatCan(geo_id: str) -> dict:
    """Return a census profile for a given dissemination area or tract."""
    return {
        "census_area": geo_id,
        "population": 3400,
        "median_household_income": 92500,
        "owner_occupied_pct": 72.3,
        "immigrant_pct": 31.2,
        "avg_household_size": 3.1,
        "age_distribution": {"0_14": 17.5, "15_34": 26.1, "35_64": 39.3, "65_plus": 17.1},
    }


def get_bc_stats_projection(city: str) -> dict:
    """Return BC Stats growth projection for a city."""
    return {"city": city, "growth_5y_pct": 6.4, "unemployment_rate": 4.8}


def get_fvrd_stats(city: str) -> dict:
    """Return Fraser Valley Regional District stats."""
    return {"median_price": 885000, "avg_dom": 22, "sale_to_list_ratio": 0.97}


def get_weather_from_EnvironmentCanada(lat: float, lon: float) -> dict:
    """Return current weather information."""
    return {"temp_c": 12.3, "condition": "Partly Cloudy", "alert": None}


def get_forecast_from_OpenWeather(lat: float, lon: float) -> dict:
    """Return short forecast from OpenWeather."""
    return {"hourly": [{"ts": datetime.utcnow().isoformat(), "temp_c": 12.5}]}


def get_crime_from_RCMP(city: str) -> dict:
    """Return basic crime stats for the city."""
    return {"incidents_last_30d": 42, "trend": "stable"}


def get_health_data_from_FraserHealth(city: str) -> dict:
    """Return Fraser Health facility availability."""
    return {"hospitals_nearby": ["Abbotsford Regional"], "air_quality_index": 3}


def get_businesses_from_BC_Registry(query: str) -> List[Dict[str, Any]]:
    """Stub for business registry search."""
    return [{"name": f"{query} Holdings Ltd.", "status": "Active"}]


def fetch_imagery_links(address: str) -> dict:
    """Return static map and imagery URLs."""
    return {
        "google_static": f"https://maps.google.com/?q={address}",
        "arcgis": f"https://arcgis.com/imagery/{address.replace(' ', '%20')}",
    }


def fetch_school_catchments_from_BC_SchoolLocator(lat: float, lon: float) -> dict:
    """Return school catchment information."""
    return {
        "elementary": {"name": "Lakeview Elementary", "distance_km": 1.2},
        "secondary": {"name": "Mountain Secondary", "distance_km": 2.8},
    }


def fetch_childcare_from_FraserHealth(lat: float, lon: float) -> List[dict]:
    """Return childcare facilities near the coordinate."""
    return [
        {"name": "Happy Kids Daycare", "distance_km": 0.6},
        {"name": "Sunshine Childcare", "distance_km": 0.9},
    ]


def get_river_levels_from_CanadaWaterOffice() -> dict:
    """Return river level summary for Fraser Valley gauges."""
    return {"fraser_river_level_m": 5.1, "vedder_river_level_m": 2.3}


def get_area_price_history(area: str) -> List[dict]:
    """Return monthly median price history for an area."""
    base_price = 850000
    history = []
    for i in range(12):
        month = (datetime.utcnow() - timedelta(days=30 * i)).strftime("%Y-%m")
        history.append({"month": month, "median_price": base_price + i * 2500})
    return list(reversed(history))


def get_area_dom_history(area: str) -> List[dict]:
    """Return days-on-market history for an area."""
    history = []
    for i in range(12):
        month = (datetime.utcnow() - timedelta(days=30 * i)).strftime("%Y-%m")
        history.append({"month": month, "avg_dom": 18 + i % 4})
    return list(reversed(history))
