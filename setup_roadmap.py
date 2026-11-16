#!/usr/bin/env python3
"""
Script para gerar automaticamente todos os Milestones, Labels e Issues
no seu repositório GitHub usando o GitHub CLI (`gh`).
Cronograma planejado: 17/11/2026 a 28/12/2026.
"""

import subprocess
import json
import sys

# Definição dos 6 Grandes Milestones com metas até 28/12/2026
MILESTONES = [
    {
        "title": "01 - Fundamentos do Python",
        "description": "Base essencial: Lógica, Variáveis, Condicionais, Strings, Listas, Loops (For/While), Tuplas e Dicionários.",
        "due_date": "2026-11-23T23:59:59Z"
    },
    {
        "title": "02 - Básico & Estruturas Avançadas",
        "description": "Funções completas, List Comprehension, Bibliotecas essenciais (time, datetime) e desafios práticos.",
        "due_date": "2026-11-28T23:59:59Z"
    },
    {
        "title": "03 - Intermediário: Dados, Automações e Web",
        "description": "Pandas, Projeto ETL completo, Manipulação de Arquivos e PDFs, E-mails, Banco de Dados (SQL), Selenium e BeautifulSoup.",
        "due_date": "2026-12-07T23:59:59Z"
    },
    {
        "title": "04 - Avançado: RPA, APIs & Dashboards",
        "description": "RPA de Processos, Expressões Regulares (Regex), Integração com APIs e JSON, Mercado Financeiro, Executáveis (.exe), Streamlit e Agentes IA.",
        "due_date": "2026-12-15T23:59:59Z"
    },
    {
        "title": "05 - Impressionador: Projetos de Mercado",
        "description": "Grandes Projetos Comerciais: Automação Empresarial, Web Scraping de Preços, Data Science & Machine Learning (Airbnb Rio), POO Completo, Web (Flask/Django), Tkinter e Jogos.",
        "due_date": "2026-12-23T23:59:59Z"
    },
    {
        "title": "06 - Especialização, Testes & Finalização",
        "description": "NumPy, Matplotlib & Seaborn para DataViz, Testes com PyTest, Front-end com PyScript e Finalização do Curso.",
        "due_date": "2026-12-28T23:59:59Z"
    }
]

