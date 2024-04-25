import tkinter as tk 

def retrieve_input():
    input_text = text_area.get("1.0", "end-1c")
    print(input_text)

root = tk.Tk()
root.title("Zone de texte")

text_area = tk.Text(root, height=10, width=50)
text_area.pack(padx = 10, pady=10)

submit_button = tk.Button(root, text="Soumettre", command=retrieve_input)
submit_button.pack(ipadx=10, ipady=5, pady=10)

root.mainloop()