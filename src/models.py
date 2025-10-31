from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class AlunoExemplo(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, index=True)
    RA = Column(String, unique=True)
