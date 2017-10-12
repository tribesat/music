"""Note to freqency
This module implements a function that maps note names
to frequencies

Authors: Hana Warner (hkwarner@email.wm.edu)
         Kelvin Abrokwa (kkabrokwajohns@email.wm.edu)
"""

# order of notes
NOTES_FLAT = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
NOTES_SHARP = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def note_to_freq(note: str) -> float:
    """Maps notes to frequencies
    """
    try:
        octave = int(note[-1])
    except:
        raise Exception('Octave must be an integer')

    if len(note) == 2:
        n = note[0]
        try:
            distance = NOTES_FLAT.index(n)
        except:
            raise Exception("Invalid note: " + note)
    elif len(note) == 3:
        n = note[:2]
        try:
            distance = [NOTES_FLAT, NOTES_SHARP][int(n[1] == '#')].index(n)
        except:
            raise Exception("Invalid note: " + note)
    else:
        raise Exception("Incorrectly formatted note input")

    C4_freq = 261.63 * 2 ** (octave - 4)
    freq = C4_freq * 2 ** (distance / 12)

    return freq
