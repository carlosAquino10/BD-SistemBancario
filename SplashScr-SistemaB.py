import tkinter as tk
from PIL import Image, ImageTk

def splash_screen():
    root = tk.Tk()
    root.title("Sistema Bancário")
    root.geometry("900x400")

    # Criar um canvas
    canvas = tk.Canvas(root, width=900, height=453)
    canvas.pack()

    # Carregar a imagem
    image = Image.open(".\\imagem\\openbanking.jpg")
    photo = ImageTk.PhotoImage(image)

    # Exibir a imagem no canvas
    canvas.create_image(476, 226, anchor=tk.CENTER, image=photo)

    # Informações dos desenvolvedores
    desenvolvido_por = [
        "Bem-vindo ao Sistema Bancário",
        "Desenvolvido por:",
        "Carlos de Aquino Itaboray",
        "Fabrício Dias de Oliveira",
        "Maciel Costa do Nascimento",
    ]

    # Adicionar as informações como texto no canvas
    y_pos = 100
    for info in desenvolvido_por:
        canvas.create_text(30, y_pos, text=info, font=("Helvetica", 18, "bold"), fill="white", anchor=tk.W)
        y_pos += 30
        y_pos += 10  # Adicionando um espaçamento de 10 pixels entre cada linha
        
    

    root.mainloop()

splash_screen()
