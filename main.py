#YouTube Video Downloader
#By Aswin Menon
#Created on 01/09/23

from tkinter import messagebox
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import threading
from tkinter import PhotoImage

#Window Properties
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("300x300")
logo = PhotoImage(file="logo.png")
root.iconphoto(False, logo)
root.resizable(False,False)

#To list the folder
def dir():
   source_path = filedialog.askdirectory(title='Select the path to save the video')
   return source_path

# To process the link, resolutions and download the video
def link(event=None):
    try:
        url = textbox.get()
        yt = YouTube(url)
        unique_resolutions = []

        for stream in yt.streams:
            resolution = stream.resolution
            if resolution is not None and resolution not in unique_resolutions:
                unique_resolutions.append(resolution)

        # Sort the resolutions list
        sorted_resolutions = sorted(unique_resolutions)

        # Update combobox values with sorted resolutions
        combo['values'] = sorted_resolutions

        # Set the highest resolution as the default value
        if sorted_resolutions:
            combo.set(sorted_resolutions[-1])  # Set the highest resolution as default

        # Show a message box for successful loading of resolutions
        messagebox.showinfo("Resolutions Loaded", "Available resolutions are loaded.")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check the link")

# Function to download the selected video
def download_video():
    url = textbox.get()
    selected_resolution = combo.get()

    def download_thread():
        try:
            yt = YouTube(url)
            selected_stream = None
            for stream in yt.streams:
                if stream.resolution == selected_resolution:
                    selected_stream = stream
                    break
            if selected_stream:
                path = selected_stream.download(dir())
                messagebox.showinfo("Download Complete", f"Video downloaded to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred. Please check the link")

 # Start a new thread for downloading
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()
    
#Function to select all the string in the text box
def select_all(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

#Function to replace all the string in the text box
def erase_all(event):
    event.widget.delete(0, 'end')
    return 'break'

#Function to paste the string in the text box
def paste(event=None):
    textbox.delete(0, 'end')
    textbox.insert('end', root.clipboard_get())
    link()  # Call the link function to populate the combobox
    return 'break'

#To display the message
messg = Label(root, text="Enter the link below")
messg.place(x=1,y=10,width=300,height=20)

#Textbox to enter the link
textbox = Entry(root)
textbox.place(x=1,y=40,width=298,height=20)

# Bind the <Return> key event to the link function
textbox.bind("<Return>", link)

#Right click menu
popup_menu = Menu(root, tearoff=0)
popup_menu.add_command(label="Paste", command=paste)
popup_menu.add_command(label="Copy", command=lambda:textbox.event_generate("<<Copy>>"))
popup_menu.add_command(label="Select All", command=lambda:textbox.event_generate("<<SelectAll>>"))
popup_menu.add_command(label="Cut", command=lambda:textbox.event_generate("<<Cut>>"))

#Key Bindings
textbox.bind('<Control-a>', select_all)
textbox.bind('<Control-A>', select_all)
textbox.bind('<Control-e>', erase_all)
textbox.bind('<Control-E>', erase_all)
textbox.bind('<Control-v>', paste)
textbox.bind('<Control-V>', paste)

#To display the right click menu
textbox.bind("<Button-3>", lambda e: popup_menu.post(e.x_root, e.y_root))

#Left click to close the menu
def popupFocusOut(self,event=None):
        popup_menu.unpost()

#To close the menu when the focus is out of the menu
root.bind("<Button-1>",popupFocusOut)

#To display the message
video_quality = Label(root, text="Select the video quality")
video_quality.place(relx=0.46, rely=0.41, anchor=CENTER)

#Creating combo box
combo = ttk.Combobox(root, state="readonly", values=[])
combo.pack(pady=140)

#To display the message
note = Label(root, text="Use SAVE TO button to change the path")
note.place(relx=0.49, rely=0.67, anchor=CENTER)

#Download button
download_button = Button(root, text="Download", command=download_video)
download_button.place(relx=0.84, rely=0.88, anchor=CENTER)

#Clear Button
clear_button = Button(root, text="Clear", command=lambda:textbox.delete(0, END))
clear_button.place(relx=0.11, rely=0.88, anchor=CENTER)

#Save to button
directory_button = tk.Button(root, text="Save To", command=dir)
directory_button.place(relx=0.45, rely=0.88, anchor=CENTER)

root.mainloop()
