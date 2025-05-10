from fastapi import APIRouter
from model.type_doc import TypeDoc
from service.parameter_service import ParameterService

router = APIRouter(prefix="/typedocs", tags=["Parameters"])

@router.get("/", response_model=list[TypeDoc])
def get_all_type_docs():
    return ParameterService.get_type_docs()
