#!/usr/bin/python
#title    : gui
#aurthor  : ashish varshney

from library import *

def gui():
    root = Tk()
    root.title("Hit Vote")
    root.geometry("400x400") # set starting size of window
    root.maxsize(400, 320) # width x height
    root.config(bg="white") # set background color of root window

    menubar = Menu(root)
    root.config(menu=menubar)
            

    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=fileMenu)
            
    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="About")
    helpMenu.add_command(label="Contact us")
    menubar.add_cascade(label="Help", menu=helpMenu)


    login = Label(root, text="Vote a Candidate", bg="#2176C1", fg='white', relief=RAISED)
    login.pack(ipady=5, fill='x')
    login.config(font=("Font", 20)) # change font and size of label

    # login image
    image = PhotoImage(file="vote.png")
    img_resize = image.subsample(5,5)
    Label(root, image=img_resize, bg="white", relief=SUNKEN).pack(pady=15)


    # name Entry 
    username_frame = Frame(root, bg="white")
    username_frame.pack()
    Label(username_frame, text="Name", bg="white").pack(side='left', padx=1, pady=5)
    username_entry = Entry(username_frame, bd=3)
    username_entry.pack(side='right')

    # Url Entry
    url_frame = Frame(root, bg="white")
    url_frame.pack()
    Label(url_frame, text="URL", bg="white").pack(side='left', padx=7)
    url_entry = Entry(url_frame, bd=3)
    url_entry.pack(side='right')

    # Create Go! Button
    go_button = Button(root, text="GO!", command=lambda: action(username_entry, url_entry), bg="#66ccff", width=15)
    go_button.pack(pady=5)


    root.mainloop()