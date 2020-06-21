import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Rechercher un mot dans n'importe quel fichier") 

WORD = None 
RESULT = "Résultat trouvé à la ligne: "

def upload_file():
    global WORD
    try:
        myfile = filedialog.askopenfilename(
            title = "Chercheur de mot",
            filetypes = (
                ("txt files","*.txt"),
                ("all files","*.*")
            )
        )
        WORD = list(open(myfile, "r"))
        search_button["state"] = "normal"
        search_variable.set("chercher un mot dans votre document")
    except:
        WORD = None
        search_variable.set("aucun fichier sélectionner")


def search():
    global FOUND
    FOUND_WORD= ""
    wanted_word = input_word.get()
    for word in WORD:
        searching_word = word.strip("\n")
        if sensitive_var.get() == 1:
            if searching_word == wanted_word:
                FOUND_WORD += "{}, ".format(WORD.index(word) + 1)
        else:
            if searching_word.lower() == wanted_word.lower():
                FOUND_WORD += "{}, ".format(WORD.index(word) + 1)
        if FOUND_WORD != "":
            search_variable.set(RESULT+FOUND_WORD)
        else:
            search_variable.set("mot introuvable")

main_frame  = tk.Frame(root, relief="groove")
result_frame  = tk.Frame(root, relief="groove")
search_variable = tk.StringVar()
search_variable.set("Cliquez sur choisir un fichier pour sélectionner un fichier")
main_frame.pack(padx=20, pady=20)
result_frame.pack(padx=10, pady=10)
upload_form =  tk.Button(main_frame,
                text ="Choisir un fichier",
                justify="center",
                command=upload_file,
            )
upload_form.grid(row=0, column=0, padx=10)
search_label = tk.Label(main_frame, justify="center", text="Chercher le mot:")
search_label.grid(row=2, column=0)
input_word = tk.Entry(main_frame, justify="center", bd= 5, width=100)
input_word.grid(row=3, column=0)
search_button = tk.Button(main_frame,text ="Trouver",command=search,font= 10)
search_button.grid(row=4, column=0, padx=20)

search_result = tk.Label(result_frame, justify="center", textvariable=search_variable)
search_result.pack()

root.mainloop()