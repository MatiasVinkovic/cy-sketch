
import tkinter 
from tkinter import filedialog, messagebox
from tkinter import *
import os
import platform



def open_file():
    "Ouvrir un fichier à partir de l'onglet Fichier dans l'IDE"
    file_path = filedialog.askopenfilename(filetypes= [("Draw++ Files", "*.dpp")])
    print("%d", file_path) #file_path retourne le chemin exact du fichier selectionné

    #une fois que j'ai récup le chemin, j'ai plus qu'a mettre ca dans la text_area
    if file_path: # on check si on a bien un file_path non vide
        with open(file_path, "r") as file:
            text_area.insert(tkinter.END, file.read())
    else:
        text_area.insert(tkinter.END, "erreur lors de la récupération du fichier")

def run():
    #résultat de l'appui du bouton run : sauvegarder dans le dossier to_run
    file_path =  '/home/cytech/Bureau/cy-sketch/to_run/to_execute.dpp'
    os.system("rm /home/cytech/Bureau/cy-sketch/to_run/*.dpp")
    
    print("%d", file_path)
    if file_path: #si le fichier a bien ete enregistrer
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tkinter.END)) #je get absolument tout le contenu de ma text_area
        window.title(f"Éditeur de Code Draw++ - {os.path.basename(file_path)}")
   
    print("Running the code...")


# je creer le fichier to_run pour executer les fichiers .dpp avec le compilateur a venir
#je check le système d'exploitation sur lequel l'appli est
if not os.path.isdir("to_run") and platform.system() == "Linux":
    os.system("mkdir to_run")
    print("no 'to_run' directory, one has just been created")
elif os.path.isdir("to_run") and platform.system() == "Windows":
    os.system("mkdir to_run")
    print("no 'to_run' directory, one has just been created")



#Création de l'envirronement Tkinter
window = tkinter.Tk()
window.title("MyDrawPP IDE")
window.geometry("800x600")

#Gestion du Menu en haut
my_menu = tkinter.Menu(window)
window.config(menu=my_menu)

#Onglet Fichier
file_menu = tkinter.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open_file)


#Bouton run
# run_button = tkinter.Button(my_menu, text="Run", command=run, background="green")
# run_button.pack(side=tkinter.RIGHT)
my_menu.add_command(label="Run",background='green', command=run)

#Zone d'édition de texte
text_area = tkinter.Text(window, wrap="char", undo=True, bg="#353434", fg="white", insertbackground="white", font="Droid", highlightcolor="grey")
text_area.pack(fill=tkinter.BOTH, expand=1)



#lancement de la page 
window.mainloop()
