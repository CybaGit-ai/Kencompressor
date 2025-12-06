from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class AgentBase(BaseModel):
    name: str
    phone: str
    email: str
    brokerage: str
    external_agent_key: Optional[str] | None = None


class AgentRead(AgentBase):
    id: UUID

    class Config:
        orm_mode = True


class ListingBase(BaseModel):
    address: str
    city: str
    region: str
    lat: float
    lon: float
    price: int
    beds: int
    baths: float
    sqft: int
    lot_sqft: Optional[int] | None = None
    property_type: str
    status: str
    agent_id: UUID


class ListingRead(ListingBase):
    id: UUID
    external_listing_key: Optional[str] | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ListingIntelRead(BaseModel):
    listing_id: UUID
    intel_json: dict

    class Config:
        orm_mode = True
