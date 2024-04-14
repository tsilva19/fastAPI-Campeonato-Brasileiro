from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from repository.database import Base

class Rodada(Base):
    __tablename__ = "rodadas"

    id = Column(Integer, primary_key=True, index=True)
    numero_rodada = Column(Integer)

    jogos = relationship("Jogo", back_populates="rodada")

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    numero_jogo = Column(Integer)
    time_a = Column(String(255))  # Adicionando o comprimento máximo
    gol_time_a = Column(Integer, default=0)
    time_b = Column(String(255))  # Adicionando o comprimento máximo
    gol_time_b = Column(Integer, default=0)

    rodada_id = Column(Integer, ForeignKey("rodadas.id"))
    rodada = relationship("Rodada", back_populates="jogos")
