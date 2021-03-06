import unittest

from rna_transcription import to_rna


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class RNATranscriptionTests(unittest.TestCase):

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual(to_rna('C'), 'G')

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurrences(self):
        self.assertEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    def test_handles_invalid_str_input(self):
        with self.assertRaises(ValueError):
            to_rna('1ACGTC')

    def test_handles_lowercase_input(self):
        with self.assertRaises(ValueError):
            to_rna('agctt')

    def test_handles_invalid_non_str_input(self):
        with self.assertRaises(TypeError):
            to_rna(123)


if __name__ == '__main__':
    unittest.main()
