from tkinter import Tk, scrolledtext, Menu, filedialog,END
import os

#root for main window
root=Tk()
root.title("Jott Pad")
textArea=ScrolledText.ScrolledText(root,width=100,height=80)

#functions

def newFile():
    if len(textArea.get('1.0',END+'-1c'))> 0:
        if messagebox.askyesno("Save","Do you wish to save?"):
            saveFile()
           
    else:
        textArea.delete('1.0',END)
        root.title("Untitled-Jottpad")
    
    
def openFile():
    
    file=filedialog.askopenfile(parent=root,title=" Select a text file",
                                filetypes=(("Text file","*.txt"),("All files","*.*")))
    
    if file!=None:
        root.title(file.name+ "- Jott pad")
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode="w")
    
    if file!=None:
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
        #changing the name after saving the file
        root.title(file.name + "- Jott Pad")

def copyInFile():
    textArea.event_generate("<<Copy>>")
    
def pasteInFile():
    textArea.event_generate("<<Paste>>")

def cutInFile():
    textArea.event_generate("<<Cut>>")


    
        
def about():
    label=messagebox.showinfo("About"," Jotter Pad - A Python Made Notepad")

def exitApp():
    if messagebox.showinfo("Quit","Are you sure you want to Quit?"):
        root.destroy()
    
#menu options
menu= Menu(root)
root.config(menu=menu)

#file
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exitApp)

#edit
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cutInFile)
editMenu.add_command(label="Copy",command=copyInFile)
editMenu.add_command(label="Paste",command=pasteInFile)




#about
menu.add_cascade(label="About",command=about)
textArea.pack()

#to keep the window open
root.mainloop()