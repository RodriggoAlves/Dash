import customtkinter as ctk 

# Cores Padrões Utilizadas
White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#7c6dc7'

def TelaDeLogin():
    ctk.set_appearance_mode("light")  # Definir o modo de aparência para claro
    Login = ctk.CTk()
    Login.title("Login")
    Login.geometry("500x600")
    Login.resizable(True, True)  # Permitir redimensionamento
    Login.config(bg=White)
    Login.iconbitmap("image/DashboardIcon.ico")

    # Container para o título
    frame_title = ctk.CTkFrame(master=Login, fg_color=White, bg_color=White)
    frame_title.pack(pady=50)

    TitleLogin = ctk.CTkLabel(master=frame_title,
                              text="LOGIN",
                              width=118,
                              height=60,
                              text_color=Purple,
                              font=('Poppins', 40, 'normal'),
                              bg_color=White)
    TitleLogin.pack()

    # Container para os campos de entrada
    frame_entries = ctk.CTkFrame(master=Login, fg_color=White, bg_color=White)
    frame_entries.pack(pady=20, expand=True)

    EntryUser = ctk.CTkEntry(master=frame_entries,
                             width=268,
                             height=35,
                             fg_color=White,
                             corner_radius=30,
                             border_color=Purple,
                             placeholder_text="Usuário",
                             font=("Poppins", 15, "normal"),
                             text_color=Purple)
    EntryUser.pack(pady=10)

    EntryPassword = ctk.CTkEntry(master=frame_entries,
                                 width=268,
                                 height=35,
                                 fg_color=White,
                                 corner_radius=30,
                                 border_color=Purple,
                                 placeholder_text="Senha",
                                 font=("Poppins", 15, "normal"),
                                 show="*",
                                 text_color=Purple)
    EntryPassword.pack(pady=10)

    # Container para o botão
    frame_button = ctk.CTkFrame(master=Login, fg_color=White, bg_color=White)
    frame_button.pack(pady=30)

    ButtonLogin = ctk.CTkButton(master=frame_button,
                                text="Fazer Login",
                                fg_color=White,
                                corner_radius=30,
                                border_width=2,
                                border_color=Purple,
                                text_color=Black,
                                font=("Poppins", 15, "normal"),
                                hover_color=Purplehover)
    ButtonLogin.pack()


