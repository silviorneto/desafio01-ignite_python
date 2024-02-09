from uuid import uuid4


class Contact:
    """
    Class that represents a contact

    Attributes:
        id (UUID): the id of the contact
        name (str): the name of the contact.
        phone (str): the phone number of the contact.
        email (str): the email of the contact.
        is_favorited (bool): whether the contact is favorited.
    """

    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
    ):
        self.id = uuid4()
        self.name = name
        self.phone = phone
        self.email = email
        self.is_favorited = False

    def __repr__(self):
        return f"<Contact[name={self.name}, phone={self.phone}, email={self.email}, is_favorited={self.is_favorited}]>"  # noqa

    def __str__(self):
        return f"----------------------------------------------------------------\nId: {self.id}\nName: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nIs Favorite: {self.is_favorited}\n----------------------------------------------------------------"  # noqa

    def update(self, attrs: dict) -> None:
        """
        Updates the attributes of the contact.

        Args:
            attrs (dict): the attributes to update.

        Returns:
            None
        """
        for attr in attrs.items():
            if attr[1] is None:
                continue
            setattr(self, attr[0], attr[1])

    def handle_favorite(self):
        """
        Toggles the is_favorited attribute.

        Returns:
            None
        """
        self.is_favorited = not self.is_favorited
