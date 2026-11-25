
import unittest

from sistema_especialista.fatos import criar_base_fatos, registrar_resposta
from sistema_especialista.motor_inferencia import executar_inferencia


class TesteMotorInferencia(unittest.TestCase):

    def test_inferencia_superaquecimento(self):
        base = criar_base_fatos()

        registrar_resposta(base, "temperatura_elevada", True)
        registrar_resposta(base, "desligamento_sob_carga", True)

        resultado = executar_inferencia(base)

        self.assertTrue(
            resultado["base_fatos"]["possivel_superaquecimento"]
        )

    def test_encadeamento_regras(self):
        base = criar_base_fatos()

        registrar_resposta(base, "temperatura_elevada", True)
        registrar_resposta(base, "desligamento_sob_carga", True)
        registrar_resposta(base, "ventoinha_nao_gira", True)

        resultado = executar_inferencia(base)

        self.assertTrue(
            resultado["base_fatos"]["possivel_superaquecimento"]
        )

        self.assertTrue(
            resultado["base_fatos"]["necessita_avaliacao_refrigeracao"]
        )

    def test_historico_inferencia(self):
        base = criar_base_fatos()

        registrar_resposta(base, "computador_lento", True)
        registrar_resposta(base, "armazenamento_quase_cheio", True)

        resultado = executar_inferencia(base)

        self.assertGreater(len(resultado["historico"]), 0)

    def test_sem_diagnostico(self):
        base = criar_base_fatos()

        resultado = executar_inferencia(base)

        self.assertEqual(resultado["diagnosticos"], [])
        self.assertEqual(resultado["regras_ativadas"], 0)

    def test_base_invalida(self):
        with self.assertRaises(TypeError):
            executar_inferencia(None)


if __name__ == "__main__":
    unittest.main()
