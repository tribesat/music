#!/usr/bin/env python3.6
"""Music creation module
"""

import wave
import math
from array import array


class Sound:
    """
    """

    def __init__(self, data: array = array('h')):
        """
        """
        self.data = data

    def __add__(self, sound):
        """
        """
        data = array('h')

        for i in range(min(len(self.data), len(sound.data))):
            data.append(self.data[i] + sound.data[i])

        # append the remaining data if the two sounds have different durations
        while i < len(self.data) - 1:
            data.append(self.data[i])
            i += 1

        while i < len(sound.data) - 1:
            data.append(sound.data[i])
            i += 1

        return Sound(data)

    def append(self, sound):
        """
        """
        self.data += sound.data

    @staticmethod
    def from_freq(frequency: float, duration: int = 1, volume: float = 50):
        """Create the sound
            duration: seconds
            frequency: of cycles per second (Hz) (frequency of the sine waves)
            volume: percent
        """
        data = array('h')  # signed short integer (-32768 to 32767) data
        sampleRate = 44100  # of samples per second (standard)
        numSamplesPerCyc = int(sampleRate / frequency)
        numSamples = int(sampleRate * duration)

        for i in range(numSamples):
            sample = 32767 * float(volume) / 100
            sample *= math.sin(math.pi * 2 *
                               (i % numSamplesPerCyc) / numSamplesPerCyc)
            data.append(int(sample))

        return Sound(data)

    def write_to_file(self, filename: str):
        """
        """
        audiofile = wave.open(filename, "wb")
        audiofile.setnchannels(1)
        audiofile.setsampwidth(2)
        audiofile.setframerate(44100)
        audiofile.writeframes(self.data.tostring())
        audiofile.close()
