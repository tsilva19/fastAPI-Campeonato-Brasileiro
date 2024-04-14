from sqlalchemy.orm import Session, joinedload

from models.models import Jogo, Rodada
from schemas.schemas import CriarRodadas
from typing import List

def criar_rodada(db: Session, dados_rodadas: CriarRodadas):
    rodada_db = Rodada(numero_rodada=dados_rodadas.numero_rodada)
    
    for index, jogo_data in enumerate(dados_rodadas.jogos, start=1):
        time_a = jogo_data.time_a  # Acessa o atributo diretamente
        time_b = jogo_data.time_b  # Acessa o atributo diretamente
        
        if time_a == time_b:
            raise ValueError("O mesmo time não pode jogar consigo mesmo em um jogo.")
        
        jogo_db = Jogo(
            numero_jogo=index,
            time_a=time_a,
            gol_time_a=0,  # Valor default
            time_b=time_b,
            gol_time_b=0   # Valor default
        )
        rodada_db.jogos.append(jogo_db)
    
    db.add(rodada_db)
    db.commit()
    db.refresh(rodada_db)
    
    return rodada_db

def lista_rodada(db: Session, numero_rodada: int):
     rodada = db.query(Rodada).filter(Rodada.numero_rodada == numero_rodada).first()
    
     if not rodada:
        return None  # Retorna None se a rodada não for encontrada
    
    # Carrega os jogos vinculados à rodada
     rodada_com_jogos = db.query(Rodada).options(joinedload(Rodada.jogos)).filter(Rodada.id == rodada.id).first()
    
     return rodada_com_jogos