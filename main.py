import glob
import types
from fileinput import filename

from pydub import AudioSegment
import math
import os
import speech_recognition as sr
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import shutil

def shorten_filename(filename):
    f = os.path.split(filename)[1]
    return "%s~%s" % (f[:3], f[-16:]) if len(f) > 19 else f

def browseFiles():
    filenamez = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Audiofiles",
                                                      "*.m4a*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="Выбран аудиофайл: " + filenamez)
    folder = 'C:\\Users\\Artem\\PycharmProjects\\Selecta'
    global path12
    path12 = shutil.copy(filenamez, folder)
    namefile = shorten_filename(path12)
    print(namefile)
    print (path12)

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 59 * 1000
        t2 = to_min * 59 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            b = 1000
            b=b+i
            split_fn = str(b) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


def btn_start():
    folder = 'C:\\Users\\Artem\\PycharmProjects\\Selecta'
    # path = shutil.copy(filenamez, folder)
    # path = "C:\\Users\\Artem\\PycharmProjects\\Selecta\\Recording (2).m4a"
    # file1 = 'audio.mp3'
    path = path12
    sound = AudioSegment.from_file(path, format='mp3')
    sound = sound + 5
    sound.export("C:\\Users\\Artem\\PycharmProjects\\Selecta\\sound.wav", format="wav")
    os.remove(path)
    file = 'sound.wav'
    nameWav = file[file.find(''): file.find('.')]
    print(nameWav)
    split_wav = SplitWavAudioMubin(folder, file)
    split_wav.multiple_split(min_per_split=1)
    yourDIR = 'C:\\Users\\Artem\\PycharmProjects\\Selecta'
    files = os.listdir(yourDIR)
    filelist = filter(lambda x: x.endswith('.wav'), files)

    f = open("Selector.txt", "w")
    wavCounter = len(glob.glob1(str(folder), "*.wav"))
    print(wavCounter)
    k=-1
    os.remove('sound.wav')
    for i in filelist:
        k=k+1
        print(i)
        if k==wavCounter-1:
            break
        else:
            с = i[i.find('1') + 2: i.find('_')]
            r = sr.Recognizer()
            file = sr.AudioFile(i)
            with file as source:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
                result = r.recognize_google(audio, language='ru')
                try:
                    f.write("\n" + с + " minute: ")
                    f.write(result)
                    print(result)
                except Exception as e:
                    print(e)

        os.remove("C:\\Users\\Artem\\PycharmProjects\\Selecta\\" + i)

# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
#window.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Путь к файлу: ",
                            width=70, height=2)
labelEmpty0 = Label(window,
                   width=70, height=2)

button_explore = Button(window,
                        text="Обзор файлов",
                        command=browseFiles, font="6dp")
labelEmpty1 = Label(window,
                   width=70, height=2)

button_start = Button(window,
                      text="Транскрибировать", command=btn_start, font="6dp")

labelEmpty2 = Label(window,
                   width=70, height=2)

button_exit = Button(window,
                     text="Выход",
                     command=exit, font="6dp")

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)
labelEmpty0.grid(column=1, row=2)
button_explore.grid(column=1, row=3)
labelEmpty1.grid(column=1, row=4)
button_start.grid(column=1, row=5)
labelEmpty2.grid(column=1, row=6)
button_exit.grid(column=1, row=7)

window.mainloop()


#def main():


#if __name__ == "__main__":
 #   main()
