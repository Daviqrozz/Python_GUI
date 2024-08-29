import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("green") 

appWidth, appHeight = 500, 500

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GUI Application")

        # Centralizando a janela na tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = int(screen_width/2 - appWidth/2)
        position_y = int(screen_height/2 - appHeight/2)
        self.geometry(f"{appWidth}x{appHeight}+{position_x}+{position_y}")

        # Configuração da Grid
        self.grid_columnconfigure(0, weight=1)  # Coluna vazia para espaçamento
        self.grid_columnconfigure(1, weight=0)  # Coluna para Label
        self.grid_columnconfigure(2, weight=0)  # Coluna para Entry
        self.grid_columnconfigure(3, weight=1)  # Coluna vazia para espaçamento

        self.grid_rowconfigure(4, weight=1)  # Expansão na direção vertical para a linha com Text Box

        # Name Label
        self.nameLabel = ctk.CTkLabel(self, text="Name")
        self.nameLabel.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Teja", width=200)  # Definindo largura
        self.nameEntry.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        # Fone Label
        self.ageLabel = ctk.CTkLabel(self, text="Telefone")
        self.ageLabel.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Fone Entry Field
        self.ageEntry = ctk.CTkEntry(self, placeholder_text="18", width=125)  # Definindo largura
        self.ageEntry.grid(row=1, column=2, padx=20, pady=20, sticky="w")

        # Save Button
        self.SaveButton = ctk.CTkButton(self, width=50, text='Salvar')
        self.SaveButton.grid(row=2, column=1, columnspan=2, padx=20, pady=20, sticky="w")  
        # Delete Button
        self.SaveButton = ctk.CTkButton(self, width=50, text='Apagar contatos',fg_color='red',hover_color='#8A0303')
        self.SaveButton.grid(row=2, column=2, columnspan=2, padx=20, pady=20, sticky="w")  
        # Export Button
        self.SaveButton = ctk.CTkButton(self, width=50, text='Exportar(CSV)')
        self.SaveButton.grid(row=5, column=2, columnspan=3, padx=20, pady=20, sticky="w")  # Colocado abaixo dos campos
        
        # Label para "Lista de Contatos"
        self.contactsLabel = ctk.CTkLabel(self, text="Lista de Contatos:")
        self.contactsLabel.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=250, height=50)  # Definindo largura
        self.displayBox.grid(row=4, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        # Expansão na direção horizontal e vertical para a caixa de texto
        self.grid_rowconfigure(4, weight=1)

    # def createText(self):
    #    return f"{Nome}:{telefone}"

if __name__ == "__main__":
    app = App()
    app.mainloop()
