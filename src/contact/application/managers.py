from sqlalchemy.orm import Session

from src.contact.application.dtos import ContactDTO
from src.contact.domain.repositories import ContactRepository
from src.models import ContactMessage


class ContactManager(object):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def create_new_contact(self, contact_dto: ContactDTO) -> ContactMessage:
        contact_entity = contact_dto.to_domain()
        contact_entity.is_valid()

        repository = ContactRepository()
        contact = repository.create(contact_entity, session=self.session)

        return contact
