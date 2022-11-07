import tkinter
from pytube import YouTube
from tkinter import ttk


root = tkinter.Tk ()
root.geometry("330x150")
root.title("edvd yt")
root.resizable(width=False, height=False)

# def
def main():

    forma = listeCombo.get()
    vid = saisie.get()
    yt = YouTube(vid)
    if(forma == 'mp3'):
        yt.streams.filter(only_audio = True).first().download(filename = "downloaded_audio.mp3")
    else:
        yt.streams.filter(progressive = True, 
    file_extension = "mp4").first().download(filename = "downloaded_video.mp4")

    valid.pack()
# obj
obj = tkinter.Label (text = "edvd yt  by anubyx")
obj2 = tkinter.Label (text = "extracteur de data vidéo digital Youtube")
saisie = tkinter.Entry (width= 300)
valid = tkinter.Label (text = "the download is complete ")
bouton = tkinter.Button (text = "download", command=main)
listeformat = ["mp4", "mp3"]
listeCombo = ttk.Combobox(root, values=listeformat, width=5, state="readonly")
listeCombo.current(0)


#(text="format", values=VALEURS)


# pack
obj.pack ()
saisie.pack()
listeCombo.pack()
bouton.pack()
obj2.pack()
root.mainloop ()