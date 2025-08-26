import tkinter as tk
from tkinter import messagebox

def verificar_nota ():
    nota_texto = entry_nota.get()

    if nota_texto.replace(".", "", 1).isdigit():
        nota = float(nota_texto)

        if nota >= 7:
            resultado = "Aprovado!"
        elif nota >= 5:
            resultado = "Reprovado!"
        else:
            resultado = "Reprovado!"

        messagebox.showinfo("Resultado", f"Situação: {resultado}")
    else:
        messagebox.showerror("Erro", "Digite um número válido.")

# janela principal
root = tk.Tk()
root.title("Verificador de Nota")
root.geometry("300x200")
root.configure(bg="#F0E68C")
 
# Widgets
tk.Label(root, text="Digite a nota do aluno:", bg="#F0E68C", fg="black", font=("arial", 11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)
 
tk.Button(root, text="Verificar", command=verificar_nota, bg="blue", fg="white", font=("arial", 11, "bold")).pack(pady=10)

root.mainloop()
