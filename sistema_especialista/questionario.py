
"""
Questionário dinâmico do TechExpert.
Responsável por selecionar as perguntas conforme
as respostas fornecidas pelo usuário.
"""

CATEGORIAS_QUESTIONARIO = {
    "inicializacao": "Problemas ao ligar o computador",
    "video": "Problemas de imagem e vídeo",
    "temperatura": "Temperatura e refrigeração",
    "desempenho": "Lentidão e travamentos",
    "conectividade": "Problemas de conexão",
    "software": "Problemas com programas e sistema"
}


PERGUNTAS = {
    "computador_nao_liga": "O computador não liga?",
    "indicadores_energia_acesos": "Alguma luz indicadora de energia acende?",
    "sinais_sonoros_inicializacao": "O computador emite sinais sonoros ao tentar iniciar?",
    "reinicia_antes_sistema": "O computador reinicia antes de carregar o sistema operacional?",

    "monitor_sem_sinal": "O monitor apresenta a mensagem de ausência de sinal?",
    "monitor_ligado": "O monitor está ligado?",
    "cabos_video_conectados": "Os cabos de vídeo estão conectados corretamente?",
    "outro_monitor_funciona": "O computador funciona normalmente com outro monitor?",

    "temperatura_elevada": "O computador apresenta temperatura elevada?",
    "desligamento_sob_carga": "O computador desliga durante atividades que exigem mais desempenho?",
    "ventoinha_nao_gira": "Alguma ventoinha parece não estar girando?",
    "ventoinha_ruido_anormal": "As ventoinhas apresentam ruídos anormais?",
    "computador_lento": "O computador está apresentando lentidão?",

    "travamentos_frequentes": "O computador apresenta travamentos frequentes?",
    "armazenamento_quase_cheio": "O armazenamento está quase cheio?",
    "memoria_muito_utilizada": "O uso da memória está frequentemente muito elevado?",
    "inicializacao_lenta": "O computador demora muito para iniciar?",
    "problema_apos_instalacao": "O problema começou após a instalação de algum programa?",

    "sem_acesso_internet": "O computador está sem acesso à internet?",
    "outros_dispositivos_conectam": "Outros dispositivos conseguem acessar a internet na mesma rede?",
    "wifi_instavel": "A conexão Wi-Fi está instável?",
    "ethernet_funciona": "A conexão funciona normalmente utilizando cabo de rede?",
    "adaptador_rede_nao_identificado": "O sistema não consegue identificar o adaptador de rede?",

    "aplicativos_fecham_sozinhos": "Os aplicativos estão fechando inesperadamente?",
    "varios_aplicativos_afetados": "O problema acontece em vários aplicativos?",
    "mensagens_erro_sistema": "O sistema apresenta mensagens de erro?",
    "problema_apos_atualizacao": "O problema começou após uma atualização?",
}


# Cada categoria possui uma sequência de perguntas.
# Algumas perguntas dependem de respostas anteriores.

FLUXOS = {
    "inicializacao": [
        ("computador_nao_liga", None),
        ("indicadores_energia_acesos", ("computador_nao_liga", True)),
        ("sinais_sonoros_inicializacao", ("computador_nao_liga", True)),
        ("reinicia_antes_sistema", ("computador_nao_liga", False)),
    ],

    "video": [
        ("monitor_sem_sinal", None),
        ("monitor_ligado", ("monitor_sem_sinal", True)),
        ("cabos_video_conectados", ("monitor_sem_sinal", True)),
        ("outro_monitor_funciona", ("monitor_sem_sinal", True)),
        ("indicadores_energia_acesos", ("monitor_sem_sinal", True)),
    ],

    "temperatura": [
        ("temperatura_elevada", None),
        ("desligamento_sob_carga", ("temperatura_elevada", True)),
        ("ventoinha_nao_gira", ("temperatura_elevada", True)),
        ("ventoinha_ruido_anormal", ("temperatura_elevada", True)),
        ("computador_lento", ("temperatura_elevada", True)),
    ],

    "desempenho": [
        ("computador_lento", None),
        ("travamentos_frequentes", None),
        ("armazenamento_quase_cheio", ("computador_lento", True)),
        ("inicializacao_lenta", ("computador_lento", True)),
        ("problema_apos_instalacao", ("computador_lento", True)),
        ("memoria_muito_utilizada", ("travamentos_frequentes", True)),
    ],

    "conectividade": [
        ("sem_acesso_internet", None),
        ("outros_dispositivos_conectam", ("sem_acesso_internet", True)),
        ("wifi_instavel", None),
        ("ethernet_funciona", ("wifi_instavel", True)),
        ("adaptador_rede_nao_identificado", ("sem_acesso_internet", True)),
    ],

    "software": [
        ("aplicativos_fecham_sozinhos", None),
        ("varios_aplicativos_afetados", ("aplicativos_fecham_sozinhos", True)),
        ("problema_apos_atualizacao", ("aplicativos_fecham_sozinhos", True)),
        ("problema_apos_instalacao", ("aplicativos_fecham_sozinhos", True)),
        ("mensagens_erro_sistema", ("aplicativos_fecham_sozinhos", True)),
    ]
}


def obter_proxima_pergunta(categoria, respostas):
    """
    Retorna a próxima pergunta que deve ser apresentada.

    categoria: categoria escolhida pelo usuário.
    respostas: dicionário contendo os fatos já respondidos.

    Retorna None quando não existem mais perguntas aplicáveis.
    """

    if categoria not in FLUXOS:
        raise ValueError("Categoria de questionário inválida.")

    if not isinstance(respostas, dict):
        raise TypeError("As respostas devem ser fornecidas em um dicionário.")

    for fato, resposta in respostas.items():
        if fato not in PERGUNTAS:
            raise KeyError(f"Pergunta desconhecida: {fato}")

        if resposta is not True and resposta is not False:
            raise ValueError("As respostas devem ser True ou False.")

    for fato, condicao in FLUXOS[categoria]:

        # Não apresenta novamente uma pergunta respondida.
        if fato in respostas:
            continue

        # Pergunta sem condição: pode ser apresentada imediatamente.
        if condicao is None:
            return {
                "fato": fato,
                "texto": PERGUNTAS[fato]
            }

        # Pergunta condicional: verifica a resposta anterior.
        fato_anterior, valor_necessario = condicao

        if respostas.get(fato_anterior) is valor_necessario:
            return {
                "fato": fato,
                "texto": PERGUNTAS[fato]
            }

    return None
