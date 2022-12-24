from server.sql_base.db_manager import base_worker
from server.sql_base.models import Expedition


def create_expeditions(expedition: Expedition):
    return base_worker.execute(query="INSERT INTO expeditions(firm_id, date, location) VALUES (?, ?, ?) RETURNING id",
                               args=(expedition.firm_id, expedition.date, expedition.location))

