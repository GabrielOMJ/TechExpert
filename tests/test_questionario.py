
import unittest

from sistema_especialista.questionario import obter_proxima_pergunta


class TesteQuestionario(unittest.TestCase):

    def test_primeira_pergunta_inicializacao(self):
        pergunta = obter_proxima_pergunta("inicializacao", {})

        self.assertEqual(pergunta["fato"], "computador_nao_liga")

    def test_pergunta_condicional(self):
        respostas = {
            "computador_nao_liga": True
        }

        pergunta = obter_proxima_pergunta("inicializacao", respostas)

        self.assertEqual(
            pergunta["fato"],
            "indicadores_energia_acesos"
        )

    def test_pergunta_nao_apresentada_quando_condicao_falsa(self):
        respostas = {
            "computador_nao_liga": False
        }

        pergunta = obter_proxima_pergunta("inicializacao", respostas)

        self.assertEqual(
            pergunta["fato"],
            "reinicia_antes_sistema"
        )

    def test_questionario_concluido(self):
        respostas = {
            "computador_nao_liga": False,
            "reinicia_antes_sistema": False
        }

        pergunta = obter_proxima_pergunta("inicializacao", respostas)

        self.assertIsNone(pergunta)

    def test_categoria_invalida(self):
        with self.assertRaises(ValueError):
            obter_proxima_pergunta("categoria_invalida", {})

    def test_resposta_invalida(self):
        respostas = {
            "computador_nao_liga": "sim"
        }

        with self.assertRaises(ValueError):
            obter_proxima_pergunta("inicializacao", respostas)


if __name__ == "__main__":
    unittest.main()
