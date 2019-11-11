import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 2
__filename__ = "BaseConverter"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)
__picpath__ = __savepath__ + "/{}.png".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:
            urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
            urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.png".format(__filename__), __picpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import *
from PIL import Image, ImageTk

combobox_list = ("<Base>", "Binaire", "Octal", "Decimal", "Hexadeci", "BCD")
finalbase_1 = "nothing"
finalbase_2 = "nothing"

def set_result(result):
    Text2.delete("1.0", END)
    Text2.insert(END, result)

def selectbase_1(event):
    global finalbase_1
    combobox_var_base_1 = combobox_var_1.get()
    if combobox_list[0] in combobox_var_base_1:
        showwarning(__filename__, "Merci de préciser un format d'encodage correct dans la liste 1.")
    else:
        finalbase_1 = combobox_var_base_1

def selectbase_2(event):
    global finalbase_2
    combobox_var_base_2 = combobox_var_2.get()
    if combobox_list[0] in combobox_var_base_2:
        showwarning(__filename__, "Merci de préciser un format d'encodage correct dans la liste 2.")
    else:
        finalbase_2 = combobox_var_base_2

def convert():
    global finalbase_1, finalbase_2
    if "nothing" in finalbase_1:
        showwarning(__filename__, "Aucun format d'encodage n'est séléctionné dans la liste 1.")
    elif "nothing" in finalbase_2:
        showwarning(__filename__, "Aucun format d'encodage n'est séléctionné dans la liste 2.")
    else:
        try:
            # If twice base are same #
            if finalbase_1 == finalbase_2:
                text_convert = Text1.get("1.0", END)
                set_result(text_convert)
            # Convert from binary #
            elif finalbase_1 == "Binaire" and finalbase_2 == "Octal":
                text_convert = oct(int(Text1.get("1.0", END), 2))
                set_result(text_convert.replace("0o", ""))
            elif finalbase_1 == "Binaire" and finalbase_2 == "Decimal":
                text_convert = int(int(Text1.get("1.0", END), 2))
                set_result(text_convert)
            elif finalbase_1 == "Binaire" and finalbase_2 == "Hexadeci":
                text_convert = hex(int(Text1.get("1.0", END), 2))
                set_result(text_convert.replace("0x", "").upper())
            elif finalbase_1 == "Binaire" and finalbase_2 == "BCD":
                text_convert = "".join(format(int(x), "04b") for x in str(int(Text1.get("1.0", END), 2)))
                set_result(text_convert)
            # Convert from octal #
            elif finalbase_1 == "Octal" and finalbase_2 == "Binaire":
                text_convert = bin(int(Text1.get("1.0", END), 8))
                set_result(text_convert.replace("0b", ""))
            elif finalbase_1 == "Octal" and finalbase_2 == "Decimal":
                text_convert = int(int(Text1.get("1.0", END), 8))
                set_result(text_convert)
            elif finalbase_1 == "Octal" and finalbase_2 == "Hexadeci":
                text_convert = hex(int(Text1.get("1.0", END), 8))
                set_result(text_convert.replace("0x", "").upper())
            elif finalbase_1 == "Octal" and finalbase_2 == "BCD":
                text_convert = "".join(format(int(x), "04b") for x in str(int(Text1.get("1.0", END), 8)))
                set_result(text_convert)
            # Convert from decimal #
            elif finalbase_1 == "Decimal" and finalbase_2 == "Binaire":
                text_convert = bin(int(Text1.get("1.0", END), 10))
                set_result(text_convert.replace("0b", ""))
            elif finalbase_1 == "Decimal" and finalbase_2 == "Octal":
                text_convert = oct(int(Text1.get("1.0", END), 10))
                set_result(text_convert.replace("0o", ""))
            elif finalbase_1 == "Decimal" and finalbase_2 == "Hexadeci":
                text_convert = hex(int(Text1.get("1.0", END), 10))
                set_result(text_convert.replace("0x", "").upper())
            elif finalbase_1 == "Decimal" and finalbase_2 == "BCD":
                text_convert = "".join(format(int(x), "04b") for x in str(int(Text1.get("1.0", END), 10)))
                set_result(text_convert)
            # Convert from hexadecimal #
            elif finalbase_1 == "Hexadeci" and finalbase_2 == "Binaire":
                text_convert = bin(int(Text1.get("1.0", END), 16))
                set_result(text_convert.replace("0b", ""))
            elif finalbase_1 == "Hexadeci" and finalbase_2 == "Octal":
                text_convert = oct(int(Text1.get("1.0", END), 16))
                set_result(text_convert.replace("0o", ""))
            elif finalbase_1 == "Hexadeci" and finalbase_2 == "Decimal":
                text_convert = int(int(Text1.get("1.0", END), 16))
                set_result(text_convert)
            elif finalbase_1 == "Hexadeci" and finalbase_2 == "BCD":
                text_convert = "".join(format(int(x), "04b") for x in str(int(Text1.get("1.0", END), 16)))
                set_result(text_convert)
            # Convert from BCD #
            elif finalbase_1 == "BCD":
                bcd_number = ""
                def split(num):
                    while num:
                        yield num[:4]
                        num = num[4:]
                for spaced_binary in list(split(Text1.get("1.0", END).replace("\n", ""))):
                    bcd_number += str(int(spaced_binary, 2))

                if finalbase_2 == "Binaire":
                    text_convert = bin(int(bcd_number, 10))
                    set_result(text_convert.replace("0b", ""))
                elif finalbase_2 == "Octal":
                    text_convert = oct(int(bcd_number, 10))
                    set_result(text_convert.replace("0o", ""))
                elif finalbase_2 == "Decimal":
                    set_result(int(bcd_number))
                elif finalbase_2 == "Hexadeci":
                    text_convert = hex(int(bcd_number, 10))
                    set_result(text_convert.replace("0x", ""))
        except:
            showwarning(__filename__, "Une erreur est survenue lors du convertissage, merci de vérifier si vous n'avez pas fait d'erreur.")

