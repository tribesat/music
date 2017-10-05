"""
"""

from tribesat_music import note_to_freq
from tribesat_music.sound import Sound

# notes and durations for Mary Had a Little Lamb in the key of C
mary_had = [
    ("E4", 1), ("D4", 1), ("C4", 1), ("D4", 1),
    ("E4", 1), ("E4", 1), ("E4", 2),
    ("D4", 1), ("D4", 1), ("D4", 2),
    ("E4", 1), ("E4", 1), ("E4", 2),
    ("E4", 1), ("D4", 1), ("C4", 1), ("D4", 1),
    ("E4", 1), ("E4", 1), ("E4", 1), ("E4", 1),
    ("D4", 1), ("D4", 1), ("E4", 1), ("D4", 1), ("C4", 2),
]

tune = Sound()

for note in mary_had:
    tune.append(Sound.from_freq(note_to_freq(note[0]), duration=note[1]))

tune.write_to_file("mary_had_a_little_lamb.wav")


