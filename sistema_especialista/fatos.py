"""
Responsavel pela definicao e organizacao dos fatos
utilizados pelo sistema.
"""

# Categorias de problemas
CATEGORIAS = {
    "inicializacao": "Problemas de inicializacao",
    "video": "Problemas de video e imagem",
    "temperatura": "Problemas de temperatura",
    "desempenho": "Problemas de desempenho",
    "conectividade": "Problemas de conectividade",
    "software": "Problemas de software"
}


# Fatos coletados diretamente do usuario
FATOS_INICIAIS = {
    # C01 - Inicializacao
    "computador_nao_liga": "O computador nao liga.",
    "indicadores_energia_acesos": "Existem indicadores de energia acesos.",
    "ventoinhas_girando": "As ventoinhas estao funcionando.",
    "sinais_sonoros_inicializacao": "Existem sinais sonoros na inicializacao.",
    "reinicia_antes_sistema": "O computador reinicia antes de carregar o sistema.",

    # C02 - Video e imagem
    "monitor_ligado": "O monitor esta ligado.",
    "monitor_sem_sinal": "O monitor apresenta ausencia de sinal.",
    "cabos_video_conectados": "Os cabos de video estao conectados.",
    "outro_monitor_funciona": "Outro monitor funciona normalmente.",

    # C03 - Temperatura
    "temperatura_elevada": "O computador apresenta temperatura elevada.",
    "ventoinha_ruido_anormal": "A ventoinha apresenta ruidos anormais.",
    "ventoinha_nao_gira": "A ventoinha nao esta girando.",
    "desligamento_sob_carga": "O computador desliga durante atividades exigentes.",

    # C04 - Desempenho
    "computador_lento": "O computador apresenta lentidao.",
    "travamentos_frequentes": "O computador apresenta travamentos frequentes.",
    "inicializacao_lenta": "O sistema demora para iniciar.",
    "armazenamento_quase_cheio": "O armazenamento esta quase cheio.",
    "memoria_muito_utilizada": "A memoria esta sendo muito utilizada.",

    # C05 - Conectividade
    "sem_acesso_internet": "O computador nao consegue acessar a internet.",
    "wifi_instavel": "A conexao Wi-Fi apresenta instabilidade.",
    "outros_dispositivos_conectam": "Outros dispositivos conseguem acessar a internet.",
    "ethernet_funciona": "A conexao Ethernet funciona normalmente.",
    "adaptador_rede_nao_identificado": "O adaptador de rede nao foi identificado.",

    # C06 - Software
    "aplicativos_fecham_sozinhos": "Aplicativos fecham inesperadamente.",
    "mensagens_erro_sistema": "O sistema apresenta mensagens de erro.",
    "problema_apos_atualizacao": "O problema comecou apos uma atualizacao.",
    "problema_apos_instalacao": "O problema comecou apos instalar um programa.",
    "varios_aplicativos_afetados": "O problema afeta varios aplicativos."
}


# Fatos que poderao ser produzidos pelo motor de inferencia
FATOS_INFERIDOS = {
    "possivel_falha_alimentacao": "Possivel falha na alimentacao eletrica.",
    "possivel_falha_inicializacao": "Possivel falha na inicializacao.",
    "possivel_instabilidade_inicializacao": "Possivel instabilidade na inicializacao.",
    "necessita_avaliacao_hardware": "Necessidade de avaliacao de hardware.",
    "possivel_falha_saida_video": "Possivel falha na saida de video.",
    "possivel_problema_monitor": "Possivel problema no monitor.",
    "necessita_verificar_video": "Necessidade de verificar conexoes de video.",
    "possivel_problema_video_computador": "Possivel problema de video no computador.",
    "possivel_superaquecimento": "Possivel superaquecimento.",
    "possivel_falha_ventilacao": "Possivel falha no sistema de ventilacao.",
    "possivel_problema_refrigeracao": "Possivel problema no sistema de refrigeracao.",
    "necessita_avaliacao_termica": "Necessidade de avaliacao termica.",
    "possivel_falta_armazenamento": "Possivel falta de espaco de armazenamento.",
    "possivel_limitacao_memoria": "Possivel limitacao de memoria.",
    "possivel_problema_desempenho": "Possivel problema de desempenho.",
    "possivel_impacto_software": "Possivel impacto de software.",
    "necessita_investigacao_desempenho": "Necessidade de investigar o desempenho.",
    "possivel_problema_rede_computador": "Possivel problema de rede no computador.",
    "possivel_problema_wifi": "Possivel problema na conexao Wi-Fi.",
    "possivel_problema_adaptador": "Possivel problema no adaptador de rede.",
    "possivel_problema_rede_local": "Possivel problema na rede local ou no provedor.",
    "possivel_problema_wifi_computador": "Possivel problema de Wi-Fi no computador.",
    "possivel_instabilidade_software": "Possivel instabilidade de software.",
    "possivel_problema_atualizacao": "Possivel problema relacionado a atualizacao.",
    "possivel_incompatibilidade_programa": "Possivel incompatibilidade de programa.",
    "possivel_instabilidade_sistema": "Possivel instabilidade do sistema operacional.",
    "possivel_incompatibilidade_atualizacao": "Possivel incompatibilidade apos atualizacao.",
    "necessita_investigacao_atualizacao": "Necessidade de investigar uma atualizacao.",
    "necessita_avaliacao_refrigeracao": "Necessidade de avaliar o sistema de refrigeracao."
}


# Cria uma base contendo todos os fatos.
# None representa uma informacao ainda desconhecida.
def criar_base_fatos():
    base = {}

    for identificador in FATOS_INICIAIS:
        base[identificador] = None

    for identificador in FATOS_INFERIDOS:
        base[identificador] = None

    return base


# Registra uma resposta fornecida pelo usuario.
# Apenas fatos iniciais podem ser alterados diretamente.
def registrar_resposta(base, identificador, valor):

    if identificador not in FATOS_INICIAIS:
        raise KeyError(
            f"Fato inicial inexistente: {identificador}"
        )

    if valor is not None and not isinstance(valor, bool):
        raise TypeError(
            "A resposta deve ser True, False ou None."
        )

    base[identificador] = valor

    return base


# Retorna a descricao de um fato.
def obter_descricao(identificador):

    if identificador in FATOS_INICIAIS:
        return FATOS_INICIAIS[identificador]

    if identificador in FATOS_INFERIDOS:
        return FATOS_INFERIDOS[identificador]

    return "Descricao nao encontrada."