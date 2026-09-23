import unittest

from vocabulario_alemao import GerenciadorVocabularioAlemao


class TestGerenciadorVocabularioAlemao(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorVocabularioAlemao()

    def test_termo_conhecido(self):
        resultado = self.gerenciador.consultar_termo("Schlüssel")
        self.assertIn("der Schlüssel", resultado)
        self.assertIn("Chave", resultado)

    def test_busca_nao_diferencia_maiusculas(self):
        resultado = self.gerenciador.consultar_termo("wissenschaft")
        self.assertIn("die Wissenschaft", resultado)

    def test_espacos_sao_ignorados(self):
        resultado = self.gerenciador.consultar_termo("  Architektur  ")
        self.assertIn("die Architektur", resultado)

    def test_termo_desconhecido(self):
        resultado = self.gerenciador.consultar_termo("Python")
        self.assertIn("não foi cadastrado", resultado)

    def test_termo_vazio(self):
        with self.assertRaises(ValueError):
            self.gerenciador.consultar_termo("   ")


if __name__ == "__main__":
    unittest.main()
