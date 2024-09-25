import unittest
from main import numeroRandom

class TestNumeroRandom(unittest.TestCase):

    def test_numero_esta_en_rango(self):
        for _ in range(100):
            numero = numeroRandom()
            self.assertTrue(1 <= numero <= 100, f"El número {numero} no está en el rango de 1 a 100")

if __name__ == '__main__':
    unittest.main()