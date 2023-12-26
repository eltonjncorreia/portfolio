from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ContactMessage(Base):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    subject: Mapped[str]
    message: Mapped[str]
