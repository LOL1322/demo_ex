import fastapi
from server.sql_base.models import User
from server.resolvers.users import create_user, get_user, get_all_user, update_user, delete_user

users_router = fastapi.APIRouter(prefix='/users', tags=['User'])


@users_router.get("/")
def start_page():
    return f"Hello new user!"


@users_router.post("/create/")
def new_user(user: User):
    return create_user(user)


@users_router.get("/get/{user_id}/")
def search_user(user_id: int):
    return get_user(user_id)


@users_router.get("/get/")
def get_user_all():
    return get_all_user()


@users_router.put("/update/{user_id}/")
def upd_user(user_id: int, new_data: User):
    return update_user(user_id, new_data)


@users_router.delete("/delete/{user_id}/")
def del_user(user_id: int):
    return delete_user(user_id)