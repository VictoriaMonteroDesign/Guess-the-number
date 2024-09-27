import unittest
from main import validarIntento

class TestValidacion(unittest.TestCase):
    def test_acertar(self):
        # paso 1: preparar
        intento = 10
        numeroRandom = 10
        intentosJugador = []
        intentosComputadora = []
        # paso 2: actuar
        resultado = validarIntento(intento, numeroRandom, intentosJugador, intentosComputadora)
        # paso 3: confirmar

        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()