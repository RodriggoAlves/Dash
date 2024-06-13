import customtkinter as ctk 


# Cores Padrçoes Utilizadas 
White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#7c6dc7'
macos = "#D1CDD1"


def TelaDeLogin():
    Login = ctk.CTk()
    Login.title("Login")
    Login.geometry("500x600")
    Login.resizable(False,False)
    Login.config(bg=White)

    TitleLogin= ctk.CTkLabel(master=Login,
                             text="LOGIN",
                             width=118,
                             height=60,
                             text_color=Purple,
                             font=('Poppins',40,'normal'),
                             bg_color=White)
    
    TitleLogin.place(x=191,y=112)

    EntryUser = ctk.CTkEntry(master=Login,
                              width=268,
                              height=35,
                              fg_color=White,
                              bg_color=White,
                              corner_radius=30,
                              border_color=Purple,
                              placeholder_text="Usuário",
                              font=("Poppins",15,"normal"),
                              text_color=Purple,
                              )
    EntryUser.place(x=116,y=248)

    EntryPassowrd = ctk.CTkEntry(master=Login,
                              width=268,
                              height=35,
                              fg_color=White,
                              bg_color=White,
                              corner_radius=30,
                              border_color=Purple,
                              placeholder_text="Senha",
                              font=("Poppins",15,"normal"),
                              text_color=Purple,
                              )
    EntryPassowrd.place(x=116,y=300)

    ButtonLogin = ctk.CTkButton(master=Login,
                                text="Fazer Login",
                                bg_color=White,
                                fg_color=White,
                                corner_radius=30,
                                border_width=2,
                                border_color=Purple,
                                text_color=Black,
                                font=("Poppins",15,"normal"),
                                hover_color=Purplehover)
    ButtonLogin.place(x=178,y=362)


    Login.mainloop()


