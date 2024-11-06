# Aluna: Milena Rickli Silvério
# Eng. de Software, 5° Período - Tópicos Avançados I
# Sistema especialista para escolha de filmes


import tkinter as tk
from tkinter import messagebox


class SistemaRecomendacaoFilmes:
    def __init__(self):
        # Base de conhecimento: regras de recomendação de filmes
        self.regras = [
            {"preferencias": {"genero": "ação", "ano": "recente"}, "filme": "Vingadores: Ultimato"},
            {"preferencias": {"genero": "comédia", "ano": "recente"}, "filme": "Jojo Rabbit"},
            {"preferencias": {"genero": "drama", "ano": "clássico"}, "filme": "Cidadão Kane"},
            {"preferencias": {"genero": "terror", "ano": "recente"}, "filme": "Um Lugar Silencioso"},
            {"preferencias": {"genero": "ficção científica", "ano": "recente"}, "filme": "Blade Runner 2049"},
            {"preferencias": {"genero": "romance", "ano": "clássico"}, "filme": "E o Vento Levou"},
            {"preferencias": {"genero": "ação", "ano": "clássico"}, "filme": "Os Sete Samurais"},
            {"preferencias": {"genero": "comédia", "ano": "clássico"}, "filme": "Os Caça-Fantasmas"},
            {"preferencias": {"genero": "drama", "ano": "recente"}, "filme": "História de um Casamento"},
            {"preferencias": {"genero": "terror", "ano": "clássico"}, "filme": "Psicose"},
            {"preferencias": {"genero": "ficção científica", "ano": "clássico"}, "filme": "A Laranja Mecânica"},
            {"preferencias": {"genero": "romance", "ano": "recente"}, "filme": "A Forma da Água"},
            {"preferencias": {"genero": "aventura", "ano": "recente"}, "filme": "Aquaman"},
            {"preferencias": {"genero": "animação", "ano": "clássico"}, "filme": "Wall-e"},
            {"preferencias": {"genero": "animação", "ano": "recente"}, "filme": "Viva - A Vida é uma Festa"},
            {"preferencias": {"genero": "fantasia", "ano": "recente"}, "filme": "Animais Fantásticos: Os Segredos de Dumbledore"},
            {"preferencias": {"genero": "fantasia", "ano": "clássico"}, "filme": "A Fantástica Fábrica de Chocolate"},
            {"preferencias": {"genero": "aventura", "ano": "clássico"}, "filme": "Indiana Jones e a Última Cruzada"},
        ]

    def recomendar(self, preferencias_usuario):
        # Verifica cada regra na base de conhecimento
        for regra in self.regras:
            # Verifica se as preferências do usuário correspondem à regra
            if all(preferencias_usuario.get(chave) == valor for chave, valor in regra["preferencias"].items()):
                return regra["filme"]
        return "Desculpe, não encontramos recomendações com base nas suas preferências."


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Recomendação de Filmes")
        tk.Label(master, text="Bem-vindo ao sistema de recomendação de filmes!", font=("Arial", 14)).pack(pady=10)
        self.sistema = SistemaRecomendacaoFilmes()
        
        # Gêneros
        self.genero_var = tk.StringVar(value="ação")
        self.ano_var = tk.StringVar(value="recente")

        tk.Label(master, text="Escolha um gênero:").pack()
        for genero in ["ação", "comédia", "drama", "terror", "ficção científica", "romance", "aventura", "animação", "fantasia"]:
            tk.Radiobutton(master, text=genero.capitalize(), variable=self.genero_var, value=genero).pack(anchor=tk.W)

        tk.Label(master, text="Escolha o tipo de filme:").pack()
        tk.Radiobutton(master, text="Recente", variable=self.ano_var, value="recente").pack(anchor=tk.W)
        tk.Radiobutton(master, text="Clássico", variable=self.ano_var, value="clássico").pack(anchor=tk.W)

        tk.Button(master, text="Recomendar Filme", command=self.recomendar_filme).pack(pady=10)

    def recomendar_filme(self):
        preferencias_usuario = {
            "genero": self.genero_var.get(),
            "ano": self.ano_var.get(),
        }
        recomendacao = self.sistema.recomendar(preferencias_usuario)
        messagebox.showinfo("Recomendação de Filme", recomendacao)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()