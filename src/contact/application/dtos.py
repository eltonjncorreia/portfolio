from dataclasses import dataclass

from src.contact.domain.entities import ContactMessageEntity


@dataclass
class ContactDTO:
    name: str
    email: str
    phone: str
    subject: str
    message: str

    def to_domain(self) -> ContactMessageEntity:
        return ContactMessageEntity(
            name=self.name,
            email=self.email,
            phone=self.phone,
            subject=self.subject,
            message=self.message,
        )
