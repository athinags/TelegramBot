from bot_instance import bot

import handlers.start
import handlers.contato
import handlers.contato_callbacks

from db.connection import engine
from db.base import Base

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    bot.polling()