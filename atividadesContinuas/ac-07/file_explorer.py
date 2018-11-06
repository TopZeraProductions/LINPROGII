import glob
import unittest

class TxtExplorer():

    def __init__(self):
        self.arquivos = {}
        for nome_arquivo in glob.glob('*txt'):
            dic = {}
            self.arquivos[nome_arquivo] = dic
            dic['objeto arquivo'] = open(nome_arquivo)
            dic['acabou'] = False

    def prox_linha(self, nome_arquivo):
        linha = self.arquivos[nome_arquivo]['objeto arquivo'].readline()
        if linha == '':
            self.arquivos[nome_arquivo]['acabou'] = True
        return linha

    def nomes(self):
        return list(self.arquivos.keys())

    def acabou(self, nome_arquivo):
        pass # Você precisa mexer nesse método!

    def reiniciar(self, arq):
        self.arquivos[arq]['objeto arquivo'].seek(0)
        self.arquivos[arq]['acabou'] = False



class ExplorerAdapter():
    '''
    No init simplesmente pegamos uma instância de TxtExplorer para manipular.
    Esse método já está pronto.
    '''
    def __init__(self):
        self.te = TxtExplorer()

    '''
    Esse método, deve sempre receber 0 como único argumento, e resetar o explorer associado.
    Ou seja: reiniciar cada um dos arquivos.
    Se ele receber algum outro argumento que não seja 0, deve levantar uma exceção.
    '''
    def seek(self, num):
        pass # Você precisa mexer nesse método!

    '''
    Este método deve retornar uma lista de todas as linhas de todos os txt disponíveis.

    Ele deve fazer isso pegando a lista de arquivos disponiveis em nosso
    TxtExplorer te, lendo linha a linha e colocando as linhas obtidas em uma lista.
    '''
    def readlines(self):
        pass # Você precisa mexer nesse método!


class TestExplorer(unittest.TestCase):
    '''
    O TxTExplorer deve achar todos os arquivos txt do diretório.
    '''

    def test_01_nomes(self):
        te = TxtExplorer()
        self.assertTrue('texto1.txt' in te.nomes())
        self.assertTrue('texto2.txt' in te.nomes())

    def test_02_prox_linha(self):
        te = TxtExplorer()
        self.assertEqual(te.prox_linha('texto1.txt'), 'a\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'b\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'c\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'pinha')
        self.assertEqual(te.prox_linha('texto2.txt'),
                         'Strategy e um padrao de projeto de software (do ingles design pattern), \n')

    def test_03_prox_linha(self):
        te = TxtExplorer()
        te.prox_linha('texto1.txt')
        self.assertFalse(te.acabou('texto1.txt'))
        te.prox_linha('texto1.txt')
        self.assertFalse(te.acabou('texto1.txt'))
        te.prox_linha('texto1.txt')
        self.assertFalse(te.acabou('texto1.txt'))
        te.prox_linha('texto1.txt')
        self.assertFalse(te.acabou('texto1.txt'))
        te.prox_linha('texto1.txt')
        self.assertTrue(te.acabou('texto1.txt'))

    def test_04_reiniciar(self):
        te = TxtExplorer()
        self.assertEqual(te.prox_linha('texto1.txt'), 'a\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'b\n')
        te.reiniciar('texto1.txt')
        self.assertEqual(te.prox_linha('texto1.txt'), 'a\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'b\n')
        te.reiniciar('texto1.txt')
        self.assertEqual(te.prox_linha('texto1.txt'), 'a\n')
        self.assertEqual(te.prox_linha('texto1.txt'), 'b\n')

    def test_05_acabou(self):
        te = TxtExplorer()
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        linha = te.prox_linha('texto1.txt')
        self.assertTrue(te.acabou('texto1.txt'))

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestExplorer)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

runTests()