from tkinter import *
from PIL import Image, ImageTk
import pygame
import os


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("MusicPlayer")
        # Window Geometry
        self.root.geometry("1000x600")
        self.root.configure(bg="black")
        root.resizable(False, False)

        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating the Track Frames for Song label & status label

        root.wm_attributes('-transparentcolor', 'blue')
        root.wm_attributes('-transparentcolor', 'green')
        root.wm_attributes('-transparentcolor', 'pink')
        root.wm_attributes('-transparentcolor', 'grey')
        # Inserting Song Track Label
        songtrack = Label(self.root, textvariable=self.track, font=(
            "Segoe Script", 18, "bold"), fg="red").place(x=30, y=250)
        # Inserting Status Label
        trackstatus = Label(self.root, textvariable=self.status, font=(
            "sans serif", 12), bg="blue", fg="pink").place(x=250, y=200)

        # Inserting Play Button
        playbtn = Button(self.root, text="PLAY", command=self.playsong, width=8, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").place(x=130, y=370)
        # Inserting Pause Button
        pausebtn = Button(self.root, text="PAUSE", command=self.pausesong, width=8, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").place(x=130, y=470)
        # Inserting Unpause Button
        unpauseybtn = Button(self.root, text="UNPAUSE", command=self.unpausesong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").place(x=330, y=470)
        # Inserting Stop Button
        stopbtn = Button(self.root, text="STOP", command=self.stopsong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").place(x=330, y=370)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root, text="Playlist", font=(
            "times new roman", 15, "bold"), fg="green", bd=5, width=500, relief=FLAT)
        songsframe.place(x=600, y=0, width=400, height=600)
        # songsframe.place(x=600, y=0, width=400)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=(
            "times new roman", 12, "bold"), bg="#ADD8E6", fg="black", bd=5, width=100, height=600, relief=SUNKEN)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill="y")
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack()
        # Changing Directory for fetching Songs
        os.chdir(r"F:\ASH IMPS\Music Player using Tkinter\songs")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # It will Display the  Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()


root = Tk()

img = ImageTk.PhotoImage(Image.open(
    r"F:\ASH IMPS\Music Player using Tkinter\bg.png"))
ltframe = Frame(root)
ltframe.pack(side=LEFT)
ltframe.place(x=0, y=0)
label = Label(ltframe, image=img)
label.pack(side=LEFT)

logoimg = ImageTk.PhotoImage(Image.open(
    r"F:\ASH IMPS\Music Player using Tkinter\msi.jpg"))
Label(root, image=logoimg, bg="pink", fg="black",
      width=150, height=150).place(x=200, y=20)

m = MusicPlayer(root)
m.playsong()
m.stopsong()
m.pausesong()
m.unpausesong()

root.mainloop()
