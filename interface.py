from tkinter import *

interface = Tk()
interface.config(bg="green")
interface.geometry("500x500")
interface.maxsize(500,500)
interface.title("Implementation AES")
texte1=Label(interface,text="Chiffrement AES",font=("arial",20),fg="black",bg="green")
texte1.place(x= 150,y=20)

texte2=Label(interface,text="Selectionnez un Fichier ou un Dossier ",font=("arial",20),fg="black",bg="green")
texte2.place(x= 10,y=100)

select=Button(text="SELECT",font=("arial",20),fg="black",bg="yellow")
select.place(x=200,y=150)

chif=Button(text="Chiffrement",font=("arial",20),fg="black",bg="yellow")
chif.place(x=50,y=300)

dechif=Button(text="Dechiffrement",font=("arial",20),fg="black",bg="yellow")
dechif.place(x=300,y=300)
interface.mainloop()
