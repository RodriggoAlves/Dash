import customtkinter as ctk
from AdicionarSaldo import*



White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#4C22A5'
macos = "#D1CDD1"

def ListaDeTransacoes():
     transações = ctk.CTk()
     transações.geometry("850x500")
     transações.title("lista De transações")
     transações.config(bg=White)
     transações.resizable(False,False)
    
     mytransations = ctk.CTkLabel(
                                    master=transações,
                                    text='R$ 700,80',
                                    text_color=Purple,
                                    font=("Poppins",50,"normal"),
                                    fg_color=White
                                            )
     mytransations.place(x=305,y=58)

     buttonaddvalor = ctk.CTkButton(
                                    master=transações,
                                    width=224,
                                    height=44,
                                    text='+ Adicionar valor',
                                    font=("Poppins",20,"normal"),
                                    text_color=Purple,
                                    bg_color=White,
                                    fg_color=White,
                                    hover_color="#9B6EFB",
                                    corner_radius=30,
                                    border_color=Purple,
                                    border_width=2,
                                    command=AdicionarSaldo
                                            )
     buttonaddvalor.place(x=313,y=162)

     linesOne = ctk.CTkFrame(
                                    master=transações,
                                    width=764,
                                    height=194,
                                    fg_color=White,
                                    bg_color=White,
                                    border_width=2,
                                    border_color=Purple
                                            )
     linesOne.place(x=43,y=249)

     textoId = ctk.CTkLabel(
                                    master=transações,
                                    text="ID",
                                    fg_color=White,
                                    bg_color=White,
                                    text_color=Black,
                                    font=("Poppins",18,"normal")
                                            )
     textoId.place(x=88,y=251)

     textTransation = ctk.CTkLabel(
                                    master=transações,
                                    text="Nome da transação",
                                    fg_color=White,
                                    bg_color=White,
                                    text_color=Black,
                                    font=("Poppins",18,"normal")
                                            )
     textTransation.place(x=333,y=251)    

     textData = ctk.CTkLabel(
                                    master=transações,
                                    text="Data",
                                    fg_color=White,
                                    bg_color=White,
                                    text_color=Black,
                                    font=("Poppins",18,"normal")
                                            )
     textData.place(x=730,y=251)   

     linesTwo = ctk.CTkFrame(
                                    master=transações,
                                    width=760,
                                    height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesTwo.place(x=45,y=276)

     linesTree = ctk.CTkFrame(
                                    master=transações,
                                    width=760,
                                    height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesTree.place(x=45,y=304)  

     linesFor = ctk.CTkFrame(
                                    master=transações,
                                    width=760,height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesFor.place(x=45,y=332)  
     
     linesfive = ctk.CTkFrame(
                                    master=transações,
                                    width=760,height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesfive.place(x=45,y=304)  

     linessix = ctk.CTkFrame(
                                    master=transações,
                                    width=760,
                                    height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linessix.place(x=45,y=360) 

     linesseven = ctk.CTkFrame(
                                    master=transações,
                                    width=760,height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesseven.place(x=45,y=388) 

     linesEight = ctk.CTkFrame( 
                                    master=transações,
                                    width=760,height=2,
                                    fg_color=Purple,
                                    bg_color=White,
                                            )
     linesEight.place(x=45,y=416) 

     lineHorizontalOne = ctk.CTkFrame(
                                    master=transações,
                                    width=2,height=190,
                                    bg_color=Purple,
                                    fg_color=Purple
                                            )
     lineHorizontalOne.place(x=152,y=251)

     lineHorizontalTwo = ctk.CTkFrame(
                                    master=transações,
                                    width=2,
                                    height=190,
                                    bg_color=Purple,
                                    fg_color=Purple
                                            )
     lineHorizontalTwo.place(x=696,y=251)
     

     transações.mainloop()

