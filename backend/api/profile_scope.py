"""Resolve profile-scoped Hermes data directories for API endpoints."""

from __future__ import annotations

from pathlib import Path

from fastapi import HTTPException

from backend.collectors.utils import default_hermes_dir


def resolve_profile_scope(profile: str | None = None) -> tuple[str, str]:
    """Return (profile_name, hermes_dir) for the requested profile.

    Profile names are resolved relative to the active Hermes home:
    - None / "default" -> ~/.hermes
    - other names      -> ~/.hermes/profiles/<name>
    """
    base_dir = Path(default_hermes_dir())
    requested = (profile or "default").strip() or "default"

    if requested == "default":
        return "default", str(base_dir)

    profile_dir = base_dir / "profiles" / requested
    if profile_dir.is_dir():
        return requested, str(profile_dir)

    raise HTTPException(status_code=404, detail=f"Profile not found: {requested}")