from server.sql_base.db_manager import base_worker
import fastapi
from server.router import routers

base_worker.create_db("../sql/tables.sql")

app = fastapi.APIRouter()

[app.include_router(router) for router in routers]
