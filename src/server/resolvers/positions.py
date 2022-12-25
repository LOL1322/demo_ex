from server.sql_base.models import Position
from server.sql_base.db_manager import base_worker


def create_position(position: Position):
    return base_worker.execute(query="INSERT INTO positions(position) VALUES (?) RETURNING id",
                               args=(position.post,))


def get_position(position_id: int):
    return base_worker.execute_query(query="SELECT id, position FROM positions WHERE id = ?",
                                     args=(position_id,))


def get_all_position():
    return base_worker.execute(query="SELECT id, position FROM positions",
                               many=True)


def update_position(position_id: int, new_data: Position):
    return base_worker.execute(query="UPDATE positions SET position=? WHERE id=?",
                               args=(new_data.post, position_id))


def delete_position(position_id: int):
    return base_worker.execute(query="DELETE FROM positions WHERE id=? ",
                               args=(position_id,))
