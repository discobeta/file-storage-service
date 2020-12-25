from fastapi import APIRouter
from app.models.healthcheck import HealthCheckResponse

router = APIRouter()

@router.get("/health-check", response_model=HealthCheckResponse)
async def health_check():
    return HealthCheckResponse(status="ok")


