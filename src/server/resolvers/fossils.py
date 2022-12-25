from server.sql_base.models import Fossil
from server.sql_base.db_manager import base_worker


def create_fossil(fossil: Fossil):
    return base_worker.execute(query="INSERT INTO fossils(expedition_id, name, date_of_discovery, age, quantity) VALUES (?, ?, ?, ?, ?) RETURNING id",
                               args=(fossil.expedition_id, fossil.name, fossil.date, fossil.age, fossil.quantity))


def get_fossil(fossil_id: int):
    return base_worker.execute_query(query="SELECT id, expedition_id, name, date_of_discovery, age, quantity FROM fossils WHERE id = ?",
                                     args=(fossil_id,))


def get_all_fossil():
    return base_worker.execute(query="SELECT id, expedition_id, name, date_of_discovery, age, quantity FROM fossils",
                               many=True)


def update_fossil(fossil_id: int, new_data: Fossil):
    return base_worker.execute(query="UPDATE fossils SET expedition_id=?, name=?, date_of_discovery=?, age=?, quantity=? WHERE id=?",
                               args=(new_data.expedition_id, new_data.name, new_data.date, new_data.age, new_data.quantity, fossil_id))


def delete_fossil(fossil_id: int):
    return base_worker.execute(query="DELETE FROM fossils WHERE id=? ",
                               args=(fossil_id,))
