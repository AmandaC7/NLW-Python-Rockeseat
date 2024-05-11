from .check_ins_repository import CheckInRepository
from src.models.settings.connection import db_connection_handler
import pytest  

db_connection_handler.connect_to_db()

def test_insert_check_in():
    attendee_id = "uuid-attendee1"

    check_in_repository = CheckInRepository()
    response = check_in_repository.insert_check_in(attendee_id)
    print(response)
