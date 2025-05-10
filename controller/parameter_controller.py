from fastapi import APIRouter, HTTPException
from model.location import Location
from service.parameter_service import ParameterService

router = APIRouter(prefix="/locations", tags=["Parameters"])

@router.get("/", response_model=list[Location])
def get_all_locations():
    return ParameterService.get_locations()

@router.get("/states", response_model=list[Location])
def get_states():
    return ParameterService.get_states()

@router.get("/by-state/{state_code}", response_model=list[Location])
def get_locations_by_state(state_code: str):
    locations = ParameterService.get_locations_by_state_code(state_code)
    if not locations:
        raise HTTPException(status_code=404, detail="No locations found for the given state code.")
    return locations

@router.get("/by-code/{location_code}", response_model=Location)
def get_location_by_code(location_code: str):
    location = ParameterService.get_location_by_code(location_code)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found.")
    return location

@router.get("/capitals", response_model=list[Location])
def get_capitals():
    return ParameterService.get_capitals()
