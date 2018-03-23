import math, struct, sys
import csv
from midiutil.MidiFile import MIDIFile
from sound import Sound

def TXT_to_MIDI(txtfile):
    sensors = 7 #number of instruments, assume organized by columns
    file = open (txtfile, 'r')
    data = []
    for line in file:
        data.append([float(x) for x in line.split()])
    size=len(data)
    mf = MIDIFile(sensors) #can make two channels, but starting with 1
    volume = 100
    duration = 1 #can make variable, right now 1 beat
    channel = 0 #1-16 MIDI channels, keeping all on one for now
    tempo = 60 #BPM
    for inst in range(sensors):
        track = inst
        mf.addTempo(track, time, tempo)
        for i in range(len(data[inst])):
            currentData = data[inst][i]
            pitch = data_to_pitch(currentData, duration, volume)
            mf.addNote(track, channel, pitch, i, duration, volume) #i==time


    with open('output8.mid', 'wb') as output_file:
        mf.writeFile(output_file)


def data_to_pitch(sensorData, duration, volume):
    frequency = sensorData
    sampleRate = 44100  # of samples per second (standard)
    if frequency == 0:
        numSamplesPerCyc = 1
    else:
        numSamplesPerCyc = int(sampleRate / frequency)
    numSamples = int(sampleRate * duration)
    for i in range(numSamples):
        sample = 32767 * float(volume) / 100
        sample *= math.sin(math.pi * 2 *
                    (i % numSamplesPerCyc) / numSamplesPerCyc)
    if sample == 0:
        mv = 0
    else:
        mv = 69 + 12 * math.log(abs(sample/440))/math.log(2)
    return int(abs(mv+4*12)) #bumps up n octaves (midi increments of 12, better sound in library for low freq data)
    #convert data to frequency for note on scale

TXT_to_MIDI('test_data5.txt')
