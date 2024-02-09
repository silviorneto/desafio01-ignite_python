import os
from sys import platform

from pyagenda.agenda import Agenda
from pyagenda.contact import Contact


def clear_terminal():
    if platform.startswith("win"):
        os.system("cls")  # Limpar terminal no Windows
    elif platform.startswith("linux") or platform.startswith("darwin"):
        os.system("clear")  # Limpar terminal no Linux/Mac


def receive_contact_info(is_new: bool = True) -> dict:
    """
    Receives the contact informations from the user.

    Returns:
        dict: contact informations.
    """
    if is_new:
        msg = "Escreva abaixo as informações do contato:"
    else:
        msg = "Escreva abaixo as informações do contato [s para pular]:"

    print(msg)
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")

    return {
        "name": name if is_new or name not in ["S", "s"] else None,
        "phone": phone if is_new or phone not in ["S", "s"] else None,
        "email": email if is_new or email not in ["S", "s"] else None,
    }


def menu() -> str:
    print("\n##### PyAgenda #####\n")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Listar favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    return input("\nDigite a opção desejada [1 - 6]: ")


def run():
    agenda = Agenda()

    while True:

        menu_option = menu()

        try:
            clear_terminal()
            menu_option = int(menu_option)
            match menu_option:
                case 1:
                    print("1. Adicionar contato\n")
                    contact_dict = receive_contact_info()
                    agenda.add_contact(Contact(**contact_dict))
                case 2:
                    print("2. Listar contatos\n")
                    agenda.list_contacts()
                case 3:
                    print("3. Editar contato\n")
                    contact_uuid = input("Id do contato: ")
                    contact_dict = receive_contact_info(is_new=False)
                    agenda.edit_contact(
                        uuid=contact_uuid,
                        name=contact_dict["name"],
                        phone=contact_dict["phone"],
                        email=contact_dict["email"],
                    )
                case 4:
                    print("4. Marcar/Desmarcar contato como favorito\n")
                    contact_uuid = input("Id do contato: ")
                    agenda.mark_favorite(uuid=contact_uuid)
                case 5:
                    print("5. Listar favoritos\n")
                    agenda.list_favorites()
                case 6:
                    print("6. Apagar contato\n")
                    contact_uuid = input("Id do contato: ")
                    agenda.delete_contact(uuid=contact_uuid)
                case 7:
                    print("Encerrando o programa...")
                    break
                case _:
                    print("Opção inválida. Favor tente novamente.")
        except (ValueError, TypeError):
            print("Erro: Opção inválida. Favor tente novamente.")
        except Exception as e:
            print(f"Erro: {e}")
