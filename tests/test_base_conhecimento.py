
"""
Testes da base de conhecimento.
"""

import unittest

from sistema_especialista.fatos import (
    criar_base_fatos,
    registrar_resposta,
    FATOS_INICIAIS,
    FATOS_INFERIDOS
)

from sistema_especialista.regras import (
    REGRAS,
    validar_base_regras,
    quantidade_regras,
    obter_regras_categoria
)


class TesteBaseConhecimento(unittest.TestCase):

    def test_criacao_base_fatos(self):
        base = criar_base_fatos()

        self.assertEqual(
            len(base),
            len(FATOS_INICIAIS) + len(FATOS_INFERIDOS)
        )

        self.assertIsNone(
            base["computador_nao_liga"]
        )

    def test_registrar_resposta(self):
        base = criar_base_fatos()

        registrar_resposta(
            base,
            "computador_nao_liga",
            True
        )

        self.assertTrue(
            base["computador_nao_liga"]
        )

    def test_resposta_invalida(self):
        base = criar_base_fatos()

        with self.assertRaises(TypeError):
            registrar_resposta(
                base,
                "computador_nao_liga",
                "sim"
            )

    def test_fato_inexistente(self):
        base = criar_base_fatos()

        with self.assertRaises(KeyError):
            registrar_resposta(
                base,
                "fato_inexistente",
                True
            )

    def test_quantidade_regras(self):
        self.assertEqual(quantidade_regras(), 30)

    def test_validacao_regras(self):
        valido, mensagem = validar_base_regras()

        self.assertTrue(valido, mensagem)

    def test_regras_por_categoria(self):
        regras = obter_regras_categoria("temperatura")

        self.assertGreater(len(regras), 0)

        for regra in regras:
            self.assertEqual(
                regra["categoria"],
                "temperatura"
            )


if __name__ == "__main__":
    unittest.main()
