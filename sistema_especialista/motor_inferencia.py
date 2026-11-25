
from .fatos import criar_base_fatos, FATOS_INFERIDOS
from .regras import REGRAS


def executar_inferencia(base_fatos):
    """
    Executa o motor de inferência do TechExpert utilizando
    encadeamento para frente (Forward Chaining).

    Retorna os fatos atualizados e o histórico das regras
    que foram ativadas durante o diagnóstico.
    """

    # Verifica se a base recebida possui todos os fatos inferidos.
    if not isinstance(base_fatos, dict):
        raise TypeError("A base de fatos deve ser um dicionário.")

    for fato in FATOS_INFERIDOS:
        if fato not in base_fatos:
            raise KeyError(f"Fato ausente na base: {fato}")

    regras_disparadas = set()
    historico = []

    houve_inferencia = True

    while houve_inferencia:
        houve_inferencia = False

        for regra in REGRAS:

            identificador = regra["id"]

            # Impede que uma mesma regra seja executada novamente.
            if identificador in regras_disparadas:
                continue

            condicoes_satisfeitas = all(
                base_fatos.get(fato) is valor
                for fato, valor in regra["condicoes"].items()
            )

            if condicoes_satisfeitas:

                conclusao = regra["conclusao"]

                # Registra a conclusão na base de fatos.
                base_fatos[conclusao] = True

                # Registra a regra como executada.
                regras_disparadas.add(identificador)

                # Guarda informações para explicar o diagnóstico.
                historico.append({
                    "regra": identificador,
                    "categoria": regra["categoria"],
                    "condicoes": regra["condicoes"].copy(),
                    "conclusao": conclusao,
                    "explicacao": regra["explicacao"],
                    "recomendacao": regra["recomendacao"]
                })

                houve_inferencia = True

    # Organiza as conclusões encontradas.
    diagnosticos = []

    for fato, valor in base_fatos.items():
        if fato in FATOS_INFERIDOS and valor is True:
            diagnosticos.append(fato)

    return {
        "base_fatos": base_fatos,
        "diagnosticos": diagnosticos,
        "historico": historico,
        "regras_ativadas": len(regras_disparadas)
    }


def criar_diagnostico():
    """
    Cria uma nova base de fatos para um diagnóstico.
    """

    return executar_inferencia(criar_base_fatos())
