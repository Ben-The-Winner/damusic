# Beat tracking example

import librosa
from tkinter import *

root = Tk()
root.geometry("400x400")

# import numpy as np
# import matplotlib.pyplot as plt
# import librosa.display
from songify import songify
import IPython.display as ipd
# import mir_eval.sonify

# 1. Get the file path to an included audio example
filename = librosa.example('nutcracker')
ipd.Audio(filename)
# 2. Load the audio as a waveform `y`, Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Extract the notes 
notes = librosa.midi_to_note(range(0,22), key='F:min')
words = notes

# 4. Rearrange them with an algo from songify.py
notes = songify(notes)
words2 = notes

# 5. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
words3 = tempo

# 6. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)



def Click():
    myLabel = Label(root, text = words)
    myLabel.pack()

def Click2():
    myLabel2 = Label(root, text = words2)
    myLabel2.pack()



def Click3():
    myLabel3 = Label(root, text = words3)
    myLabel3.pack()



myButton= Button(root, text= "click here to see the original notes", command= Click, bg="yellow")
myButton.pack()

myButton2= Button(root, text= "click here to see the shuffled notes", command= Click2, bg="green")
myButton2.pack()


myButton3= Button(root, text= "click here to see the tempo", command= Click3, bg="red")
myButton3.pack()

root.configure(background="#f0ff33")


root.mainloop()


