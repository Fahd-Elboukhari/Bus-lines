import customtkinter as ctk
from tkinter import messagebox
import json
import datetime
import os
from lignes import bus_lines

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Espace Conducteur")
root.geometry("500x500")

# Variables globales pour accès dans toutes les fonctions
ligne_combo = None
type_combo = None
description_entry = None

# Fonction de vérification
def verifier_identifiants(nom, mot_de_passe):
    try:
        with open("conducteurs.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        for conducteur in data:
            if conducteur["nom"].strip().lower() == nom.strip().lower() and conducteur["mot_de_passe"] == mot_de_passe:
                return True
    except:
        pass
    return False

# Fonction pour envoyer un signalement
def envoyer_signalement():
    global ligne_combo, type_combo, description_entry
    ligne = ligne_combo.get()
    type_signalement = type_combo.get()
    description = description_entry.get().strip()

    if not ligne or not type_signalement:
        messagebox.showerror("Erreur", "Veuillez sélectionner une ligne et un type.")
        return

    signalement = {
        "ligne": ligne,
        "type": type_signalement,
        "description": description,
        "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    if os.path.exists("signalements.json"):
        with open("signalements.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(signalement)

    with open("signalements.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("Succès", "Signalement envoyé avec succès.")
    description_entry.delete(0, "end")
    ligne_combo.set("")
    type_combo.set("")

# Afficher interface conducteur après connexion réussie
def lancer_interface():
    global ligne_combo, type_combo, description_entry

    login_frame.destroy()

    form = ctk.CTkFrame(root)
    form.pack(pady=40)

    ctk.CTkLabel(form, text="🚍 Numéro de ligne :").pack(pady=5)
    ligne_combo = ctk.CTkComboBox(form, values=[l[0] for l in bus_lines], width=200)
    ligne_combo.pack(pady=5)

    ctk.CTkLabel(form, text="📝 Type de signalement :").pack(pady=5)
    type_combo = ctk.CTkComboBox(form, values=["Retard", "Panne", "Embouteillage"], width=200)
    type_combo.pack(pady=5)

    ctk.CTkLabel(form, text="Description (facultative) :").pack(pady=5)
    description_entry = ctk.CTkEntry(form, placeholder_text="Détails", width=300)
    description_entry.pack(pady=5)

    ctk.CTkButton(form, text="📤 Envoyer", command=envoyer_signalement).pack(pady=15)

# Interface de connexion
login_frame = ctk.CTkFrame(root)
login_frame.pack(pady=100)

ctk.CTkLabel(login_frame, text="Connexion Conducteur", font=("Arial", 18, "bold")).pack(pady=10)
nom_entry = ctk.CTkEntry(login_frame, placeholder_text="Nom")
nom_entry.pack(pady=5)
mdp_entry = ctk.CTkEntry(login_frame, placeholder_text="Mot de passe", show="*")
mdp_entry.pack(pady=5)
status_label = ctk.CTkLabel(login_frame, text="")
status_label.pack()

def tenter_connexion():
    nom = nom_entry.get().strip()
    mdp = mdp_entry.get().strip()
    if verifier_identifiants(nom, mdp):
        lancer_interface()
    else:
        status_label.configure(text="❌ Nom ou mot de passe incorrect", text_color="red")

ctk.CTkButton(login_frame, text="Se connecter", command=tenter_connexion).pack(pady=10)

root.mainloop()
