from tkinter import *
import pywhatkit as kit
from datetime import datetime, timedelta

def btn_clicked():
    numero = entry0.get()
    if not numero.startswith('+'):
        numero = '+55' + numero
    mensagem = entry1.get("1.0", "end-1c")

    # Obter o horário atual e adicionar 2 minutos
    agora = datetime.now() + timedelta(minutes=1)
    hora = agora.hour
    minuto = agora.minute

    kit.sendwhatmsg(numero, mensagem, hora, minuto)
    print(f"Mensagem enviada para {numero} às {hora}:{minuto} com a mensagem: {mensagem}")


window = Tk()

window.geometry("640x480")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 480,
    width = 640,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    303.0, 186.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 113.0, y = 173,
    width = 380.0,
    height = 24)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    303.0, 312.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 116.0, y = 239,
    width = 374.0,
    height = 145)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 413, y = 404,
    width = 100,
    height = 33)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    320.0, 240.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
