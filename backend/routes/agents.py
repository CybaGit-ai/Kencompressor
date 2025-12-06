from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from backend.db import get_session
from backend.models import Agent
from backend.schemas import AgentRead

router = APIRouter()


@router.get("/agents", response_model=list[AgentRead])
def list_agents(session=Depends(get_session)):
    return session.exec(select(Agent)).all()


@router.get("/agent/resolve", response_model=list[AgentRead])
def resolve_agent(name: str | None = None, phone: str | None = None, session=Depends(get_session)):
    query = select(Agent)
    if name:
        query = query.where(Agent.name.ilike(f"%{name}%"))
    if phone:
        query = query.where(Agent.phone.ilike(f"%{phone}%"))
    results = session.exec(query).all()
    if not results:
        raise HTTPException(status_code=404, detail="No matching agents found")
    return results
