import fastapi
from server.sql_base.models import Firm
from server.resolvers.firms import create_firm, get_firm, get_all_firm, update_firm, delete_firm

firms_router = fastapi.APIRouter(prefix='/firms', tags=['Firms'])


@firms_router.get("/")
def start_page():
    return f"Hello new user!"


@firms_router.post("/create/")
def new_categories(firm: Firm):
    return create_firm(firm)


@firms_router.get("/get/{firm_id}/")
def search_firm(firm_id: int):
    return get_firm(firm_id)


@firms_router.get("/get/")
def get_firm_all():
    return get_all_firm()


@firms_router.put("/update/{firm_id}/")
def upd_firm(firm_id: int, new_data: Firm):
    return update_firm(firm_id=firm_id, new_data=new_data)


@firms_router.delete("/delete/{firm_id}/")
def del_expedition(firm_id: int):
    return delete_firm(firm_id)
