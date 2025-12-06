from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from backend import db
from backend.routes import agents, listings
from backend.seed import seed_data
from backend.services.aggregator import build_intel_for_listing
from backend.models import Listing

app = FastAPI(title="Fraser Valley Agent Intel")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    db.init_db()
    with Session(db.engine) as session:
        seed_data(session)
        listings_rows = session.query(Listing).all()
        for listing in listings_rows:
            build_intel_for_listing(listing.id, session)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(agents.router)
app.include_router(listings.router)
