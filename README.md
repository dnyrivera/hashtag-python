# 🐍 Python Impressionador — Learning Roadmap & Portfolio

Comprehensive repository tracking my hands-on exercises, industry projects, and progress through the **Python Impressionador** training program (Hashtag Treinamentos).

🎯 **Target Completion Date**: **December 28, 2026**  
⏳ **Total Workload**: 118 hours | 619 contents

---

## 🗺️ GitHub Milestones & Roadmap

The training program is structured into **6 Major GitHub Milestones**, designed with strategic deadlines to finish before the target date:

| Milestone | Scope & Core Topics | Target Due Date | Status |
| :--- | :--- | :---: | :---: |
| **[01 - Python Fundamentals](../../milestones)** | Logic, Variables, Conditionals, Strings, Lists, Loops (For/While), Dictionaries | **Nov 23, 2026** | 🟡 In Progress |
| **[02 - Core Python & Advanced Structures](../../milestones)** | Functions (`def`), List Comprehensions, Standard Libraries (`time`, `datetime`), Mini-Apps | **Nov 28, 2026** | ⚪ Not Started |
| **[03 - Intermediate: Data Analysis, Automations & Web](../../milestones)** | Pandas, Full ETL Project, Files/PDFs, Automated Emails, SQL, Selenium, BeautifulSoup | **Dec 07, 2026** | ⚪ Not Started |
| **[04 - Advanced: RPA, REST APIs & Dashboards](../../milestones)** | Enterprise RPA, Regex, REST APIs & JSON, Finance, Streamlit Dashboards, AI Agents | **Dec 15, 2026** | ⚪ Not Started |
| **[05 - Masterclass: Industry-Standard Projects](../../milestones)** | Enterprise Automation, Web Scraper, Data Science & ML (Airbnb Rio), OOP Architecture, Flask/Django | **Dec 23, 2026** | ⚪ Not Started |
| **[06 - Specialization, Testing & Final Certification](../../milestones)** | NumPy, Matplotlib & Seaborn DataViz, PyTest Unit Testing, Front-end (PyScript), Final Certification | **Dec 28, 2026** | ⚪ Not Started |

---

## 📂 Repository Structure

```text
hashtag-python/
├── 01_topics/        # Theoretical notebooks and fundamental concept exercises
├── 02_projects/      # Production-grade practical projects and portfolio items
├── 03_exercises/     # Standalone exercises and commented solutions
├── requirements.txt  # Python environment dependencies
└── setup_roadmap.py  # Automation script to configure GitHub Milestones and Issues
```

---

## ⚡ How Commits Advance Milestones Automatically

Every module is tracked via a dedicated **GitHub Issue** nested under its milestone.

When completing a class, project, or exercise set, include the issue reference in your commit message:

```bash
git add .
git commit -m "feat: complete project 01 automation with pyautogui (closes #1)"
git push origin main
```

> Using action keywords like `closes #ID`, `fixes #ID`, or `resolves #ID` triggers GitHub to **close the issue automatically**, advancing the Milestone progress bar toward 100%!
