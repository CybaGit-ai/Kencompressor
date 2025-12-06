from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from backend.db import get_session
from backend.models import Listing, ListingIntel
from backend.schemas import ListingRead, ListingIntelRead
from backend.services.aggregator import build_intel_for_listing

router = APIRouter()


@router.get("/agent/{agent_id}/listings", response_model=list[ListingRead])
def get_agent_listings(agent_id: UUID, session=Depends(get_session)):
    listings = session.exec(
        select(Listing).where(Listing.agent_id == agent_id, Listing.status == "ACTIVE")
    ).all()
    return listings


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
