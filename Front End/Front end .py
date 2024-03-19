import customtkinter as ctk
from tkinter import*
import datetime as dt
import time
import webbrowser

# Cores Padrçoes Utilizadas 

White = '#ffffff'
Black = '#000000'
Purple = '#2D087C'
Purplehover = '#4C22A5'





def Dashboard():
    Mydashboard = ctk.CTk()
    Mydashboard.geometry('1360x768')
    Mydashboard.config(bg=White)
    Mydashboard.resizable(False,False)
    Mydashboard.title('Dashboard')
    Mydashboard.attributes("-fullscreen",True)

    # botão da economia 

    Economyimage = PhotoImage(file='C:\\Users\\rodri\\OneDrive\\Desktop\\Dash\\Image\\MoneyImage.png')

    ButtonEconomy = ctk.CTkButton(master=Mydashboard,image=Economyimage,
                                  width=240,height=58,
                                  text='$   689,00',text_color=Black,font=('Inter',25,'bold'),
                                  corner_radius=12,border_color=Black,border_width=2,
                                  fg_color=White,bg_color=White,
                                  hover=White)
    ButtonEconomy.place(x=445,y=123)


    # botão da Data 
    
    Calendarimage = PhotoImage(file='C:\\Users\\rodri\\OneDrive\\Desktop\\Dash\\Image\\CalendarImage.png')

    ButtonEconomy = ctk.CTkButton(master=Mydashboard,image=Calendarimage,
                                  width=240,height=58,
                                  text='  18/03/2024',text_color=Black,font=('Inter',25,'bold'),
                                  corner_radius=12,border_color=Black,border_width=2,
                                  fg_color=White,bg_color=White,
                                  hover=White)
    ButtonEconomy.place(x=738,y=123)


    # Botões da tela 

    buttonMetas = ctk.CTkButton(master=Mydashboard,
                                width=533,height=76,
                                text='Metas',font=('Inter',25,'bold'),
                                text_color=White,
                                bg_color=White,fg_color=Purple,
                                corner_radius=20,border_width=2,border_color=Black,
                                hover_color=Purplehover)
    buttonMetas.place(x=445,y=255)


    buttonNotas = ctk.CTkButton(master=Mydashboard,
                                width=533,height=76,
                                text='Notas',font=('Inter',25,'bold'),
                                text_color=White,
                                bg_color=White,fg_color=Purple,
                                corner_radius=20,border_width=2,border_color=Black,
                                hover_color=Purplehover)
    buttonNotas.place(x=445,y=362)


    buttonHorarios = ctk.CTkButton(master=Mydashboard,
                                width=533,height=76,
                                text='Notas',font=('Inter',25,'bold'),
                                text_color=White,
                                bg_color=White,fg_color=Purple,
                                corner_radius=20,border_width=2,border_color=Black,
                                hover_color=Purplehover)
    buttonHorarios.place(x=445,y=469)
    

    buttonAjustes = ctk.CTkButton(master=Mydashboard,
                                width=533,height=76,
                                text='Ajustes',font=('Inter',25,'bold'),
                                text_color=White,
                                bg_color=White,fg_color=Purple,
                                corner_radius=20,border_width=2,border_color=Black,
                                hover_color=Purplehover)
    buttonAjustes.place(x=445,y=576)


    InstagramImage = PhotoImage(file='C:\\Users\\rodri\\OneDrive\\Desktop\\Dash\\Image\\InstagramImage.png')


    def LinkInstagram():
        urlinstagram = 'https://www.instagram.com/rodriggo.sx'
        webbrowser.open_new(urlinstagram)

    ButtonInstagram = ctk.CTkButton(master=Mydashboard,image=InstagramImage,command=LinkInstagram,
                                    text='',
                                    corner_radius=12,border_width=1,border_color=Purple,
                                    fg_color=White,bg_color=White,hover_color=White,
                                    width=33,height=43)
    ButtonInstagram.place(x=634,y=685)

    


    
    
    Mydashboard.mainloop()



Dashboard()

