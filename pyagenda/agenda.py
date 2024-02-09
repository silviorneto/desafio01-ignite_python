from typing import List, Optional

from pyagenda.contact import Contact


class Agenda:
    """
    Class that represents an agenda

    Attributes:
        contacts (List[Contact]): contact list.
    """

    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def _get_contact_by_id(self, uuid: str) -> Contact | None:
        for contact in self.contacts:
            if str(contact.id) == uuid:
                return contact
        return None

    def add_contact(self, new_contact: Contact) -> None:
        """
        Adds a new contact to the contact list.

        Args:
            new_contact (Contact): a contact data represented by an instance of Contact. # noqa

        Returns:
            None
        """
        self.contacts.append(new_contact)
        print(f"\nAdicionado {new_contact.name} [id: {new_contact.id}]!")

    def list_contacts(self):
        """
        Lists all the contacts in the contact list.

        Returns:
            None
        """
        print("\nListando contatos...")
        for contact in self.contacts:
            print(f"{contact}")

    def edit_contact(
        self,
        uuid: str,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
    ) -> None:
        """
        Edits an existing contact in the contact list.

        Args:
            uuid (str): The uuid of the contact
            name (str | None, optional): The name of the contact. Defaults to None. # noqa
            phone (str | None, optional): The phone of the contact. Defaults to None. # noqa
            email (str | None, optional): The email of the contact. Defaults to None. # noqa

        Returns:
            None
        """
        contact = self._get_contact_by_id(uuid)
        if contact is None:
            print("\nContato não encontrado!")
            return

        contact.update({"name": name, "phone": phone, "email": email})
        print(f"\nAtualizado {contact.name} [id: {contact.id}]!")

    def mark_favorite(self, uuid: str) -> None:
        """
        Marks an existing contact in the contact list as favorite.

        Args:
            uuid (str): an id of contact. # noqa
        """
        contact = self._get_contact_by_id(uuid)
        if contact is None:
            print("\nContato não encontrado!")
            return

        contact.handle_favorite()
        print(f"\nAtualizado {contact.name} [id: {contact.id}] como favorito!")  # noqa

    def list_favorites(self) -> None:
        """
        Lists all the favorite contacts in the contact list.

        Returns:
            None
        """
        print("Listando favoritos...")
        for contact in self.contacts:
            if contact.is_favorited:
                print(f"{contact !s}")

    def delete_contact(self, uuid: str) -> None:
        """
        Deletes an existing contact in the contact list.

        Args:
            uuid (str): an id of contact. # noqa
        """
        contact = self._get_contact_by_id(uuid)
        if contact is None:
            print("\nContato não encontrado!")
            return

        self.contacts.remove(contact)
        print(f"{contact.name} deletado!")
