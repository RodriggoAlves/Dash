import customtkinter as ctk
from PopUp import*
from ConfirmarSenha import*


White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#4C22A5'
macos = "#D1CDD1"



def AdicionarSaldo():
        money = ctk.CTk()
        money.geometry("850x500")
        money.config(bg=White)
        money.title("Adicionar Transação")
        money.resizable(False,False)
        money.iconbitmap("image/DashboardIcon.ico")

        nameUser = ctk.CTkLabel(
                                    master=money,
                                    width=260,
                                    height=29,
                                    text='Olá Rodriggo',
                                    font=('Poppins',40,'normal'),
                                    text_color=Purple,
                                    fg_color=White,
                                    bg_color=White
                                            )
        nameUser.place(x=295,y=100)

        NomeDaTransacao = ctk.CTkEntry(
                                    master=money,
                                    width=344,
                                    height=51,
                                    fg_color=White,
                                    bg_color=White,
                                    corner_radius=12,
                                    border_color=Purple,
                                    border_width=1,
                                    placeholder_text="R$   Adicione um saldo...",
                                    font=("Poppins",24,"normal"),
                                    text_color=Purple
                                            )
        NomeDaTransacao.place(x=253,y=199)

        addMoney = ctk.CTkEntry(
                                    master=money,
                                    width=344,
                                    height=51,
                                    fg_color=White,
                                    bg_color=White,
                                    corner_radius=12,
                                    border_color=Purple,
                                    border_width=1,
                                    placeholder_text="Nome da transação",
                                    font=("Poppins",24,"normal"),
                                    text_color=Purple
                                            )
        addMoney.place(x=253,y=273)

        saveMoneyadd = ctk.CTkButton(
                                    master=money,
                                    width=170,
                                    height=40,
                                    text="Continuar",
                                    font=("Poppins",24,"normal"),
                                    corner_radius=12,
                                    border_color=Purple,
                                    border_width=1,
                                    text_color=Black,
                                    hover_color=Purple,
                                    text_color_disabled=Black,
                                    fg_color=White,
                                    bg_color=White,
                                    command=ConfirmarSenha
                                    )
        saveMoneyadd.place(x=340,y=346)

        money.mainloop()
