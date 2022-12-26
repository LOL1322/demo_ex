from server.sql_base.models import User
from server.sql_base.db_manager import base_worker


def create_user(user: User):
    return base_worker.execute_query(
        query="INSERT INTO users(personnel_id, login, password) VALUES (?, ?, ?) RETURNING id",
        args=(user.personnel_id, user.login, user.password))


def get_user(user_id: int):
    return base_worker.execute_query(query="SELECT id, personnel_id, login, password FROM users WHERE id = ?",
                                     args=(user_id,))


def get_all_user():
    return base_worker.execute_query(query="SELECT id, personnel_id, login, password FROM users",
                                     fetchone=False)


def update_user(user_id: int, new_data: User):
    return base_worker.execute_query(query="UPDATE users SET personnel_id=?, login=?, password=? WHERE id=?",
                                     args=(new_data.personnel_id, new_data.login, new_data.password, user_id))


def delete_user(user_id: int):
    return base_worker.execute_query(query="DELETE FROM users WHERE id=? ",
                                     args=(user_id,))


def check_login(login: User):
    return base_worker.execute_query(
        query="SELECT P.position_id FROM personnel P INNER JOIN users U ON U.personnel_id = P.user_id WHERE (U.login, U.password) = (?, ?)",
        args=(login.login, login.password))
