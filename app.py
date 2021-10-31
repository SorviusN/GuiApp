import tkinter as tk;
from tkinter import Label, filedialog, Text

#Lets us run apps that we will run.
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)

# This is a function
def exitApp():
    root.destroy()

# This is a function
def addApp():
    #If something already exists within the frame, destroy it.
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/Users/Desktop", title="Please Select File",
    # Lets us choose executable files only, or switch to all files if we want to.
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    #Append whichever file we chose to the apps array.
    apps.append(filename)
    print(filename)

    # For every single app within the apps array, 
    # we will create a label and attach it to the frame.
    for app in apps:
        Label = tk.Label(frame, text=app, bg="#b59283")
        Label.pack()

def runApps():
    for app in apps:
        os.startfile(app)
        print("test")

# Sets where you would like to put the canvas of your app.
canvas = tk.Canvas(root, height=600, width=600, bg="#b59283")
canvas.pack()


# Outer frame of the tk application.
frame = tk.Frame(root, bg="#204254")

# Relative width and height of the frame, 
# as well as the position relative to the background.
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=15, pady=10, 
fg="white", bg="#204254", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=15, pady=10, 
fg="black", bg="#b59283", command=runApps)
runApps.pack()

exitApp = tk.Button(root, text="Exit", padx=10, pady=5, fg="white", bg="black", command=exit)
exitApp.pack()

root.mainloop()

# When closing the app, save a text file, write it as f, 
# with f we can write all of our apps.
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
