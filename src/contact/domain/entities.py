from dataclasses import dataclass


@dataclass
class ContactMessageEntity:
    name: str
    email: str
    phone: str
    subject: str
    message: str

    def is_valid(self):
        clean_number = "".join(filter(str.isdigit, self.phone))

        if len(clean_number) != 11:
            raise ValueError("Número de telefone inválido para o Brasil")

        return True
