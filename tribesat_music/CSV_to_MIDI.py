import math, struct, sys
import csv
from midiutil.MidiFile import MIDIFile
import sound.py

#assume CSV input--want to convert to format readable by MIDI instruments

def CSV_to_MIDI('CSVfile'):
    with open(CSVfile, 'rb') as data:
        inputData = csv.reader(data)
    sensors = 7#number of instruments-->depends on how writes to CSV,
    #but assuming each instrument is in different file, but might need to change
    size = len(inputData)
    mf = MIDIFile(1) #can make two channels, but starting with 1
    volume = 100
    duration = 1 #can make variable, right now 1 beat
    time = 0 #start time
    for inst in range(sensors):
        track = inst
        for i in range(size):
            currentData = inputData[i][inst]
            pitch = data_to_pitch(currentData)
            time += 1
            mf.addNote(track, channel, pitch, time, duration, volume)
            track+=1

def data_to_pitch(sensorData):
    pitch = Sound(sensorData)
    freq = pitch.from_freq(sensorData)
    return freq
    #convert data to frequency for note on scale