# Issues estruturadas com checklists detalhados por módulo
ISSUES = [
    # --- MILESTONE 1 ---
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M01 a M04: Primeiros Programas e 1º Projeto Prático (Automação)",
        "labels": ["fundamentos", "projeto"],
        "body": """### Objetivo
Dominar a configuração inicial, introdução e o 1º projeto prático integrando automação com PyAutoGUI e análise de dados.

### Checklist de Aulas e Tarefas
- [x] Configuração de ambiente e VS Code
- [x] 1º Projeto: Automação + Análise de Dados
- [x] Automação com PyAutoGUI (cliques, teclado e navegação)
- [ ] Leitura da base de dados e cálculo de indicadores com Pandas
- [ ] Envio automático de e-mail com relatório de vendas
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M05: Mais sobre Variáveis e Estruturas Sequenciais",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Consolidar tipos de dados, formatação de textos modernos e manipulação de variáveis.

### Checklist de Aulas e Tarefas
- [x] Tipos de variáveis e conversões (casting)
- [x] Formatação com `.format()` e f-strings
- [x] Lista de Exercícios - Estruturas Sequenciais
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M06: If - Estruturas Condicionais em Python",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Dominar tomada de decisão com `if`, `elif`, `else` e operadores lógicos.

### Checklist de Aulas e Tarefas
- [x] Estrutura do if, blocos e indentação
- [x] Operadores de comparação e lógicos (`and`, `or`)
- [x] Exercícios If (Parte 1 e 2)
- [ ] Lista de Exercícios - Estruturas de Decisão
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M07: Strings - Manipulação e Métodos",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Trabalhar com índices, fatiamento (slicing) e métodos nativos de texto.

### Checklist de Aulas e Tarefas
- [ ] Índices positivos e negativos, fatiamento de strings
- [ ] Métodos úteis (`strip`, `replace`, `find`, `split`, etc.)
- [ ] Formatação de valores numéricos e moedas
- [ ] Exercícios Práticos de Strings (Parte 1 e 2)
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M08: Listas em Python - Métodos e Usos",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Trabalhar com coleções ordenadas, mutabilidade e listas aninhadas.

### Checklist de Aulas e Tarefas
- [ ] Adicionar/remover itens (`append`, `extend`, `pop`, `remove`)
- [ ] Ordenação (`sort`, `sorted`) e busca (`index`, `in`)
- [ ] Cópia rasa vs cópia profunda de listas
- [ ] Lista de listas (matrizes)
- [ ] Exercícios de Listas (Parte 1 e 2)
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M09 e M10: Estruturas de Repetição (For e While)",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Dominar loops finitos e condicionais em coleções.

### Checklist de Aulas e Tarefas
- [ ] For each e `enumerate` (índice + elemento)
- [ ] Loops aninhados (for dentro de for)
- [ ] Controle de fluxo com `break` e `continue`
- [ ] Estrutura `while` e prevenção de loops infinitos
- [ ] Lista de Exercícios de Repetição
"""
    },
    {
        "milestone": "01 - Fundamentos do Python",
        "title": "M11 a M13: Tuplas, Dicionários e Iterables",
        "labels": ["fundamentos"],
        "body": """### Objetivo
Compreender estruturas de chave-valor (`dict`), imutabilidade (`tuple`) e tipos iteráveis (`set`, `range`).

### Checklist de Aulas e Tarefas
- [ ] Tuplas e Unpacking de variáveis
- [ ] Dicionários: métodos `keys()`, `values()`, `items()`
- [ ] Manipulação e transformação de dicionários (`zip`)
- [ ] Iterables, `range` e conjuntos (`set`)
- [ ] Exercícios Práticos de Dicionários
"""
    },

    # --- MILESTONE 2 ---
    {
        "milestone": "02 - Básico & Estruturas Avançadas",
        "title": "M01: Funções em Python (def, parâmetros e retornos)",
        "labels": ["intermediario"],
        "body": """### Objetivo
Modularizar código, criar funções reutilizáveis e tratar exceções.

### Checklist de Aulas e Tarefas
- [ ] Criação de funções e retorno de múltiplos valores
- [ ] Argumentos posicionais, nomeados e valores padrão
- [ ] `*args` e `**kwargs` (múltiplos argumentos)
- [ ] Docstrings, Type Hints e tratamento de erros
- [ ] Desafios e exercícios práticos de funções
"""
    },
    {
        "milestone": "02 - Básico & Estruturas Avançadas",
        "title": "M02: List Comprehension",
        "labels": ["intermediario"],
        "body": """### Objetivo
Escrever código conciso e pythônico para filtragem e transformação de listas.

### Checklist de Aulas e Tarefas
- [ ] Sintaxe básica de List Comprehension
- [ ] Filtragem condicional com `if`
- [ ] Tratamento de casos com `if ... else` ternário
- [ ] Exercícios de List Comprehension
"""
    },
    {
        "milestone": "02 - Básico & Estruturas Avançadas",
        "title": "M04 e M05: Módulos, Bibliotecas (time, datetime) e Desafios",
        "labels": ["intermediario"],
        "body": """### Objetivo
Aprender a importar e usar bibliotecas nativas, trabalhar com datas e resolver desafios práticos.

### Checklist de Aulas e Tarefas
- [ ] Manipulação de tempo com `time`
- [ ] Datas, fusos horários e formatação com `datetime`
- [ ] Desafio prático: Cálculo de impostos e tratamento de colunas
- [ ] Mini-projetos: Analisador de texto, Gerador de senhas e Gerador de QR Code
"""
    },

    # --- MILESTONE 3 ---
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M01 e M02: Análise de Dados com Pandas e Integração Excel",
        "labels": ["dados", "projeto"],
        "body": """### Objetivo
Manipulação completa de DataFrames, limpeza, visualização e integração Excel.

### Checklist de Aulas e Tarefas
- [ ] DataFrames, Series e leitura de arquivos `.csv` e `.xlsx`
- [ ] Filtragem, agrupamentos (`groupby`) e agregação de dados
- [ ] Adicionar/remover colunas e tratamento de valores nulos
- [ ] Mini-projeto de Análise de Dados com Pandas
"""
    },
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M03: Projeto Completo de ETL com Pandas",
        "labels": ["dados", "projeto"],
        "body": """### Objetivo
Executar um pipeline completo de Extração, Transformação e Carga (ETL).

### Checklist de Aulas e Tarefas
- [ ] Carregamento, inspeção e limpeza de dados
- [ ] Feature Engineering (criação de variáveis)
- [ ] Análises por múltiplos agrupamentos e junção de bases (`merge`/`concat`)
- [ ] Análise temporal e geração de relatórios
"""
    },
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M05 e M06: Integração com Arquivos, Pastas e PDFs",
        "labels": ["automacao"],
        "body": """### Objetivo
Automatizar a gestão do sistema de arquivos e manipulação de documentos PDF.

### Checklist de Aulas e Tarefas
- [ ] Manipulação de arquivos `.txt` com context manager (`with`)
- [ ] Navegação de diretórios com `pathlib` e `shutil`
- [ ] Separação, união e extração de tabelas em PDF (`PyPDF`, `tabula`)
"""
    },
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M07: Integração com E-mail (Gmail, Outlook e SendGrid)",
        "labels": ["automacao"],
        "body": """### Objetivo
Automatizar envio e leitura de e-mails corporativos com relatórios e anexos.

### Checklist de Aulas e Tarefas
- [ ] Envio via SMTP (Gmail com senha de app)
- [ ] Envio com anexos, assinaturas e imagens embutidas
- [ ] Leitura e extração de anexos com `imap_tools`
- [ ] Automação de e-mails em massa com SendGrid
"""
    },
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M08: Integração com Bancos de Dados SQL",
        "labels": ["dados", "banco-de-dados"],
        "body": """### Objetivo
Conectar o Python a bancos de dados relacionais e executar operações CRUD.

### Checklist de Aulas e Tarefas
- [ ] Conexão com banco via `pyodbc` / SQLite / MySQL
- [ ] Operações CRUD: Create, Read, Update, Delete
- [ ] Leitura direta com `pandas.read_sql`
- [ ] Introdução ao ORM com `SQLAlchemy`
"""
    },
    {
        "milestone": "03 - Intermediário: Dados, Automações e Web",
        "title": "M09 e M10: Web Scraping com Selenium e BeautifulSoup",
        "labels": ["web", "automacao"],
        "body": """### Objetivo
Construir robôs de automação web e raspagem de dados.

### Checklist de Aulas e Tarefas
- [ ] Seletores CSS e XPath no Selenium
- [ ] Preenchimento de formulários e download automático
- [ ] Desafio: Automação de envio de mensagens no WhatsApp
- [ ] Raspagem de dados estruturados com BeautifulSoup (BS4)
"""
    },

    # --- MILESTONE 4 ---
    {
        "milestone": "04 - Avançado: RPA, APIs & Dashboards",
        "title": "M01 e M02: RPA com Python e Expressões Regulares (Regex)",
        "labels": ["avancado", "automacao"],
        "body": """### Objetivo
Construir automações robóticas corporativas (ERP/SAP) e dominar padrões de Regex.

### Checklist de Aulas e Tarefas
- [ ] RPA de processos corporativos de ponta a ponta
- [ ] Padrões de Regex, grupos e validação de textos complexos
- [ ] Desafio: Extração automatizada de dados com Regex
"""
    },
    {
        "milestone": "04 - Avançado: RPA, APIs & Dashboards",
        "title": "M03: Integração com APIs REST e JSON",
        "labels": ["avancado", "api"],
        "body": """### Objetivo
Consumir e construir APIs RESTful com Python.

### Checklist de Aulas e Tarefas
- [ ] Consumo de APIs públicas (Cotação de moedas, CEP, IBGE)
- [ ] Envio de SMS via API do Twilio
- [ ] Criação de uma API REST completa com Python
- [ ] Integração com Firebase REST API
"""
    },
    {
        "milestone": "04 - Avançado: RPA, APIs & Dashboards",
        "title": "M04 a M08: Finanças, Dashboards (Streamlit) e Agentes de IA",
        "labels": ["avancado", "dados", "ia"],
        "body": """### Objetivo
Análise quantitativa de investimentos, dashboards interativos e agentes inteligentes.

### Checklist de Aulas e Tarefas
- [ ] Carteira de investimentos, rentabilidade e matriz de risco
- [ ] Construção de Dashboards interativos com Streamlit
- [ ] Empacotamento de scripts em executáveis (`.exe`) com PyInstaller
- [ ] Agentes de IA com OpenAI, Hugging Face e LangChain
"""
    },

    # --- MILESTONE 5 ---
    {
        "milestone": "05 - Impressionador: Projetos de Mercado",
        "title": "Projeto 1: Automação Empresarial de Processo (Lojas e Indicadores)",
        "labels": ["projeto", "mercado"],
        "body": """### Objetivo
Construir o sistema completo de cálculo de faturamento, ticket médio e envio de relatórios para gerentes e diretoria.

### Checklist
- [ ] Separação e consolidação de tabelas por filial
- [ ] Cálculo de indicadores (Faturamento, Diversidade, Ticket Médio)
- [ ] Envio automático de e-mails em formato HTML com tabelas
- [ ] Geração de rankings diários e anuais
"""
    },
    {
        "milestone": "05 - Impressionador: Projetos de Mercado",
        "title": "Projeto 2: Automação Web Comercial (Comparador de Preços)",
        "labels": ["projeto", "mercado", "web"],
        "body": """### Objetivo
Robô de busca e comparação de preços em múltiplos e-commerces com paginação.

### Checklist
- [ ] Scraping dinâmico em múltiplos sites de compras
- [ ] Comparação inteligente de correspondência de produtos
- [ ] Envio de alertas de ofertas encontradas
"""
    },
    {
        "milestone": "05 - Impressionador: Projetos de Mercado",
        "title": "Projeto 3: Ciência de Dados & Machine Learning (Airbnb Rio de Janeiro)",
        "labels": ["projeto", "machine-learning", "dados"],
        "body": """### Objetivo
Pipeline completo de Data Science para prever preços de diárias do Airbnb.

### Checklist
- [ ] Extração e consolidação de bases de dados massivas
- [ ] Limpeza, tratamento de nulos e remoção de outliers estatísticos
- [ ] Análise exploratória com Seaborn e visualizações geoespaciais
- [ ] Encoding de variáveis categóricas
- [ ] Treinamento e comparação de modelos preditivos
- [ ] Deploy do modelo com interface de usuário
"""
    },
    {
        "milestone": "05 - Impressionador: Projetos de Mercado",
        "title": "Projeto 4: Programação Orientada a Objetos (POO) Completa",
        "labels": ["poo", "projeto"],
        "body": """### Objetivo
Construir arquitetura de software profissional com Classes, Métodos e Herança.

### Checklist
- [ ] Criação de classes, atributos e construtores (`__init__`)
- [ ] Encapsulamento, atributos privados e métodos de classe
- [ ] Herança e Polimorfismo (Sistema Bancário de Contas e Agências)
"""
    },
    {
        "milestone": "05 - Impressionador: Projetos de Mercado",
        "title": "Projetos 5 a 8: Desenvolvimento Web, Tkinter e Jogos",
        "labels": ["projeto", "interface", "web"],
        "body": """### Objetivo
Criar interfaces gráficas com Tkinter, aplicações Web (Flask/Django) e desenvolvimento de jogos com Pygame.

### Checklist
- [ ] Interface desktop interativa com Tkinter (Cotações e CRUD de estoque)
- [ ] Criação de Jogo interativo estilo Flappy Bird (Pygame)
- [ ] Fundamentos de Web Apps com Flask e Django
"""
    },

    # --- MILESTONE 6 ---
    {
        "milestone": "06 - Especialização, Testes & Finalização",
        "title": "Especialização: NumPy, Matplotlib, Seaborn e PyTest",
        "labels": ["especializacao"],
        "body": """### Objetivo
Aprofundar em computação numérica com NumPy, visualizações profissionais com Matplotlib/Seaborn e testes unitários com PyTest.

### Checklist
- [ ] Arrays multidimensionais e operações vetorizadas com NumPy
- [ ] Anatomia de gráficos customizados e estilos com Matplotlib
- [ ] Gráficos estatísticos avançados com Seaborn
- [ ] Criação de suíte de testes automatizados com PyTest
- [ ] Conclusão de 100% do curso e emissão de certificado
"""
    }
]

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result

