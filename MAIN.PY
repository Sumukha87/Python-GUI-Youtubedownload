import tkinter
from turtle import title
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink=link.get()
        ytobj = YouTube(ytlink,on_progress_callback=on_progress)
        video = ytobj.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid")
    print("Download Complete")

def on_progress(stream,chunk,bytes_remaning):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaning
    percentage=bytes_downloaded/total_size*100
    per=str(int(percentage))
    pPercentage.configure(text=per+"%")
    pPercentage.update()



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloder")

title=customtkinter.CTkLabel(app,text="Insert a link")
title.pack(padx=10,pady=10)
url_var=tkinter.StringVar()
link= customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

pPercentage= customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()
progerssBar=customtkinter.CTkProgressBar(app,width=400)
progerssBar.set(0)
progerssBar.pack(padx=20,pady=20)



download=customtkinter.CTkButton(app,text="Downlode",command=startDownload)

download.pack(padx=20,pady=20)
app.mainloop()