from app.database import Base
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import String

class User(Base):
    __tablename__="users"

    id: Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(50))
    email:Mapped[str]=mapped_column(String(100),unique=True)