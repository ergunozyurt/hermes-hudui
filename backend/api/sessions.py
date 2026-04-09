"""Sessions endpoints."""

from fastapi import APIRouter

from backend.collectors.sessions import collect_sessions
from .serialize import to_dict
from .profile_scope import resolve_profile_scope

router = APIRouter()


@router.get("/sessions")
async def get_sessions(profile: str | None = None):
    profile_name, hermes_dir = resolve_profile_scope(profile)
    result = to_dict(collect_sessions(hermes_dir))
    result["profile"] = profile_name
    return result
