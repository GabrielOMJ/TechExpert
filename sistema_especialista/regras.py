
"""
Responsavel pelo armazenamento das regras de conhecimento
utilizadas pelo sistema especialista.
"""

from .fatos import FATOS_INICIAIS, FATOS_INFERIDOS


# Funcao auxiliar para padronizar a criacao das regras.
def criar_regra(
    identificador,
    categoria,
    condicoes,
    conclusao,
    explicacao,
    recomendacao
):
    return {
        "id": identificador,
        "categoria": categoria,
        "condicoes": condicoes,
        "conclusao": conclusao,
        "explicacao": explicacao,
        "recomendacao": recomendacao
    }


# Base de conhecimento: 30 regras
REGRAS = [

    # ==========================================
    # C01 - PROBLEMAS DE INICIALIZACAO
    # ==========================================

    criar_regra(
        "R01", "inicializacao",
        {
            "computador_nao_liga": True,
            "indicadores_energia_acesos": False
        },
        "possivel_falha_alimentacao",
        "O computador nao liga e nao apresenta indicadores de energia.",
        "Encaminhar o equipamento para avaliacao da alimentacao eletrica."
    ),

    criar_regra(
        "R02", "inicializacao",
        {
            "computador_nao_liga": True,
            "indicadores_energia_acesos": True
        },
        "possivel_falha_inicializacao",
        "O computador apresenta indicadores de energia, mas nao inicia normalmente.",
        "Recomendar avaliacao tecnica do processo de inicializacao."
    ),

    criar_regra(
        "R03", "inicializacao",
        {
            "reinicia_antes_sistema": True
        },
        "possivel_instabilidade_inicializacao",
        "O computador reinicia antes de carregar o sistema operacional.",
        "Investigar possiveis problemas de hardware ou software durante a inicializacao."
    ),

    criar_regra(
        "R04", "inicializacao",
        {
            "computador_nao_liga": True,
            "sinais_sonoros_inicializacao": True
        },
        "necessita_avaliacao_hardware",
        "O computador nao inicia e apresenta sinais sonoros durante a inicializacao.",
        "Encaminhar para avaliacao tecnica dos componentes de hardware."
    ),

    # ==========================================
    # C02 - PROBLEMAS DE VIDEO E IMAGEM
    # ==========================================

    criar_regra(
        "R05", "video",
        {
            "monitor_sem_sinal": True,
            "indicadores_energia_acesos": True
        },
        "possivel_falha_saida_video",
        "O computador apresenta sinais de energia, mas o monitor nao recebe imagem.",
        "Solicitar verificacao das conexoes e da saida de video."
    ),

    criar_regra(
        "R06", "video",
        {
            "monitor_sem_sinal": True,
            "outro_monitor_funciona": True
        },
        "possivel_problema_monitor",
        "Outro monitor funciona normalmente, indicando uma possivel falha no monitor original.",
        "Recomendar avaliacao do monitor original e de suas conexoes."
    ),

    criar_regra(
        "R07", "video",
        {
            "monitor_sem_sinal": True,
            "cabos_video_conectados": False
        },
        "necessita_verificar_video",
        "O monitor apresenta ausencia de sinal e os cabos de video nao estao conectados corretamente.",
        "Verificar as conexoes de video antes de solicitar uma manutencao."
    ),

    criar_regra(
        "R08", "video",
        {
            "monitor_sem_sinal": True,
            "cabos_video_conectados": True,
            "outro_monitor_funciona": False
        },
        "possivel_problema_video_computador",
        "Diferentes monitores nao apresentam imagem, mesmo com os cabos conectados.",
        "Encaminhar para avaliacao da saida de video e dos componentes relacionados."
    ),

    # ==========================================
    # C03 - PROBLEMAS DE TEMPERATURA
    # ==========================================

    criar_regra(
        "R09", "temperatura",
        {
            "temperatura_elevada": True,
            "desligamento_sob_carga": True
        },
        "possivel_superaquecimento",
        "A temperatura elevada associada a desligamentos durante atividades exigentes pode indicar superaquecimento.",
        "Recomendar avaliacao do sistema de refrigeracao."
    ),

    criar_regra(
        "R10", "temperatura",
        {
            "temperatura_elevada": True,
            "ventoinha_nao_gira": True
        },
        "possivel_falha_ventilacao",
        "A temperatura elevada associada a uma ventoinha sem funcionamento pode indicar falha de ventilacao.",
        "Encaminhar para avaliacao tecnica das ventoinhas."
    ),

    criar_regra(
        "R11", "temperatura",
        {
            "temperatura_elevada": True,
            "ventoinha_ruido_anormal": True
        },
        "possivel_problema_refrigeracao",
        "A temperatura elevada e os ruidos anormais podem indicar problemas no sistema de refrigeracao.",
        "Recomendar inspecao tecnica do sistema de refrigeracao."
    ),

    criar_regra(
        "R12", "temperatura",
        {
            "temperatura_elevada": True,
            "computador_lento": True
        },
        "necessita_avaliacao_termica",
        "A temperatura elevada acompanhada de lentidao pode indicar impacto termico no desempenho.",
        "Recomendar verificacao das condicoes termicas do equipamento."
    ),

    # ==========================================
    # C04 - PROBLEMAS DE DESEMPENHO
    # ==========================================

    criar_regra(
        "R13", "desempenho",
        {
            "computador_lento": True,
            "armazenamento_quase_cheio": True
        },
        "possivel_falta_armazenamento",
        "A lentidao associada ao armazenamento quase cheio pode indicar falta de espaco disponivel.",
        "Verificar o armazenamento e avaliar a necessidade de liberar espaco."
    ),

    criar_regra(
        "R14", "desempenho",
        {
            "travamentos_frequentes": True,
            "memoria_muito_utilizada": True
        },
        "possivel_limitacao_memoria",
        "Os travamentos frequentes associados a elevada utilizacao de memoria podem indicar limitacao de recursos.",
        "Recomendar avaliacao da utilizacao de memoria e dos programas em execucao."
    ),

    criar_regra(
        "R15", "desempenho",
        {
            "computador_lento": True,
            "inicializacao_lenta": True
        },
        "possivel_problema_desempenho",
        "A lentidao geral e a inicializacao demorada indicam possiveis problemas de desempenho.",
        "Investigar os processos de inicializacao e os recursos utilizados."
    ),

    criar_regra(
        "R16", "desempenho",
        {
            "computador_lento": True,
            "problema_apos_instalacao": True
        },
        "possivel_impacto_software",
        "A lentidao comecou apos a instalacao de um programa.",
        "Investigar o programa instalado e sua compatibilidade com o sistema."
    ),

    criar_regra(
        "R17", "desempenho",
        {
            "travamentos_frequentes": True,
            "inicializacao_lenta": True
        },
        "necessita_investigacao_desempenho",
        "Os travamentos frequentes e a inicializacao lenta indicam necessidade de investigacao do desempenho.",
        "Recomendar avaliacao dos recursos e do estado geral do sistema."
    ),

    # ==========================================
    # C05 - PROBLEMAS DE CONECTIVIDADE
    # ==========================================

    criar_regra(
        "R18", "conectividade",
        {
            "sem_acesso_internet": True,
            "outros_dispositivos_conectam": True
        },
        "possivel_problema_rede_computador",
        "Outros dispositivos acessam a internet normalmente, mas o computador analisado nao consegue conectar.",
        "Investigar as configuracoes de rede do computador."
    ),

    criar_regra(
        "R19", "conectividade",
        {
            "wifi_instavel": True,
            "ethernet_funciona": True
        },
        "possivel_problema_wifi",
        "A conexao Ethernet funciona, mas a conexao Wi-Fi apresenta instabilidade.",
        "Recomendar avaliacao do adaptador Wi-Fi e das configuracoes da conexao sem fio."
    ),

    criar_regra(
        "R20", "conectividade",
        {
            "adaptador_rede_nao_identificado": True
        },
        "possivel_problema_adaptador",
        "O adaptador de rede nao esta sendo identificado pelo sistema operacional.",
        "Encaminhar para verificacao do adaptador e dos respectivos drivers."
    ),

    criar_regra(
        "R21", "conectividade",
        {
            "sem_acesso_internet": True,
            "outros_dispositivos_conectam": False
        },
        "possivel_problema_rede_local",
        "Nenhum dos dispositivos analisados consegue acessar a internet.",
        "Verificar o roteador, a rede local e a disponibilidade do provedor."
    ),

    criar_regra(
        "R22", "conectividade",
        {
            "wifi_instavel": True,
            "outros_dispositivos_conectam": True
        },
        "possivel_problema_wifi_computador",
        "Outros dispositivos conectam normalmente, enquanto o Wi-Fi do computador apresenta instabilidade.",
        "Investigar o adaptador sem fio e as configuracoes de rede do computador."
    ),

    # ==========================================
    # C06 - PROBLEMAS DE SOFTWARE
    # ==========================================

    criar_regra(
        "R23", "software",
        {
            "aplicativos_fecham_sozinhos": True,
            "varios_aplicativos_afetados": True
        },
        "possivel_instabilidade_software",
        "Diferentes aplicativos estao fechando inesperadamente.",
        "Recomendar investigacao do ambiente de software do computador."
    ),

    criar_regra(
        "R24", "software",
        {
            "mensagens_erro_sistema": True,
            "problema_apos_atualizacao": True
        },
        "possivel_problema_atualizacao",
        "Os erros do sistema comecaram apos uma atualizacao.",
        "Investigar possiveis incompatibilidades ou falhas relacionadas a atualizacao."
    ),

    criar_regra(
        "R25", "software",
        {
            "problema_apos_instalacao": True,
            "aplicativos_fecham_sozinhos": True
        },
        "possivel_incompatibilidade_programa",
        "Os aplicativos apresentam falhas apos a instalacao de um programa.",
        "Investigar possiveis incompatibilidades entre os programas instalados."
    ),

    criar_regra(
        "R26", "software",
        {
            "mensagens_erro_sistema": True,
            "varios_aplicativos_afetados": True
        },
        "possivel_instabilidade_sistema",
        "As mensagens de erro e os problemas em diferentes aplicativos podem indicar instabilidade do sistema operacional.",
        "Recomendar avaliacao do sistema operacional."
    ),

    criar_regra(
        "R27", "software",
        {
            "aplicativos_fecham_sozinhos": True,
            "problema_apos_atualizacao": True
        },
        "possivel_incompatibilidade_atualizacao",
        "Os aplicativos passaram a fechar inesperadamente apos uma atualizacao.",
        "Investigar a compatibilidade da atualizacao com os aplicativos."
    ),

    # ==========================================
    # REGRAS COMPLEMENTARES
    # ==========================================

    criar_regra(
        "R28", "desempenho",
        {
            "computador_lento": True,
            "travamentos_frequentes": True
        },
        "necessita_investigacao_desempenho",
        "A lentidao acompanhada de travamentos frequentes indica necessidade de investigacao.",
        "Recomendar avaliacao dos componentes e recursos utilizados."
    ),

    criar_regra(
        "R29", "software",
        {
            "problema_apos_atualizacao": True,
            "mensagens_erro_sistema": True,
            "varios_aplicativos_afetados": True
        },
        "necessita_investigacao_atualizacao",
        "Diferentes aplicativos apresentam problemas e mensagens de erro apos uma atualizacao.",
        "Recomendar investigacao tecnica da atualizacao realizada."
    ),

    criar_regra(
        "R30", "temperatura",
        {
            "possivel_superaquecimento": True,
            "ventoinha_nao_gira": True
        },
        "necessita_avaliacao_refrigeracao",
        "O superaquecimento identificado e a ausencia de funcionamento da ventoinha indicam necessidade de avaliacao do sistema de refrigeracao.",
        "Encaminhar o equipamento para avaliacao tecnica do sistema de refrigeracao."
    )
]


# Retorna todas as regras de uma categoria.
def obter_regras_categoria(categoria):
    return [
        regra for regra in REGRAS
        if regra["categoria"] == categoria
    ]


# Verifica se uma regra possui todos os fatos necessarios.
def validar_base_regras():

    identificadores = set()

    for regra in REGRAS:

        if regra["id"] in identificadores:
            return False, f"Identificador duplicado: {regra['id']}"

        identificadores.add(regra["id"])

        if not regra["condicoes"]:
            return False, f"Regra sem condicoes: {regra['id']}"

        if regra["conclusao"] not in FATOS_INFERIDOS:
            return False, f"Conclusao inexistente: {regra['id']}"

        for fato in regra["condicoes"]:

            if fato not in FATOS_INICIAIS and fato not in FATOS_INFERIDOS:
                return False, f"Fato inexistente na regra {regra['id']}: {fato}"

            if not isinstance(regra["condicoes"][fato], bool):
                return False, f"Condicao invalida na regra {regra['id']}"

    return True, "Base de conhecimento validada com sucesso."


# Retorna a quantidade de regras cadastradas.
def quantidade_regras():
    return len(REGRAS)
