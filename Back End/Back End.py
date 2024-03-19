import customtkinter as ctk
from datetime import datetime as dt
import time




# Função do relogio
def MostrarHoras():
    horas = dt.now()
    horascomseconds = horas.strftime("%d/%m/%y")
    print(horascomseconds)
    
MostrarHoras()

