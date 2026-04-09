"""Cron jobs endpoint."""

from fastapi import APIRouter

from backend.collectors.cron import collect_cron
from .serialize import to_dict
from .profile_scope import resolve_profile_scope

router = APIRouter()


@router.get("/cron")
async def get_cron(profile: str | None = None):
    profile_name, hermes_dir = resolve_profile_scope(profile)
    result = to_dict(collect_cron(hermes_dir))
    result["profile"] = profile_name
    return result
