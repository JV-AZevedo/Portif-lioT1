from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/perfil")
def perfil():
    return {"nome": "João Vitor Azevedo Almeida","idade":"19",
            "escolaridade":"Cursando Engenharia da Computação (Faculdade Fastech), 3º Semestre",
            "projetos": "Irrigador automático com arduíno, portifólio T1"}
