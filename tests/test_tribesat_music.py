import unittest
from tribesat_music import note_to_freq
from parameterized import parameterized


class TestTribesatMusic(unittest.TestCase):
    @parameterized.expand([
        ["C0", 16.35],  # low note
        ["F#0", 23.12],  # a sharp
        ["Ab2", 103.83],  # sharp
        ["C4", 261.63],  # base for comparison
        ["A#8", 7458.62],  # very high note
    ])
    def test_note_to_freq(self, note, freq):
        """Test note to frequency function"""
        margin = 0.2
        self.assertTrue(abs(note_to_freq(note) - freq) < margin)

    @parameterized.expand([
        [""],
        ["A"],
        ["Z1"],
        ["Zb"],
        ["Z#"],
        ["AF"],
    ])
    def test_note_to_freq_errors(self, note):
        """Test note to frequency function exceptions"""
        with self.assertRaises(Exception):
            note_to_freq(note)
