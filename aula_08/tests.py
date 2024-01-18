

def soma(a, b):
    return a + b 


nomes = ["julio", "fabricio", "andréia"]


# Forma 01 dde teste
# soma_5_4 = soma(5, 4) #9

# assert soma_5_4 == 9, "A valor esperado da soma é 9"

# print('Funcão soma esta ok')


# assert len(nomes) == 2, "A valor esperado é 2"



# FORMA 02 DE teste (Class)
import unittest

class TestesUnitarios(unittest.TestCase):

    def teste_soma(self):
        soma_5_4 = sum([5,4]) # 9

        self.assertEqual(soma_5_4, 9, "O valor esperado é 9")

    def teste_nomes(self):
        nomes = ["julio", "Barbara"]

        self.assertEqual(len(nomes), 2, "O valor esperado é 2")



if __name__ == "__main__":
    unittest.main()


