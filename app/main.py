from fastapi import FastAPI
from app.api.controllers.tasks_controller import tasks_controller

#EXECUTAR NO TERMINAL
#pip install fastapi uvicorn
#python app.py

#RODAR A APLICAÇÃO À PARTIR DA PASTA 'Techflow-Task'. Exemplo no terminal:
#C:\Users\{seu usuario}\{caminho onde está salvo o projeto na sua máquina}\Techflow-Task> uvicorn app.main:app --reload
#uvicorn app.main:app --reload

#ACESSAR NO NAVEGADOR
#http://127.0.0.1:8000/docs

app = FastAPI()

app.include_router(tasks_controller)