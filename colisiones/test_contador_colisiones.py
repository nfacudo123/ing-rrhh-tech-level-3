import unittest
from contador_colisiones import cont_colision

#Pruebas Unitarias para revisar el código y su secuencia
class TestCountcolis(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(cont_colision('LR'), '0 0')
        self.assertEqual(cont_colision('RL'), '1 1')
        self.assertEqual(cont_colision('RRR'), '0 0 0')
        self.assertEqual(cont_colision('RRL'), '1 2 1')

if __name__ == '__main__':
    unittest.main()
