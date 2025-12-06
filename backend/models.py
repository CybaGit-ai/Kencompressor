from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID

from sqlmodel import SQLModel, Field, Relationship


class Agent(SQLModel, table=True):
    __tablename__ = "agents"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str
    phone: str
    email: str
    brokerage: str
    external_agent_key: Optional[str] = Field(default=None)

    listings: list["Listing"] = Relationship(back_populates="agent")


class Listing(SQLModel, table=True):
    __tablename__ = "listings"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    external_listing_key: Optional[str] = Field(default=None)
    address: str
    city: str
    region: str
    lat: float
    lon: float
    price: int
    beds: int
    baths: float
    sqft: int
    lot_sqft: Optional[int] = Field(default=None)
    property_type: str
    status: str
    agent_id: UUID = Field(foreign_key="agents.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    agent: Optional[Agent] = Relationship(back_populates="listings")
    intel: Optional["ListingIntel"] = Relationship(back_populates="listing")


class ListingIntel(SQLModel, table=True):
    __tablename__ = "listing_intel"

    listing_id: UUID = Field(foreign_key="listings.id", primary_key=True)
    intel_json: dict

    listing: Listing = Relationship(back_populates="intel")
