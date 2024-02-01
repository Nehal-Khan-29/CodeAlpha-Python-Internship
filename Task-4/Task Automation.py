# Modules ==========================================================================================================

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import shutil

# Extension ========================================================================================================

extension_to_folder = {
    'py': 'Python',
    'c': 'C',
    'cpp': 'C++',
    'java': 'Java',
    'html': 'HTML',
    'css': 'HTML',
    'js': 'HTML',
}

# Main ========================================================================================================

def main():
    global destination_dir, source_dir
    
    if destination_dir == "":
        messagebox.showerror("Error", "Destination Directory not selected")
    if source_dir == "":
        messagebox.showerror("Error", "Source Directory not selected")
    
    for folder in extension_to_folder.values():
        folder_path = os.path.join(destination_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, filename)
        
        name, extension = os.path.splitext(filename)
        extension = extension[1:]
        
        if extension in extension_to_folder:
            destination_folder = extension_to_folder[extension]
            destination_path = os.path.join(destination_dir, destination_folder, filename)
            
            shutil.move(source_file_path, destination_path)
            
    messagebox.showinfo("Success", "File Automation successful!")
            
            
root = tk.Tk()
root.title('Task Automation')
root.resizable(False,False)
root.geometry('300x300')
bg_image = Image.open("Task-4/bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300 
window_height = 350
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)
root.geometry("+{}+{}".format(x, y))

def source():
    global source_dir
    source_dir = fd.askdirectory()
def dest():
    global destination_dir
    destination_dir = fd.askdirectory()
    
Button(root, text='Source Directory', command=source, height=1, width=20, font=('Comic Sans MS', 10, 'bold')).place(relx=0.5, rely=0.35, anchor=CENTER)
Button(root, text='Destination Directory', command=dest, height=1, width=20, font=('Comic Sans MS', 10, 'bold')).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(root, text='Automate', command=main, height=1, width=10, bg='blue', fg='white', font=('Comic Sans MS', 10, 'bold')).place(relx=0.5, rely=0.65, anchor=CENTER)

root.mainloop()
