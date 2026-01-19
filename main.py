from fastapi import FastAPI
from pydantic import BaseModel # <--- Adicione esta parte
# Inicializa a aplicação
app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float
    em_oferta: bool = None

# Define a rota raiz
@app.get("/")
def ler_raiz():
    return {"mensagem": "Olá, mundo!"}

# Define a rota saudacao
@app.get("/saudacao")
def ler_saudacao():
    return {"mensagem": "Olá, Geovani!"}

@app.get("/ola/{nome}")
def cumprimentar_pessoa(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

# @app.get("/itens/{item_id}")
# def ler_item(item_id: int):
#     return {"item_id": item_id}

@app.post("/itens/")
def criar_item(item: Item):
    return item