baseconverter = Tk()
width = 1080
height = 600
baseconverter.update_idletasks()
x = (baseconverter.winfo_screenwidth() - width) // 2
y = (baseconverter.winfo_screenheight() - height) // 2
baseconverter.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
baseconverter.resizable(width=False, height=False)
baseconverter.title(__filename__)
baseconverter.configure(background="lightgray")

if os.path.exists(__iconpath__):
    baseconverter.iconbitmap(__iconpath__)

if os.path.exists(__picpath__):
    BG = Image.open(__picpath__)
    img = ImageTk.PhotoImage(BG)
    BGL = Label(baseconverter, image=img)
    BGL.place(relx=0, rely=0, relheight=1, relwidth=1)

font1 = "-family {Rockwell Extra Bold} -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
font2 = "-family {Rockwell Extra Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0"

combobox_var_1 = StringVar()
combobox_var_1.set(combobox_list[0])

Combobox1 = Combobox(baseconverter, textvariable=combobox_var_1, values=combobox_list, state="readonly", background="white")
Combobox1.place(relx=0.25, rely=0.58, relheight=0.05, relwidth=0.12)
Combobox1.configure(width=130)
Combobox1.configure(takefocus="")
Combobox1.configure(font=font1)
Combobox1.bind("<<ComboboxSelected>>", selectbase_1)

combobox_var_2 = StringVar()
combobox_var_2.set(combobox_list[0])

Combobox2 = Combobox(baseconverter, textvariable=combobox_var_2)
Combobox2.place(relx=0.74, rely=0.58, relheight=0.05, relwidth=0.12)
Combobox2.configure(values=combobox_list)
Combobox2.configure(state="readonly")
Combobox2.configure(background="white")
Combobox2.configure(width=130)
Combobox2.configure(takefocus="")
Combobox2.configure(font=font1)
Combobox2.bind("<<ComboboxSelected>>", selectbase_2)

if not os.path.exists(__picpath__):
    Label1 = Label(baseconverter)
    Label1.place(relx=0.14, rely=0.58, height=30, width=100)
    Label1.configure(activebackground="lightgray")
    Label1.configure(activeforeground="black")
    Label1.configure(background="lightgray")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font=font2)
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="black")
    Label1.configure(text="Base :")

    Label2 = Label(baseconverter)
    Label2.place(relx=0.64, rely=0.58, height=31, width=86)
    Label2.configure(activebackground="lightgray")
    Label2.configure(activeforeground="black")
    Label2.configure(background="lightgray")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font=font2)
    Label2.configure(foreground="#000000")
    Label2.configure(highlightbackground="#d9d9d9")
    Label2.configure(highlightcolor="black")
    Label2.configure(text="Base :")

Button1 = Button(baseconverter)
Button1.place(relx=0.43, rely=0.75, height=50, width=150)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(command=convert)
Button1.configure(font=font2)
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text="Convertir")

Text1 = Text(baseconverter)
Text1.place(relx=0.07, rely=0.15, relheight=0.3, relwidth=0.35)
Text1.configure(background="white")
Text1.configure(font=font1)
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(undo="1")
Text1.configure(width=380)
Text1.configure(wrap=WORD)

Text2 = Text(baseconverter)
Text2.place(relx=0.57, rely=0.15, relheight=0.3, relwidth=0.35)
Text2.configure(background="white")
Text2.configure(font=font1)
Text2.configure(foreground="black")
Text2.configure(highlightbackground="#d9d9d9")
Text2.configure(highlightcolor="black")
Text2.configure(insertbackground="black")
Text2.configure(selectbackground="#c4c4c4")
Text2.configure(selectforeground="black")
Text2.configure(undo="1")
Text2.configure(width=380)
Text2.configure(wrap=WORD)

baseconverter.mainloop()
