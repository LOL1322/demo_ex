import fastapi
from server.sql_base.models import Position
from server.resolvers.positions import create_position, get_position, get_all_position, update_position, delete_position

positions_router = fastapi.APIRouter(prefix='/positions', tags=['Position'])


@positions_router.get("/")
def start_page():
    return f"Hello new user!"


@positions_router.post("/create/")
def new_position(position: Position):
    return create_position(position)


@positions_router.get("/get/{position_id}/")
def search_position(position_id: int):
    return get_position(position_id)


@positions_router.get("/get/")
def get_position_all():
    return get_all_position()


@positions_router.put("/update/{position_id}/")
def upd_position(position_id: int, new_data: Position):
    return update_position(position_id, new_data)


@positions_router.delete("/delete/{position_id}/")
def del_position(position_id: int):
    return delete_position(position_id)

