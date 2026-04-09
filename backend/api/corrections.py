"""Corrections endpoint."""

from fastapi import APIRouter

from backend.collectors.corrections import collect_corrections
from .serialize import to_dict
from .profile_scope import resolve_profile_scope

router = APIRouter()


@router.get("/corrections")
async def get_corrections(profile: str | None = None):
    profile_name, hermes_dir = resolve_profile_scope(profile)
    result = to_dict(collect_corrections(hermes_dir))
    result["profile"] = profile_name
    return result
