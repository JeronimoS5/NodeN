from fastapi import FastAPI
from controller import person_controller, parameter_controller, type_doc_controller
from service.parameter_service import ParameterService

app = FastAPI(title="People API with N-ary Tree")

ParameterService.load_parameters()

app.include_router(person_controller.router)
app.include_router(parameter_controller.router)
app.include_router(type_doc_controller.router)