def main():
    print("=" * 60)
    print("🚀 Iniciando configuração do Roadmap no GitHub...")
    print("=" * 60)

    # 1. Verificar se gh está autenticado
    auth_check = run("gh auth status")
    if auth_check.returncode != 0:
        print("\n❌ Atenção: O GitHub CLI (gh) precisa estar autenticado.")
        print("Execute no seu terminal: gh auth login\n")
        sys.exit(1)

    # 2. Criar Labels personalizadas
    print("\n🏷️  Criando Labels...")
    labels = [
        ("fundamentos", "0E8A16", "Módulos de Fundamentos"),
        ("intermediario", "1D76DB", "Módulos de Nível Intermediário"),
        ("avancado", "5319E7", "Módulos de Nível Avançado"),
        ("projeto", "D93F0B", "Projetos práticos e portfólio"),
        ("dados", "0052CC", "Análise de Dados, Pandas e ETL"),
        ("automacao", "FBCA04", "RPA, PyAutoGUI e Scripts"),
        ("web", "B60205", "Web Scraping e Selenium"),
        ("machine-learning", "006B75", "Ciência de Dados e Modelos Preditivos"),
        ("api", "D4C5F9", "APIs REST e Integrações"),
        ("poo", "C2E0C6", "Orientação a Objetos"),
        ("especializacao", "E99695", "NumPy, Testes e Extras")
    ]
    for name, color, desc in labels:
        run(f'gh label create "{name}" --color "{color}" --description "{desc}" --force')

    # 3. Criar Milestones
    print("\n🎯 Criando Milestones...")
    milestone_map = {}
    for m in MILESTONES:
        cmd = f'gh api repos/:owner/:repo/milestones -f title="{m["title"]}" -f description="{m["description"]}" -f due_on="{m["due_date"]}"'
        res = run(cmd)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            milestone_map[m["title"]] = data.get("number")
            print(f"  ✅ Milestone criado: {m['title']} (Due: {m['due_date'][:10]})")
        else:
            # Se já existir, obter lista de milestones
            print(f"  ℹ️  Milestone já existe ou foi recuperado: {m['title']}")

    # Atualizar mapa de milestones
    res_list = run("gh api repos/:owner/:repo/milestones")
    if res_list.returncode == 0:
        for item in json.loads(res_list.stdout):
            milestone_map[item["title"]] = item["number"]

    # 4. Criar Issues
    print("\n📝 Criando Issues vinculadas aos Milestones...")
    for issue in ISSUES:
        m_title = issue["milestone"]
        m_number = milestone_map.get(m_title)
        
        labels_arg = " ".join([f'--label "{lbl}"' for lbl in issue["labels"]])
        m_arg = f'--milestone "{m_number}"' if m_number else f'--milestone "{m_title}"'
        
        # Salva o body temporário
        with open("/tmp/issue_body.md", "w") as f:
            f.write(issue["body"])
            
        cmd = f'gh issue create --title "{issue["title"]}" --body-file "/tmp/issue_body.md" {labels_arg} {m_arg}'
        res = run(cmd)
        if res.returncode == 0:
            print(f"  ✅ Issue criada: {issue['title']}")
        else:
            print(f"  ⚠️  Erro ao criar issue: {issue['title']} ({res.stderr.strip()})")

    print("\n" + "=" * 60)
    print("🎉 Parabéns! Todos os Milestones e Issues foram configurados com sucesso.")
    print("Meta final do treinamento: 28/12/2026 🏁")
    print("=" * 60)

if __name__ == "__main__":
    main()
