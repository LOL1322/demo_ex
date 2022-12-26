import fastapi
from server.sql_base.models import Personnel
from server.resolvers.personnel import create_personnel, get_personnel, get_all_personnel, update_personnel, delete_personnel

personnel_router = fastapi.APIRouter(prefix='/personnel', tags=['Personnel'])


@personnel_router.get("/")
def start_page():
    return f"Hello new user!"


@personnel_router.post("/create/")
def new_personnel(personnel: Personnel):
    return create_personnel(personnel)


@personnel_router.get("/get/{personnel_id}/")
def search_personnel(personnel_id: int):
    return get_personnel(personnel_id)


@personnel_router.get("/get/")
def get_personnel_all():
    return get_all_personnel()


@personnel_router.put("/update/{personnel_id}/")
def upd_personnel(personnel_id: int, new_data: Personnel):
    return update_personnel(personnel_id, new_data)


@personnel_router.delete("/delete/{personnel_id}/")
def del_personnel(personnel_id: int):
    return delete_personnel(personnel_id)

