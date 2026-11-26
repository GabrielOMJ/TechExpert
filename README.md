# TechExpert

Sistema especialista desenvolvido em Python para auxiliar na identificação de possíveis problemas em computadores, oferecendo diagnósticos preliminares, explicações e recomendações aos usuários.

O projeto foi desenvolvido no contexto da empresa fictícia **ByteCare Tecnologia**, com o objetivo de demonstrar a aplicação de sistemas especialistas na área de suporte técnico.

## Objetivo

Desenvolver um sistema capaz de simular o raciocínio de um especialista em informática, utilizando uma base de fatos e regras para analisar as respostas fornecidas pelo usuário e identificar possíveis problemas no computador.

## Funcionalidades

- Questionário dinâmico para identificação de problemas.
- Diagnóstico organizado por categorias.
- Identificação de possíveis falhas no computador.
- Explicação das regras aplicadas durante o diagnóstico.
- Recomendações para os problemas identificados.
- Validação das respostas fornecidas pelo usuário.

### Categorias de diagnóstico

O sistema contempla seis categorias:

1. Inicialização;
2. Vídeo e imagem;
3. Temperatura;
4. Desempenho;
5. Conectividade;
6. Software.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Flask:** desenvolvimento da aplicação web.
- **HTML:** estrutura das páginas.
- **CSS:** estilização da interface.

## Sistema especialista

O TechExpert utiliza o método de **encadeamento para frente (Forward Chaining)**, no qual os fatos conhecidos são analisados pelas regras da base de conhecimento para produzir novas conclusões.

A base de conhecimento contém:

- 28 fatos iniciais;
- 29 fatos inferidos;
- 30 regras de diagnóstico.

Durante o processo, o sistema identifica quais regras foram aplicadas e apresenta explicações para os resultados obtidos, permitindo que o usuário compreenda o raciocínio utilizado.

## Estrutura do projeto

```text
TechExpert/
│
├── sistema_especialista/
│   ├── fatos.py
│   ├── regras.py
│   ├── motor_inferencia.py
│   ├── explicacao.py
│   └── questionario.py
│
├── static/
│   └── ...
│
├── templates/
│   └── ...
│
├── tests/
│   └── ...
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/GabrielOMJ/TechExpert.git
```

### 2. Acessar a pasta do projeto

```bash
cd TechExpert
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python app.py
```

Após iniciar a aplicação, acesse o endereço abaixo no navegador:

```text
http://127.0.0.1:5000
```

## Testes

O projeto passou por uma etapa de validação para verificar o funcionamento das funcionalidades implementadas.

Foram realizados **18 testes**, todos aprovados, sem apresentar erros durante a execução.

## Contexto empresarial

O sistema foi desenvolvido considerando a empresa fictícia **ByteCare Tecnologia**, que oferece serviços de suporte e assistência técnica em informática.

O TechExpert representa uma ferramenta de apoio ao atendimento, auxiliando na identificação inicial de problemas e fornecendo orientações que podem facilitar o processo de suporte técnico.

## Observações

O TechExpert foi desenvolvido como projeto acadêmico, com finalidade educacional e demonstrativa. Os diagnósticos apresentados são preliminares e não substituem uma avaliação técnica profissional.

---

Desenvolvido como projeto acadêmico.