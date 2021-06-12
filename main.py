from tkinter import *
#import tkinter
from pytube import YouTube
from tkinter import messagebox, filedialog

# Global variables declaration
x_axis = 220


# Functions declarations

# Defining Browse() to select a 
# destination folder to save the video
  
def Browse():
    # Presenting user with a pop-up for
    # directory selection. initialdir 
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
   
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)

def Downloader():     
    # url =YouTube(str(video_link.get()))
    # video = url.streams.first()
    # video.download()
    # Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= x_axis , y = 210)  
    # getting user-input Youtube Link
    Youtube_url = video_link.get()
      
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
   
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_url)
   
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.first()
   
    # Downloading the video to destination 
    # directory
    videoStream.download(download_Folder)
   
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY", 
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_Folder)


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    downloader_label = Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold')
    downloader_label.grid(  row=1,
                            column=1,
                            pady = 15)

    link_label = Label(root, 
                       text="YouTube Link  :",
                       bg="#E8D579")
    link_label.grid(row=2,
                    column=0,
                    pady=10,
                    padx=5)
   
    root.linkText = Entry(root,
                          width=57,
                          textvariable=video_link)
    root.linkText.grid(row=2, 
                       column=1,
                       pady=10,
                       padx=5,
                       columnspan = 2)
   
    destination_label = Label(root, 
                              text="Destination    :",
                              bg="#E8D579")
    destination_label.grid(row=3,
                           column=0,
                           pady=10,
                           padx=5)
   
    root.destinationText = Entry(root,
                                 width=42,
                                 textvariable=download_Path)
    root.destinationText.grid(row=3, 
                              column=1,
                              pady=5,
                              padx=0)
   
    browse_B = Button(root, 
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#0060df",
                      fg='#ffffff')
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
   

    Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', fg='#ffffff',cursor='hand2', padx = 6, pady = 4, command = Downloader).place(x=x_axis+12 ,y = 180)


# Driver Code
root = Tk()

root.geometry('600x380')
root.resizable(0, 0)
root.title("Pankaj - Youtube Video Downloader")

video_link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()