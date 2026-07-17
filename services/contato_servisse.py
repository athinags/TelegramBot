from db.connection import SessionLocal
from db.models.contato import Contato

def salvar_contato(user_name: str, option: str):
    session = SessionLocal()
    try:
        contato = Contato(
        user_name=user_name,
        option=option
        )
        session.add(contato)
        session.commit()
    finally:
        session.close()
