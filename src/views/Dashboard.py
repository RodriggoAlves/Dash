import customtkinter as ctk
from tkinter import*
from datetime import datetime as dt
import time
import webbrowser
from PopUp import PopUp


# Cores Padrçoes Utilizadas 

White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#4C22A5'
macos = "#D1CDD1"


def DashboardTela(Tela):
    Mydashboard = ctk.CTk()
    Mydashboard.geometry('1360x768')
    Mydashboard.config(bg=White)
    Mydashboard.resizable(True,True)
    Mydashboard.title('Dashboard')
    Mydashboard.attributes("-fullscreen",False)



    # Esse e o frame roxo atrás do menu

    Framemenu = ctk.CTkFrame(
                                    master=Mydashboard,
                                    width=282,
                                    height=768,
                                    fg_color=Purple,
                                    bg_color=White,
                                    corner_radius=30,
                                    border_color=White,
                                    border_width=1
                                            )
    Framemenu.place  (x=0,y=0)


    # "Framemenucorrect" E um frame para corrigir a borda
    # Pois não e possivel usar borda somente de um lado no CTK

    Framemenucorrect = ctk.CTkFrame(
                                    master=Mydashboard,
                                    width=251,
                                    height=768,
                                    fg_color=Purple,
                                    bg_color=Purple
                                            )
    Framemenucorrect.place  (x=0,y=0)


    # Botão no final de sair 

    # Imagem de Log Out
    ButtonLogOutImage = PhotoImage(file='Image/LogOutImage.png')
    
    #Função de sair do Dashboard
    def LogOut():
        Logout = ctk.CTk()
        Logout.geometry("400x200")
        Logout.title('Close')
        Logout.config(bg=White)
        Logout.resizable(False,False)


        MensagemSair = ctk.CTkLabel(
                                    master=Logout,
                                    text='Tem certeza \nque deseja sair?',
                                    font=('Poppins',20,'normal'),
                                    text_color=Purple,
                                    fg_color=White,
                                            )
        MensagemSair.place(x=116,y=48)

        # Botão para confirmar se quer sair 


        def Close():
            Mydashboard.destroy()
            Logout.destroy()

        buttonSim = ctk.CTkButton(
                                    master=Logout,
                                    width=67,height=26,
                                    fg_color=White,
                                    bg_color=White,
                                    text='Sim',
                                    text_color=Black,
                                    font=('Poppins',18,'normal'),
                                    corner_radius=12,
                                    border_width=1,
                                    border_color=Purple,
                                    hover_color=Purple,
                                    command=Close
                                            )
        buttonSim.place(x=116,y=124)

        def ContinueOpen():
            Logout.destroy()

        buttonNão = ctk.CTkButton(master=Logout,
                                    width=67,
                                    height=26,
                                    fg_color=White,
                                    bg_color=White,
                                    text='Não',
                                    text_color=Black,
                                    font=('Poppins',18,'normal'),
                                    corner_radius=12,
                                    border_width=1,
                                    border_color=Purple,
                                    hover_color=Purple,
                                    command=ContinueOpen
                                            )
        buttonNão.place(x=200,y=124)




        Logout.mainloop()


    # Botão de sair
    ButtonLogOut = ctk.CTkButton(master=Mydashboard,
                                    width=42,
                                    height=42,
                                    bg_color=Purple,
                                    fg_color=Purple,
                                    image=ButtonLogOutImage,
                                    text='',
                                    hover_color=Purplehover,
                                    command=LogOut
                                            )
    ButtonLogOut.place(x=120,y=634)


    # A Imagem do usuario 

    UserImage = PhotoImage(file='Image/UserImage.png')

    Userimageprofile = ctk.CTkLabel(master=Mydashboard,
                                    width=160,height=162,
                                    image=UserImage,
                                    fg_color=Purple,
                                    text='')
    Userimageprofile.place(x=57,y=51)


    # Saldo do usuario


    Economyimage = PhotoImage(file='Image/MoneyImage.png')

    ButtonEconomy = ctk.CTkButton(
                                    master=Mydashboard,
                                    image=Economyimage,
                                    width=240,
                                    height=58,
                                    fg_color=White,
                                    bg_color=White,
                                    text='$   689,00',
                                    text_color=Black,
                                    font=('Poppins',25,'bold'),
                                    corner_radius=12,
                                    border_color=Black,
                                    border_width=2,
                                    hover=White,
                                    command=Tela
                                            )
    ButtonEconomy.place(x=445,y=123)

    # botão que mostra a Data 
    
    def MostrarData():
        data = dt.now()
        DataDayYears = data.strftime("%d/%m/%y  ")
        Calendarimage = PhotoImage(file='Image/CalendarImage.png')
        ButtonCalendar = ctk.CTkButton(master=Mydashboard,image=Calendarimage,
                                  width=240,height=58,
                                  text=DataDayYears,text_color=Black,
                                  font=('Poppins',25,'bold'),
                                  corner_radius=12,border_color=Black,border_width=2,
                                  fg_color=White,bg_color=White,
                                  hover=White)
        ButtonCalendar.place(x=738,y=123)
        Mydashboard.after(10000,MostrarData)

    MostrarData()

    # Botões centrais da tela 
  
    # Botão de Metas
    buttonMetas = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=533,
                                    height=76,
                                    bg_color=White,
                                    fg_color=Purple,
                                    text='Metas',
                                    font=('Inter',25,'bold'),
                                    text_color=White,
                                    corner_radius=20,
                                    border_width=2,
                                    border_color=Black,
                                    hover_color=Purplehover
                                            )
    buttonMetas.place(x=445,y=255)

    #Botão de Notas
    buttonNotas = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=533,
                                    height=76,
                                    text='Notas',
                                    font=('Inter',25,'bold'),
                                    text_color=White,
                                    bg_color=White,
                                    fg_color=Purple,
                                    corner_radius=20,
                                    border_width=2,
                                    border_color=Black,
                                    hover_color=Purplehover
                                            )
    buttonNotas.place(x=445,y=362)

    #Botão de Horários
    buttonHorarios = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=533,
                                    height=76,
                                    text='Horários',
                                    font=('Inter',25,'bold'),
                                    text_color=White,
                                    bg_color=White,
                                    fg_color=Purple,
                                    corner_radius=20,
                                    border_width=2,
                                    border_color=Black,
                                    hover_color=Purplehover
                                            )
    buttonHorarios.place(x=445,y=469)
    
    #Botão de ajustes
    buttonAjustes = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=533,
                                    height=76,
                                    bg_color=White,
                                    fg_color=Purple,
                                    text='Ajustes',
                                    font=('Inter',25,'bold'),
                                    text_color=White,
                                    corner_radius=20,
                                    border_width=2,
                                    border_color=Black,
                                    hover_color=Purplehover
                                            )
    buttonAjustes.place(x=445,y=576)

    # Função do Botão do instagram 

    InstagramImage = PhotoImage(file='Image/InstagramImage.png')
    def LinkInstagram():
        urlinstagram = 'https://www.instagram.com/rodriggo.sx'
        webbrowser.open_new(urlinstagram)

    ButtonInstagram = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=33,
                                    height=43,
                                    fg_color=White,
                                    bg_color=White,
                                    image=InstagramImage,
                                    command=LinkInstagram,
                                    hover_color=White,
                                    corner_radius=12,
                                    border_color=Purple,
                                    text=''
                                            )
    ButtonInstagram.place(x=645,y=685)

    # Função do botão do YouTube

    InstagramImage = PhotoImage(file='Image/YoutubeImage.png')
    def LinkYouTube():
        urlYouTube = 'https://www.youtube.com/@rzndmodder'
        webbrowser.open_new(urlYouTube)

    ButtonYoutube = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=40,
                                    height=43,
                                    fg_color=White,
                                    bg_color=White,
                                    image=InstagramImage,
                                    command=LinkYouTube,
                                    hover_color=White,
                                    corner_radius=12,
                                    border_color=Purple,
                                    text=''
                                            )
    ButtonYoutube.place(x=696,y=685)

    # Função do botão do WhatsApp

    WhatsAppImage = PhotoImage(file='Image/WhatsappImage.png')

    def LinkWhatsApp():
        urlWhatsApp = 'https://wa.me/5562981917921'
        webbrowser.open_new(urlWhatsApp)

    ButtonWhatsApp = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=40,
                                    height=43,
                                    image=WhatsAppImage,
                                    command=LinkWhatsApp,
                                    fg_color=White,
                                    bg_color=White,
                                    hover_color=White,
                                    corner_radius=12,
                                    border_color=Purple,
                                    text=''
                                            )
    ButtonWhatsApp.place(x=745,y=685)
    
    # Mostrar hora na tela 

    def MostrarHoras():
        horas = dt.now()
        horascomseconds = horas.strftime("%H:%M:%S")

        texthoras = ctk.CTkLabel(
                                    master=Mydashboard,
                                    width=66,
                                    height=30,
                                    fg_color=White,
                                    bg_color=White,
                                    text=horascomseconds,
                                    font=('Poppins',25,'normal'),
                                    text_color=Black
                                            )
        texthoras.place(x=1200,y=20)

        Mydashboard.after(1000,MostrarHoras)
        
    MostrarHoras()
    
    # Mostrar o calendario na tela

    Calendarrightimage = PhotoImage(file='Image/CalendarrigthImage.png')

    calendartight = ctk.CTkLabel(
                                    master=Mydashboard,
                                    width=237,
                                    height=191,
                                    image=Calendarrightimage,
                                    text='',
                                    fg_color=White,
                                    bg_color=White
                                            )
    calendartight.place(x=1092,y=123)

    # Leitura de livros
    # Label com a Borda

    Leituralabel = ctk.CTkButton(
                                    master=Mydashboard,
                                    width=191,
                                    height=362,
                                    fg_color=White,
                                    bg_color=White,
                                    text='',
                                    hover_color=White,
                                    corner_radius=12,
                                    border_color=Purplehover,
                                    border_width=2
                                            )
    Leituralabel.place(x=1120,y=361)


    Mydashboard.mainloop()


