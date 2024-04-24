from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest  

db_connection_handler.connect_to_db()

@pytest.mark.skip
def test_insert_attendee():
    event_id = "meu-uuid1"
    attendees_info = {
        "uuid": "uuid-attendee1",
        "name": "name",
        "email": "email@email.com",
        "event_id": event_id 
    }

    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendees(attendees_info)
    print(response)

@pytest.mark.skip
def test_get_attendee_badge_by_id():
    attendees_id="uuid-attendee1"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendees_id)
    print(attendee)