from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={
        400: {"detail": "error message"}
    },
)
