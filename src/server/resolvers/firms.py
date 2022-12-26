from server.sql_base.models import Firm
from server.sql_base.db_manager import base_worker


def create_firm(firm: Firm):
    return base_worker.execute_query(query="INSERT INTO firms(title, location) VALUES (?, ?) RETURNING id",
                                     args=(firm.title, firm.location))


def get_firm(firm_id: int):
    return base_worker.execute_query(query="SELECT id, title, location FROM firms WHERE id = ?",
                                     args=(firm_id,))


def get_all_firm():
    return base_worker.execute_query(query="SELECT id, title, location FROM firms",
                                     fetchone=False)


def update_firm(firm_id: int, new_data: Firm):
    return base_worker.execute_query(query="UPDATE firms SET title=?, location=? WHERE id=?",
                                     args=(new_data.title, new_data.location, firm_id))


def delete_firm(firm_id: int):
    return base_worker.execute_query(query="DELETE FROM firms WHERE id=? ",
                                     args=(firm_id,))
