"""
This module points, the routes to the main application
"""
from typing import Tuple

from fastapi.routing import APIRouter

from ..internal import admin


routers: Tuple[APIRouter] = (
    admin.router,
    # Add more routers here...
)