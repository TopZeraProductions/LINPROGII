import unittest

class SearchFile():

    def __init__(self, arquivo):
        self.lista = arquivo.readlines()

    def buscar(self, string):
        cont = []

        for linha in self.lista:
            if string in linha:
                cont.append(string)

        return cont

class TestSearch(unittest.TestCase):
    
    def test_01_buscar(self):
        arquivo = open('texto1.txt')
        sf = SearchFile(arquivo)
        self.assertEqual(len(sf.buscar('a')), 2)
        self.assertEqual(len(sf.buscar('b')), 1)
        self.assertEqual(len(sf.buscar('c')), 1)
        self.assertEqual(len(sf.buscar('z')), 0)
        self.assertEqual(len(sf.buscar('pinha')), 1)
    
    def test_02_buscar(self):
        arquivo = open('texto1.txt')
        sf = SearchFile(arquivo)
        self.assertEqual(len(sf.buscar('z')), 0)
        self.assertEqual(len(sf.buscar('c')), 1)
        self.assertEqual(len(sf.buscar('b')), 1)
        self.assertEqual(len(sf.buscar('a')), 2)
    
    def test_03_buscar(self):
        arquivo = open('texto2.txt')
        sf = SearchFile(arquivo)
        self.assertEqual(len(sf.buscar('padrao')), 4)
        self.assertEqual(len(sf.buscar('projeto')), 1)

    def ntest_04_adapter(self):
        import file_explorer
        ea = file_explorer.ExplorerAdapter()
        sf = SearchFile(ea)
        self.assertEqual(len(sf.buscar('padrao')), 4)
        self.assertEqual(len(sf.buscar('projeto')), 1)
        self.assertEqual(len(sf.buscar('pinha')), 1)

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSearch)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

runTests()
