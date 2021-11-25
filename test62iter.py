import unittest
import atp62iter as code

class TestProgramm(unittest.TestCase):
    def test_high_and_low_number(self):
        a = code.create(15)
        a = sorted(a)
        list_a = []
        list_a.append(a[0])
        list_a.append(a[len(a) - 1])

        list_low_and_high = code.high_and_low_number(a)

        self.assertEqual(list_a, list_low_and_high)
