from sqlalchemy.orm import Session
from src.contact.domain.entities import ContactMessageEntity
from src.models import ContactMessage


class ContactRepository:

    def create(self, contact_entity: ContactMessageEntity, session: Session) -> ContactMessage:
        try:
            contact = ContactMessage(
                name=contact_entity.name,
                email=contact_entity.email,
                phone=contact_entity.phone,
                subject=contact_entity.subject,
                message=contact_entity.message,
            )

            session.add(contact)

            session.commit()

        except Exception as e:
            session.rollback()
            raise e

        return contact
