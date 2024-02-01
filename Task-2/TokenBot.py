# Modules ================================================================================================================================================

from tkinter import *
import tkinter as tk
import spacy
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Main ===================================================================================================================================================

root = tk.Tk()
root.title('AskBot')
root.resizable(False,False)
root.geometry('600x600')
root.config(bg='#000000')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600 
window_height = 650
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
root.geometry("+{}+{}".format(x, y))

# Text Entryy ============================================================================================================================================

displaychat = Text(root, height=32, width=74, background='black', foreground='white',font=("Cascadia Mono", 10))
displaychat.place(x=1.5)
displaychat.config(relief='sunken')

entrychat = Text(root, height=5, width=74)
entrychat.place(relx=0.5,rely=0.925,anchor=CENTER)
entrychat.config(relief='sunken')
    
def send_message():
    user_input = entrychat.get("1.0", "end-1c").strip()
    displaychat.insert(tk.END, "\nUser: ", "user")
    displaychat.insert(tk.END, user_input + "\n")
    tokens = nltk.word_tokenize(user_input)
    tagged_tokens = nltk.pos_tag(tokens)
    for token, pos_tag in tagged_tokens:
        displaychat.insert(tk.END, f"Token: ", "token")
        displaychat.insert(tk.END, f"{token}", "normal")
        displaychat.insert(tk.END, f", POS: {pos_tag}\n")
    entrychat.delete("1.0", tk.END)

displaychat.tag_config("user", foreground="green")
displaychat.tag_config("token", foreground="blue")
displaychat.tag_config("normal", foreground="white")

bg_button = Button(root, text="Ask", command=send_message, background='green', foreground='white',font=("Cascadia Mono", 10))
bg_button.place(x=560,y=560)

root.mainloop()
