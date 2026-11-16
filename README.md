# 🐍 Python Impressionador — Jornada de Aprendizado & Portfólio

Repositório dedicado ao acompanhamento, projetos práticos e exercícios do curso **Python Impressionador** (Hashtag Treinamentos).

🎯 **Meta de Conclusão**: **28 de Dezembro de 2026**  
⏳ **Carga Horária Total**: 118 horas | 619 conteúdos

---

## 🗺️ Roadmap de Milestones & Prazos

O curso está dividido em **6 Grandes Milestones no GitHub**, distribuídos estrategicamente para conclusão até o prazo final:

| Milestone | Escopo & Conteúdo Principal | Data Limite (Due Date) | Status |
| :--- | :--- | :---: | :---: |
| **[01 - Fundamentos do Python](../../milestones)** | Lógica, Variáveis, Ifs, Strings, Listas, Loops (For/While), Dicionários | **23/11/2026** | 🟡 Em Progresso |
| **[02 - Básico & Estruturas Avançadas](../../milestones)** | Funções (`def`), List Comprehension, `time`, `datetime`, Mini-projetos | **28/11/2026** | ⚪ Não iniciado |
| **[03 - Intermediário: Dados & Web](../../milestones)** | Pandas, Projeto ETL, Arquivos/PDF, E-mails, SQL, Selenium, BeautifulSoup | **07/12/2026** | ⚪ Não iniciado |
| **[04 - Avançado: RPA, APIs & Dashboards](../../milestones)** | RPA de Processos, Regex, APIs REST/JSON, Finanças, Streamlit, Agentes IA | **15/12/2026** | ⚪ Não iniciado |
| **[05 - Impressionador: Projetos de Mercado](../../milestones)** | Automação Empresarial, Web Scraping, Data Science (Airbnb + ML), POO, Flask/Django | **23/12/2026** | ⚪ Não iniciado |
| **[06 - Especialização, Testes & Finalização](../../milestones)** | NumPy, Matplotlib/Seaborn, PyTest, Front-end (PyScript), Conclusão | **28/12/2026** | ⚪ Não iniciado |

---

## 📂 Estrutura do Repositório

```text
hashtag-python/
├── 01_topics/        # Cadernos de teoria e conceitos fundamentais
├── 02_projects/      # Projetos práticos completos aplicados ao mercado
├── 03_exercises/     # Listas de exercícios e gabaritos comentados
├── requirements.txt  # Dependências do ambiente Python
└── setup_roadmap.py  # Script de automação de Milestones e Issues no GitHub
```

---

## ⚡ Como Vincular Commits aos Milestones

Cada módulo possui uma **Issue** correspondente dentro do seu respectivo Milestone.

Ao concluir uma aula, projeto ou lista de exercícios:

```bash
git add .
git commit -m "feat: concluindo projeto de automacao com pyautogui (closes #1)"
git push origin main
```

> Usando palavras-chave como `closes #ID`, `fixes #ID` ou `resolves #ID`, o GitHub **fecha a issue automaticamente** e faz a barra de progresso do Milestone subir até os 100%!
