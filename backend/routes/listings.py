from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from backend.db import get_session
from backend.models import Agent, Listing, ListingIntel
from backend.schemas import ListingRead, ListingIntelRead, ListingCreate
from backend.services.aggregator import build_intel_for_listing
from backend.services.sources import geocode_address

router = APIRouter()


@router.get("/agent/{agent_id}/listings", response_model=list[ListingRead])
def get_agent_listings(agent_id: UUID, session=Depends(get_session)):
    listings = session.exec(
        select(Listing).where(Listing.agent_id == agent_id, Listing.status == "ACTIVE")
    ).all()
    return listings


@router.post("/agent/{agent_id}/listings", response_model=ListingRead)
def create_listing_for_agent(
    agent_id: UUID, listing_data: ListingCreate, session=Depends(get_session)
):
    agent = session.exec(select(Agent).where(Agent.id == agent_id)).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    lat, lon = geocode_address(listing_data.address, listing_data.city, listing_data.region)
    listing = Listing(
        address=listing_data.address,
        city=listing_data.city,
        region=listing_data.region,
        lat=lat,
        lon=lon,
        price=listing_data.price,
        beds=listing_data.beds,
        baths=listing_data.baths,
        sqft=listing_data.sqft if listing_data.sqft is not None else 0,
        lot_sqft=listing_data.lot_sqft,
        property_type=listing_data.property_type,
        status="ACTIVE",
        agent_id=agent_id,
    )
    session.add(listing)
    session.commit()
    session.refresh(listing)

    build_intel_for_listing(listing.id, session)
    return listing


@router.get("/listing/{listing_id}", response_model=ListingRead)
def get_listing(listing_id: UUID, session=Depends(get_session)):
    listing = session.exec(select(Listing).where(Listing.id == listing_id)).first()
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing


@router.get("/listing/{listing_id}/intel", response_model=ListingIntelRead)
def get_listing_intel(listing_id: UUID, session=Depends(get_session)):
    intel = session.exec(select(ListingIntel).where(ListingIntel.listing_id == listing_id)).first()
    if not intel:
        raise HTTPException(status_code=404, detail="Intel not found")
    return intel


@router.post("/listing/{listing_id}/refresh_intel", response_model=dict)
def refresh_listing_intel(listing_id: UUID, session=Depends(get_session)):
    try:
        intel = build_intel_for_listing(listing_id, session)
    except ValueError:
        raise HTTPException(status_code=404, detail="Listing not found")
    return intel
