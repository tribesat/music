import math, struct, sys
import csv
from midiutil.MidiFile import MIDIFile
from sound import Sound
#from StringIO import StringIO

#assume CSV input--want to convert to format readable by MIDI instruments

def TXT_to_MIDI(txtfile):
    sensors = 7 #number of instruments, assume organized by columns
    file = open (txtfile, 'r')
    data = []
    for line in file:
        data.append([float(x) for x in line.split()])
    size=len(data)
    mf = MIDIFile(sensors) #can make two channels, but starting with 1
    #memFile = StringIO()
    volume = 100
    duration = 1 #can make variable, right now 1 beat
    time = 0 #start time
    channel = 0 #1-16 MIDI channels
    tempo = 60 #BPM
    for inst in range(sensors):
        track = inst
        mf.addTempo(track, time, tempo)
        for i in range(size):
            currentData = data[i][inst]
            pitch = data_to_pitch(currentData)
            time += 1
            mf.addNote(track, channel, pitch, time, duration, volume)
#pitch needs to be between 0 and 255--need to double check MIDI mapping vs freq
    with open('output.mid', 'wb') as output_file:
        mf.writeFile(output_file)
    #mf.writeFile(memFile)

def data_to_pitch(sensorData):
    pitch = Sound(sensorData)
    freq = pitch.from_freq(sensorData)
    return freq
    #convert data to frequency for note on scale

TXT_to_MIDI('test_data.txt')
