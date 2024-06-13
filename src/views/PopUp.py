import customtkinter as ctk

White = '#ffffff'
Black = '#000000'
Purple = '#4200FF'
Purplehover = '#4C22A5'
macos = "#D1CDD1"

def PopUp():
        textinpopUp = "Savo com sucesso"
        savetela = ctk.CTk()
        savetela.geometry("400x199")
        savetela.config(bg=White)
        savetela.resizable(False,False)
        savetela.title("Transação Salva") 


        textSave = ctk.CTkLabel(
                                    master=savetela,
                                    width=156,
                                    height=21,
                                    fg_color=White,
                                    bg_color=White,
                                    text=textinpopUp,
                                    text_color=Purple,
                                    font=("poppins",21,"normal")
                                           )
        textSave.place(x=115,y=52)

        buttonOk = ctk.CTkButton(
                                    master=savetela,
                                    width=109,
                                    height=24,
                                    fg_color=White,
                                    bg_color=White,
                                    text="Ok",
                                    text_color=Black,
                                    corner_radius=30,
                                    border_color=Purple,
                                    border_width=1,
                                    hover_color=Purplehover
                                            )
        buttonOk.place(x=145,y=120)


        savetela.mainloop() 

