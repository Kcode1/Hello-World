from tkinter import *
from tkinter import ttk
from googletrans import Translator

root = Tk()
root.geometry("800x550+250+100")
root.title("Real Traductor")
root.resizable(0,0)
root.iconbitmap('C:/Users/root/Desktop/prog/registre.ico')
root.configure(bg="lightblue")
#====================================== declaration des variable globale =======================================
source = ""
destination = ""
t = ""

def Traduction(event):
    global source
    global destination
    source = langBox1.get()
    destination = langBox2.get()

def Traduct():
    trans = Translator()
    global t
    t = T1.get("1.0",END)
    translated = trans.translate(t, src = source, dest = destination)
    traduct = translated.text
    T2.delete('1.0',END)
    T2.insert(END, traduct)
            
lbl_lang_source = Label(root, text = 'Choisir langue source', font=('Times', 15),bg="lightblue")
lbl_lang_source.place(x=20,y=30)
langues = ['French','English','Spanish','German','ht','Japanese','']
langBox1 = ttk.Combobox(root, width = 25, values = langues)
langBox1.current(0)
langBox1.place(x=200,y=30)
langBox1.bind("<<ComboboxSelected>>", Traduction)

T1 = Text(root, font=("Times", 13)) 
T1.place(x=20,y=100, width = 360, height = 400)

vsb = ttk.Scrollbar(root , orient="vertical",command=T1.yview)
vsb.place(x=380, y=100, height=400, width =15)
T1.configure(yscrollcommand=vsb.set)
        
lbl_lang_destination = Label(root, text = 'Choisir langue destination', font=('Times', 15),bg="lightblue")
lbl_lang_destination.place(x=390,y=30)

langBox2 = ttk.Combobox(root, width = 25, values = langues)
langBox2.place(x=610,y=30)
langBox2.bind("<<ComboboxSelected>>", Traduction)

lbl_NB = Label(root, text='Veiller selectionner votre langue de destination', font='Arial, 12', fg='crimson',bg="lightblue")
lbl_NB.place(x=250,y=70)

T2 = Text(root, font=("Times", 13))
T2.place(x=410,y=100, width = 360, height = 400)

vsb = ttk.Scrollbar(root , orient="vertical",command=T2.yview)
vsb.place(x=770, y=100, height=400, width =15)
T2.configure(yscrollcommand=vsb.set)

btn_traduction = Button(root, text = 'Traduire', font=('Times', 12, 'bold'), command = Traduct)
btn_traduction.place(x=360,y=505)

root.mainloop()