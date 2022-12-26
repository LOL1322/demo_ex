import fastapi
from server.sql_base.models import Fossil
from server.resolvers.fossils import create_fossil, get_fossil, get_all_fossil, update_fossil, delete_fossil

fossils_router = fastapi.APIRouter(prefix='/fossils', tags=['Fossils'])


@fossils_router.get("/")
def start_page():
    return f"Hello new user!"


@fossils_router.post("/create/")
def new_fossil(fossil: Fossil):
    return create_fossil(fossil)


@fossils_router.get("/get/{fossil_id}/")
def search_fossil(fossil_id: int):
    return get_fossil(fossil_id)


@fossils_router.get("/get/")
def get_fossil_all():
    return get_all_fossil()


@fossils_router.put("/update/{fossil_id}/")
def upd_fossil(fossil_id: int, new_data: Fossil):
    return update_fossil(fossil_id, new_data)


@fossils_router.delete("/delete/{fossil_id}/")
def del_fossil(fossil_id: int):
    return delete_fossil(fossil_id)
