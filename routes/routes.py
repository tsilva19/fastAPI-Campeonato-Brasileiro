from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from service.crud import criar_rodada, lista_rodada, atualiza_jogo #  update_game
from schemas.schemas import CriarRodadas, AtualizarJogo
from repository.database import SessionLocal
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/rodadas/", response_model=CriarRodadas)
def criar_rodada_api(dados_rodadas: CriarRodadas, db: Session = Depends(get_db)):
    cria_rodada = criar_rodada(db, dados_rodadas)
    return cria_rodada

@router.get("/rodadas/{numero_rodada}/")
def lista_rodada_api(numero_rodada: int, db: Session = Depends(get_db)):
    round_data = lista_rodada(db, numero_rodada)
    if not round_data:
        raise HTTPException(status_code=404, detail="rodada não encontrada")
    return round_data

@router.put("/rodadas/{numero_rodada}/jogos/{numero_jogo}/", response_model=AtualizarJogo)
def atualizar_jogo_api(numero_rodada: int, numero_jogo: int, atualiza_jogo_request: AtualizarJogo, db: Session = Depends(get_db)):
    atualizado = atualiza_jogo(db, numero_rodada, numero_jogo, atualiza_jogo_request)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return atualizado
