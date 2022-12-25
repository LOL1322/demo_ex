from server.sql_base.models import Personnel
from server.sql_base.db_manager import base_worker


def create_personnel(personnel: Personnel):
    return base_worker.execute(query="INSERT INTO personnel(position_id, user_id, name, surname, phone, date_birth) VALUES (?, ?, ?, ?, ?, ?) RETURNING id",
                               args=(personnel.position_id, personnel.user_id, personnel.name, personnel.surname, personnel.phone, personnel.date))


def get_personnel(personnel_id: int):
    return base_worker.execute_query(query="SELECT id,  user_id, position_id, user_id, name, surname, phone, date_birth FROM personnel WHERE id = ?",
                                     args=(personnel_id,))


def get_all_personnel():
    return base_worker.execute(query="SELECT id, position_id, user_id, name, surname, phone, date_birth FROM personnel",
                               many=True)


def update_personnel(personnel_id: int, new_data: Personnel):
    return base_worker.execute(query="UPDATE personnel SET position_id=?, user_id=?, name=?, surname=?, phone=?, date_birth=? WHERE id=?",
                               args=(new_data.position_id, new_data.user_id, new_data.name, new_data.surname, new_data.phone, new_data.date, personnel_id))


def delete_personnel(personnel_id: int):
    return base_worker.execute(query="DELETE FROM personnel WHERE id=? ",
                               args=(personnel_id,))
