from server.sql_base.db_manager import base_worker
from server.sql_base.models import Expedition


def create_expedition(expedition: Expedition):
    return base_worker.execute_query(
        query="INSERT INTO expeditions(firm_id, date, location) VALUES (?, ?, ?) RETURNING id",
        args=(expedition.firm_id, expedition.date, expedition.location))


def get_expedition(expedition_id: int):
    return base_worker.execute_query(query="SELECT id, date, location FROM expeditions WHERE id = ?",
                                     args=(expedition_id,))


def get_all_expeditions():
    return base_worker.execute_query(query="SELECT id, date, location FROM expeditions",
                                     fetchone=False)


def update_expedition(expedition_id: int, new_data: Expedition):
    return base_worker.execute_query(query="UPDATE expeditions SET (date, location) = (?, ?) WHERE id=?",
                                     args=(new_data.date, new_data.location, expedition_id))


def delete_expedition(expedition_id: int):
    return base_worker.execute_query(query="DELETE FROM expeditions WHERE id=?",
                                     args=(expedition_id,))
