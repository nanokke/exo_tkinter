import tkinter as tk   

#fonction nommée fahrenheit_to_celsius()
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get())         
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_result.config(text=f"{celsius:.2f} °C")       
    except ValueError:
        lbl_result.config(text="Entrée invalide")          

#fenêtre Tkinter
window = tk.Tk()

#Définissez le titre de la fenêtre
window.title("Convertisseur de Température")

#taille de fenetre
window.geometry("300x100")

#Définissez la taille de la fenêtre comme fixe
window.resizable(width=False, height=False)

#Affichez du texte pour styler
label_titre = tk.Label(master=window, text="Fahrenheit → Celsius", font=("Arial", 14))
label_titre.grid(row=0, column=0, columnspan=3, pady=10)

#cadre pour contenir le widget d'entrée Fahrenheit et le label
frm_entry = tk.Frame(master=window)
frm_entry.grid(row=1, column=0, padx=10, pady=10)

#entrée pour accepter la température en Fahrenheit.
ent_temperature = tk.Entry(master=frm_entry, width=10)
ent_temperature.grid(row=0, column=0, sticky="e")

#afficher le symbole de degré et le texte "F"
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
#disposer du label
lbl_temp.grid(row=0, column=1, sticky="w")

#bouton pour initier le processus de conversion
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
#disposer du bouton
btn_convert.grid(row=1, column=1, padx=10)

#afficher le résultat de la conversion en Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
#disposer du label de résultat
lbl_result.grid(row=1, column=2, padx=10)

#Appelez la méthode mainloop() 
window.mainloop()
