import tkinter as tk
from tkinter import ttk
from lignes import bus_stops, bus_lines

# Fonction pour filtrer les lignes selon la recherche
def filter_lines(event=None):
    search_term = search_entry.get().strip().lower()
    clear_canvas()
    if not search_term:  # Si la recherche est vide, afficher toutes les lignes
        display_lines(bus_lines)
    else:
        filtered_lines = [
            line for line in bus_lines if search_term in line[0].lower() or search_term in line[1].lower()
        ]
        if filtered_lines:
            display_lines(filtered_lines)
        else:
            # Afficher un message si aucune correspondance
            message_label = tk.Label(canvas_frame, text="Rien ne correspond à votre recherche",
                                      bg="#ffffff", fg="red", font=("Arial", 12, "bold"))
            message_label.pack(pady=10)

# Fonction pour effacer le contenu du canvas
def clear_canvas():
    for widget in canvas_frame.winfo_children():
        widget.destroy()

# Fonction pour afficher les lignes
def display_lines(lines):
    clear_canvas()
    for line in lines:
        line_frame = tk.Frame(canvas_frame, bg="#e0f7fa", bd=1, relief="solid")
        line_frame.pack(fill="x", pady=5, padx=10)

        # Label pour le numéro de la ligne
        line_number_label = tk.Label(line_frame, text=line[0], bg="#00796b", fg="white",
                                     font=("Arial", 12, "bold"), width=8)
        line_number_label.pack(side="left", padx=5, pady=5)

        # Label pour la description de la ligne
        line_desc_label = tk.Label(line_frame, text=line[1], bg="#e0f7fa", fg="#004d40",
                                   font=("Arial", 10), anchor="w", justify="left")
        line_desc_label.pack(side="left", fill="x", padx=5, pady=5, expand=True)

        # Label pour le tarif de la ligne
        line_price_label = tk.Label(line_frame, text=f"Tarif: {line[2]}", bg="#e0f7fa", fg="#388e3c",
                                    font=("Arial", 10, "bold"))
        line_price_label.pack(side="right", padx=5, pady=5)

        # Ajouter un bouton pour afficher les arrêts
        stops_button = tk.Button(line_frame, text=">", bg="#00796b", fg="white",
                                  font=("Arial", 10, "bold"), command=lambda l=line: show_stops(l[0]))
        stops_button.pack(side="right", padx=5, pady=5)

# Fonction pour afficher les arrêts d'une ligne
def show_stops(line_number):
    clear_canvas()
    stops_list = bus_stops.get(line_number, [])

    if stops_list:
        tk.Label(canvas_frame, text=f"Arrêts pour la ligne {line_number} :", bg="#ffffff",
                 fg="#00796b", font=("Arial", 14, "bold")).pack(pady=10)
        for stop in stops_list:
            stop_label = tk.Label(canvas_frame, text=stop, bg="#e0f7fa", fg="#004d40",
                                  font=("Arial", 12), anchor="w", justify="left")
            stop_label.pack(fill="x", pady=5, padx=10)
    else:
        tk.Label(canvas_frame, text="Aucun arrêt trouvé pour cette ligne", bg="#ffffff",
                 fg="red", font=("Arial", 12, "bold")).pack(pady=10)

    back_button = tk.Button(canvas_frame, text="Retour", bg="#00796b", fg="white",
                            font=("Arial", 10, "bold"), command=go_back_to_main)
    back_button.pack(pady=10)

# Fonction pour revenir au menu principal
def go_back_to_main():
    clear_canvas()
    display_lines(bus_lines)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Recherche de lignes de bus")
root.geometry("600x600")
root.configure(bg="#e0f7fa")

# Barre de recherche
search_frame = tk.Frame(root, bg="#e0f7fa")
search_frame.pack(fill="x", padx=10, pady=10)

search_label = tk.Label(search_frame, text="Recherche:", bg="#e0f7fa", fg="#00796b", font=("Arial", 12, "bold"))
search_label.pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=40)
search_entry.pack(side="left", padx=5)
search_entry.bind("<KeyRelease>", filter_lines)

search_icon = tk.Label(search_frame, text="🔍", bg="#e0f7fa", font=("Arial", 14))
search_icon.pack(side="left", padx=5)

# Zone principale pour afficher les résultats
main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Canvas pour les lignes
canvas = tk.Canvas(main_frame, bg="#ffffff")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas_frame = tk.Frame(canvas, bg="#ffffff")
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Afficher toutes les lignes au lancement
display_lines(bus_lines)

# Lancement de l'application
root.mainloop()
