import unittest
from regula_falsi import regula_falsi

class Tests(unittest.TestCase):

    # Passed
    def test_one_root(self):
        self.assertEqual(regula_falsi(lambda x: x ** 3 + 2 * x ** 2 + 10 * x - 20, 2, 3, 0), 1.3688081078213727)

    # Failed - bring incorrect root
    def test_not_correct_root(self):
        self.assertEqual(regula_falsi(lambda x: x**5 - 2 * x + 1, 0.53524852, 0.99, 0), 1)

    # Failed - divergence because of the error limitation less than 1.6
    # Passed - convergence error limitation less than 1.6
    def test_other_root(self):
        self.assertEqual(regula_falsi(lambda x: x**5 - 2 * x + 1, -1.4, -1.28, 1.6), -1.290310384560915)

