import customtkinter as ctk
from tkinter.messagebox import askyesno, showinfo
from tkinter import BOTH, BOTTOM
import string
import random
import tkinter as tk

# Création de la fenêtre principale
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
fenetre = ctk.CTk()
fenetre.title("PassWord Generator")
fenetre.geometry("570x400")
fenetre.resizable(height= False, width= False)

#Creation des sous frames
frame1 = ctk.CTkFrame(master=fenetre, width=500, height=35)
frame1.place(y=15, x=50)

frame2 = ctk.CTkFrame(master=fenetre, width=620, height=70)
frame2.place(y=332, x=0)

# Configuration des variables pour les checkbox
checkbox_var_Lettres = tk.BooleanVar()
checkbox_var_Lettres.set(True)
checkbox_var_Chiffre = tk.BooleanVar()
checkbox_var_Chiffre.set(False)
checkbox_var_Ponctuations = tk.BooleanVar()
checkbox_var_Ponctuations.set(False)

# Fonction pour générer le mot de passe
def generer_mot_de_passe():
    # Récupération de la longueur du mot de passe
    try:
        longueur_mot_de_passe = int(entry_longueur_mot_de_passe.get())
    except ValueError:
        showinfo('ERREUR',"Veuillez entrer un nombre entier pour la longueur du mot de passe.")
        return
    
    # Vérification des checkbox cochées
    caracteres_possibles = ""
    if checkbox_var_Lettres.get():
        caracteres_possibles += string.ascii_letters
    if checkbox_var_Chiffre.get():
        caracteres_possibles += string.digits
    if checkbox_var_Ponctuations.get():
        caracteres_possibles += string.punctuation
    
    # Génération du mot de passe
    if len(caracteres_possibles) == 0:
        showinfo('NOTIFICATION',"Veuillez sélectionner au moins une option.")
        return
    
    # Gestion de la longueur du mot de passe
    elif longueur_mot_de_passe > 30 :
        showinfo('NOTIFICATION',"La longueur maximale d'un mot de passe est de 30 caractères")
        
    else:
        mot_de_passe = "".join(random.choice(caracteres_possibles) for _ in range(longueur_mot_de_passe))
    
    # Affichage du résultat
        label_resultat.configure(frame1,text=mot_de_passe)
    
    # Impression dans un fichier externe si l'option est cochée
    if checkbox_imprimer.get():
        try:
            with open("mot_de_passe.txt", "w") as f:
                f.write(mot_de_passe)
        except IOError:
            showinfo('Erreur', "impossible d'écrire dans le fichier mot_de_passe.txt.")

#Fonction pour fermer la fenetre
def confirmation():
    close = askyesno(title="Quitter", message="Voulez-vous vraiment Quitter ?")
    if close:
        fenetre.destroy()
fenetre.protocol("WM_DELETE_WINDOW", confirmation)

# Fonction pour créer un fichier externe
def creer_fichier():
    try:
        with open("mot_de_passe.txt", "x"):
            showinfo('NOTIFICATION',"Le fichier mot_de_passe.txt a été créé.")
    except FileExistsError:
        showinfo('NOTIFICATION',"Le fichier mot_de_passe.txt existe déjà.")
    except IOError:
        showinfo('NOTIFICATION',"impossible de créer le fichier mot_de_passe.txt.")

# Création des widgets
label_longueur_mot_de_passe = ctk.CTkLabel(fenetre, text="Longueur du mot de passe :")
entry_longueur_mot_de_passe = ctk.CTkEntry(fenetre)
checkbox_Lettres = ctk.CTkCheckBox(fenetre, text="Avec les Lettres", variable=checkbox_var_Lettres)
checkbox_Chiffre = ctk.CTkCheckBox(fenetre, text="Avec les Chiffres", variable=checkbox_var_Chiffre)
checkbox_Ponctuations = ctk.CTkCheckBox(fenetre, text="Avec les Symboles", variable=checkbox_var_Ponctuations)
checkbox_imprimer = ctk.CTkCheckBox(fenetre, text="Imprimer le mot de passe dans un fichier externe")
bouton_generer_mot_de_passe = ctk.CTkButton(fenetre, text="Générer le mot de passe", command=generer_mot_de_passe)
bouton_creer_fichier = ctk.CTkButton(fenetre, text="Créer un fichier externe", command=creer_fichier)
label_resultat = ctk.CTkLabel(frame1, text="")

#Les fonctions cancel et finish
button1 = ctk.CTkButton(master=frame2, text="Annuler", command=fenetre.destroy)
button1.place(y=15, x=20)

button2 = ctk.CTkButton(master=frame2, text="Terminer", command=fenetre.destroy)
button2.place(y=15, x=410)

# Placement des widgets dans la fenêtre
label_longueur_mot_de_passe.place(x=10, y=100)
entry_longueur_mot_de_passe.place(x=10, y=150)
checkbox_Lettres.place(x=350, y=100)
checkbox_Chiffre.place(x=350, y=150)
checkbox_Ponctuations.place(x=350, y=200)
checkbox_imprimer.place(x=10, y=300)
bouton_generer_mot_de_passe.place(x=10, y=200)
bouton_creer_fichier.place(x=400, y=300)
label_resultat.place(x=50, y=4)

# Lancement de la boucle principale
fenetre.mainloop()
