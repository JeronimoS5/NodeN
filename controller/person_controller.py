from fastapi import APIRouter, HTTPException
from model.person import Person
from service.person_service import PersonService

router = APIRouter(prefix="/people", tags=["People"])

@router.post("/", response_model=Person)
def create_person(person: Person):
    return PersonService.create(person)

@router.get("/", response_model=list[Person])
def get_all_people():
    return PersonService.get_all()

@router.get("/{person_id}", response_model=Person)
def get_person_by_id(person_id: str):
    person = PersonService.get_by_id(person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.put("/{person_id}", response_model=Person)
def update_person(person_id: str, updated_person: Person):
    person = PersonService.update(person_id, updated_person)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.delete("/{person_id}")
def delete_person(person_id: str):
    success = PersonService.delete(person_id)
    if not success:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"detail": "Person deleted"}

@router.get("/adult-daughters", response_model=list[Person])
def get_people_with_adult_daughter():
    return PersonService.get_people_with_adult_daughter()

@router.get("/filter", response_model=list[Person])
def filter_people_by_criteria(location_code: str, type_doc: str, gender: str):
    return PersonService.filter_by_location_typedoc_gender(location_code, type_doc, gender)

@router.get("/by-location/{location_code}", response_model=list[Person])
def get_people_by_location(location_code: str):
    return PersonService.get_by_location(location_code)
