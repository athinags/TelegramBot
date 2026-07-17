from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from db.base import Base

class Contato(Base):
    __tablename__ = "contatos"
    
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    option = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))