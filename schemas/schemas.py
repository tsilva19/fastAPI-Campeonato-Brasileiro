from pydantic import BaseModel
from typing import List

class Jogo(BaseModel):
    time_a: str
    time_b: str
    gol_time_a: int = 0
    gol_time_b: int = 0

class CriarRodadas(BaseModel):
    numero_rodada: int
    jogos: List[Jogo]


