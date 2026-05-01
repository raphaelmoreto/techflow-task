from fastapi import FastAPI
from api.controllers.tasks_controller import tasks_controller

#EXECUTAR NO TERMINAL
#pip install fastapi uvicorn
#pip install -r requirements.txt
#python app.py

#RODAR A APLPICAÇÃO
#uvicorn main:app --reload

#ACESSAR NO NAVEGADOR
#http://127.0.0.1:8000/docs

app = FastAPI()

app.include_router(tasks_controller)