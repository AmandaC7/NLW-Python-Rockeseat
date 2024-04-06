from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.check_ins import CheckIns
from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class CheckInRepository:

    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(attendeeId=attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            
            except IntegrityError:
                 raise Exception('Check In ja cadastrado')
            except Exception as exception:
                 database.session.rollback()
                 raise exception
    
    def get_check_in_by_id(self, check_in_id: int):
         with db_connection_handler as database:
            try:
                check_in = (
                    database.session
                        .query(CheckIns)
                        .join(Attendees, Attendees.id==CheckIns.attendeeId)
                        .filter(CheckIns.id==check_in_id)
                        .with_entities(
                            CheckIns.id,
                            Attendees.name                  
                        )
                        .one()
                )
                return check_in
            except NoResultFound:
                return None