from tkinter import *
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk
import qrcode

window= Tk()
window.title("QR Code Generator v1.0a")
window.geometry("800x450")
window.configure(bg="#ffdf76")

str='Test!'

def generateQR(event):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(txtAreaStr.get("1.0",END))
    qr.make(fit=True)

    img = qr.make_image(fill_color = "black", back_color="white")
    files=[('Joint Photographic Expers Group (JPG)', '*.jpg'), ('All Files', '*.*'),]

    filename = asksaveasfilename(filetypes=files, defaultextension=files)
    img.save(filename.title)
    img=ImageTk.PhotoImage(image=img)
    lblQRImagePlcaceHolder.configure(image=img)

lblStr= Label(window, text='Type some text here', fg='#2f6694', bg='#ffdf76')
lblStr.place(anchor = NW)

txtAreaStr = Text(width=40, height=15, bg='#2f6694', fg='#ffdf76')
txtAreaStr.insert('end', str)
txtAreaStr.place(x=4, y=20)

btnSend = Button(window,text="Generate QR code", bg='#2f6694', fg='#ffdf76')
btnSend.place(x=4, y=280)
btnSend.bind('<ButtonRelease-1>', generateQR)

lblQRImagePlcaceHolder = Label(window)
lblQRImagePlcaceHolder.place(relx = 1, rely=0.04, x=-4, anchor = NE)

window.mainloop()