import fastapi
from server.sql_base.models import Expedition
from server.resolvers.expeditions import create_expedition, get_expedition, get_all_expeditions, update_expedition, delete_expedition

expeditions_router = fastapi.APIRouter(prefix='/expedition', tags=['Expedition'])


@expeditions_router.get("/")
def start_page():
    return f"Hello new user!"


@expeditions_router.post("/create/")
def new_expedition(expedition: Expedition):
    return create_expedition(expedition)


@expeditions_router.get("/get/{expedition_id}/")
def search_expedition(expedition_id: int):
    return get_expedition(expedition_id)


@expeditions_router.put("/update/{expedition_id}/")
def upd_expedition(expedition_id: int, new_data: Expedition):
    return update_expedition(expedition_id=expedition_id, new_data=new_data)


@expeditions_router.delete("/delete/{expedition_id}/")
def del_expedition(expedition_id: int):
    return delete_expedition(expedition_id)


@expeditions_router.get("/get/")
def get_expedition_all():
    return get_all_expeditions()
