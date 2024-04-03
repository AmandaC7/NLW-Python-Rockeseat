import pytest
from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid1",
        "title": "title",
        "slug": "slug",
        "maximum_attendees": 150
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

def test_get_event_by_id():
    event_id = "meu-uuid1"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
