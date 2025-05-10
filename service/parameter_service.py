import csv
from typing import List
from model.parameter import Parameter
from model.location import Location
from model.type_doc import TypeDoc


class ParameterService:
    parameters: List[Parameter] = []

    @classmethod
    def load_parameters(cls, locations_path: str = "locations.csv"):
        cls._load_locations(locations_path)
        cls._load_type_docs()

    @classmethod
    def _load_locations(cls, path: str):
        with open(path, mode="r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                code = row["Código Municipio"].strip()
                description = f"{row['Nombre Municipio'].strip()} - {row['Nombre Departamento'].strip()}"
                state_code = row["Código Departamento"].strip()
                state_name = row["Nombre Departamento"].strip()
                is_capital = row["Código Municipio"].strip().endswith("001")
                cls.parameters.append(Location(
                    code=code,
                    description=description,
                    state_code=state_code,
                    state_name=state_name,
                    is_capital=is_capital
                ))

    @classmethod
    def _load_type_docs(cls):
        cls.parameters.append(TypeDoc(code="CC", description="Cédula de Ciudadanía"))
        cls.parameters.append(TypeDoc(code="TI", description="Tarjeta de Identidad"))
        cls.parameters.append(TypeDoc(code="PA", description="Pasaporte"))

    @classmethod
    def get_all(cls) -> List[Parameter]:
        return cls.parameters

    @classmethod
    def get_locations(cls) -> List[Location]:
        return [p for p in cls.parameters if isinstance(p, Location)]

    @classmethod
    def get_type_docs(cls) -> List[TypeDoc]:
        return [p for p in cls.parameters if isinstance(p, TypeDoc)]

    @classmethod
    def get_location_by_code(cls, code: str) -> Location | None:
        for p in cls.parameters:
            if isinstance(p, Location) and p.code == code:
                return p
        return None

    @classmethod
    def get_locations_by_state_code(cls, state_code: str) -> List[Location]:
        return [
            p for p in cls.parameters
            if isinstance(p, Location) and p.state_code == state_code
        ]

    @classmethod
    def get_states(cls) -> List[Location]:
        seen = set()
        result = []
        for p in cls.parameters:
            if isinstance(p, Location):
                if p.state_code not in seen:
                    seen.add(p.state_code)
                    result.append(p)
        return result

    @classmethod
    def get_capitals(cls) -> List[Location]:
        return [p for p in cls.parameters if isinstance(p, Location) and p.is_capital]
