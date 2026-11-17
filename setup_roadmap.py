#!/usr/bin/env python3
"""
Automatically generates all Milestones, Labels, and Issues
in your GitHub repository using the GitHub CLI (`gh`).
Timeline: November 17, 2026 to December 28, 2026.
"""

import json
import subprocess
import sys

# Definition of the 6 Major Milestones targeted for completion before Dec 28, 2026
MILESTONES = [
    {
        "title": "01 - Python Fundamentals",
        "description": "Core foundation: Logic, Variables, Conditionals, Strings, Lists, Loops (For/While), Tuples, and Dictionaries.",
        "due_date": "2026-11-23T23:59:59Z"
    },
    {
        "title": "02 - Core Python & Advanced Structures",
        "description": "Functions, List Comprehension, Essential Standard Libraries (time, datetime), and practical coding challenges.",
        "due_date": "2026-11-28T23:59:59Z"
    },
    {
        "title": "03 - Intermediate: Data Analysis, Automations & Web",
        "description": "Pandas, Full ETL Project, File & PDF Handling, Automated Emails, SQL Databases, Selenium, and BeautifulSoup.",
        "due_date": "2026-12-07T23:59:59Z"
    },
    {
        "title": "04 - Advanced: RPA, REST APIs & Dashboards",
        "description": "Process RPA, Regular Expressions (Regex), REST APIs & JSON, Financial Markets, Executables (.exe), Streamlit Dashboards, and AI Agents.",
        "due_date": "2026-12-15T23:59:59Z"
    },
    {
        "title": "05 - Masterclass: Industry-Standard Projects",
        "description": "Production-grade projects: Business Process Automation, Web Price Scraper, Data Science & ML (Airbnb Rio), Full OOP, Web (Flask/Django), Tkinter, and Game Dev.",
        "due_date": "2026-12-23T23:59:59Z"
    },
    {
        "title": "06 - Specialization, Testing & Final Certification",
        "description": "NumPy, Matplotlib & Seaborn DataViz, Automated Unit Testing with PyTest, Front-end with PyScript, and Course Completion.",
        "due_date": "2026-12-28T23:59:59Z"
    }
]

# Structured Issues with actionable checklists
ISSUES = [
    # --- MILESTONE 1 ---
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M01 to M04: First Programs & Practical Project 01 (Automation)",
        "labels": ["fundamentals", "project"],
        "body": """### Goal
Master initial setup, IDE environment, and build the 1st practical project integrating PyAutoGUI automation and basic data analysis.

### Checklist
- [x] Environment setup & VS Code configuration
- [x] 1st Project: Automation + Data Analysis workflow
- [x] Mouse & keyboard automation with PyAutoGUI
- [ ] Read data file and compute key metrics with Pandas
- [ ] Automated email report delivery
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M05: Variables & Sequential Structures",
        "labels": ["fundamentals"],
        "body": """### Goal
Solidify variable types, type casting, modern string formatting, and sequential program execution.

### Checklist
- [x] Variable data types and casting
- [x] Text formatting with `.format()` and modern f-strings
- [x] Sequential Structure exercise set
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M06: If - Conditional Structures in Python",
        "labels": ["fundamentals"],
        "body": """### Goal
Master decision-making logic with `if`, `elif`, `else`, and Boolean logical operators.

### Checklist
- [x] If structure, indentation, and code blocks
- [x] Comparison operators and logical operators (`and`, `or`)
- [x] Conditional exercises (Part 1 and 2)
- [ ] Decision Structure exercise set
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M07: Strings - Manipulation & Methods",
        "labels": ["fundamentals"],
        "body": """### Goal
Perform string slicing, indexing, and use built-in string manipulation methods.

### Checklist
- [ ] Positive and negative indexing, substring slicing
- [ ] Essential string methods (`strip`, `replace`, `find`, `split`, etc.)
- [ ] Number and currency formatting
- [ ] String practical exercises (Part 1 and 2)
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M08: Python Lists - Methods & Operations",
        "labels": ["fundamentals"],
        "body": """### Goal
Work with ordered collections, mutable data structures, and nested lists.

### Checklist
- [ ] Adding/removing items (`append`, `extend`, `pop`, `remove`)
- [ ] Sorting (`sort`, `sorted`) and search (`index`, `in`)
- [ ] Shallow copy vs Deep copy
- [ ] Nested lists (matrices)
- [ ] Lists exercise set (Part 1 and 2)
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M09 & M10: Loops & Iterations (For and While)",
        "labels": ["fundamentals"],
        "body": """### Goal
Master finite and conditional loops across collections.

### Checklist
- [ ] For each loops and `enumerate` (index + item)
- [ ] Nested loops (for inside for)
- [ ] Loop control flow with `break` and `continue`
- [ ] While loops and preventing infinite loops
- [ ] Iteration structure exercise set
"""
    },
    {
        "milestone": "01 - Python Fundamentals",
        "title": "M11 to M13: Tuples, Dictionaries & Iterables",
        "labels": ["fundamentals"],
        "body": """### Goal
Understand key-value mappings (`dict`), immutable sequences (`tuple`), and iterable collections (`set`, `range`).

### Checklist
- [ ] Tuples and variable unpacking
- [ ] Dictionary methods: `keys()`, `values()`, `items()`
- [ ] Dictionary manipulation and transformation with `zip`
- [ ] Iterables, `range`, and unique sets (`set`)
- [ ] Dictionary practical exercises
"""
    },

    # --- MILESTONE 2 ---
    {
        "milestone": "02 - Core Python & Advanced Structures",
        "title": "M01: Functions in Python (def, parameters & return values)",
        "labels": ["core"],
        "body": """### Goal
Modularize code, write reusable functions, and handle exceptions cleanly.

### Checklist
- [ ] Defining functions and returning multiple values
- [ ] Positional arguments, keyword arguments, and default parameters
- [ ] Variable-length arguments (`*args` and `**kwargs`)
- [ ] Docstrings, Type Hints, and error handling
- [ ] Function challenge exercises
"""
    },
    {
        "milestone": "02 - Core Python & Advanced Structures",
        "title": "M02: List Comprehension",
        "labels": ["core"],
        "body": """### Goal
Write concise, idiomatic Python code for list transformations and filtering.

### Checklist
- [ ] Basic List Comprehension syntax
- [ ] Conditional filtering with `if`
- [ ] Inline ternary conditions (`if ... else`)
- [ ] Practical List Comprehension exercises
"""
    },
    {
        "milestone": "02 - Core Python & Advanced Structures",
        "title": "M04 & M05: Standard Libraries (time, datetime) & Challenges",
        "labels": ["core"],
        "body": """### Goal
Work with time, dates, timezones, and build practical mini-applications.

### Checklist
- [ ] Time manipulation and benchmarking with `time`
- [ ] Dates, timezones, and formatting with `datetime`
- [ ] Practical challenge: Tax calculation and column processing
- [ ] Mini-projects: Text Analyzer, Password Generator, and QR Code Generator
"""
    },

    # --- MILESTONE 3 ---
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M01 & M02: Data Analysis with Pandas & Excel Integration",
        "labels": ["data", "project"],
        "body": """### Goal
Full DataFrame manipulation, data cleaning, aggregation, and Excel automation.

### Checklist
- [ ] DataFrames, Series, and reading `.csv` / `.xlsx` files
- [ ] Filtering, grouping (`groupby`), and aggregation
- [ ] Column creation, modification, and handling missing data
- [ ] Pandas Data Analysis Mini-Project
"""
    },
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M03: End-to-End ETL Project with Pandas",
        "labels": ["data", "project"],
        "body": """### Goal
Build and execute a complete Extract, Transform, Load (ETL) pipeline.

### Checklist
- [ ] Data ingestion, inspection, and cleaning
- [ ] Feature engineering (derived variables)
- [ ] Multi-level group aggregations and data joins (`merge`/`concat`)
- [ ] Time series analysis and report generation
"""
    },
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M05 & M06: File, Folder & PDF Automation",
        "labels": ["automation"],
        "body": """### Goal
Automate filesystem operations and programmatically manipulate PDF documents.

### Checklist
- [ ] File I/O with context managers (`with open`)
- [ ] Filesystem navigation with `pathlib` and `shutil`
- [ ] PDF page splitting, merging, and table extraction (`PyPDF`, `tabula`)
"""
    },
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M07: Email Automation (Gmail, Outlook & SendGrid)",
        "labels": ["automation"],
        "body": """### Goal
Automate sending and reading corporate emails with dynamic reports and attachments.

### Checklist
- [ ] SMTP email delivery (Gmail with App Passwords)
- [ ] HTML emails with attachments, signatures, and inline images
- [ ] Reading emails and extracting attachments with `imap_tools`
- [ ] High-volume bulk emails via SendGrid API
"""
    },
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M08: SQL Database Integration",
        "labels": ["data", "database"],
        "body": """### Goal
Connect Python applications to relational databases and execute CRUD operations.

### Checklist
- [ ] Database connectivity via `pyodbc` / SQLite / MySQL
- [ ] CRUD operations: Create, Read, Update, Delete
- [ ] Direct queries into DataFrames with `pandas.read_sql`
- [ ] Introduction to ORM with `SQLAlchemy`
"""
    },
    {
        "milestone": "03 - Intermediate: Data Analysis, Automations & Web",
        "title": "M09 & M10: Web Scraping with Selenium & BeautifulSoup",
        "labels": ["web", "automation"],
        "body": """### Goal
Build automated browser bots and high-performance HTML web scrapers.

### Checklist
- [ ] CSS Selectors and XPath navigation in Selenium
- [ ] Automated form filling and automatic file downloads
- [ ] Challenge: WhatsApp automated message bot
- [ ] Parsing structured data with BeautifulSoup (BS4)
"""
    },

    # --- MILESTONE 4 ---
    {
        "milestone": "04 - Advanced: RPA, REST APIs & Dashboards",
        "title": "M01 & M02: Enterprise RPA & Regular Expressions (Regex)",
        "labels": ["advanced", "automation"],
        "body": """### Goal
Build end-to-end robotic process automation (ERP/SAP) and master Regex patterns.

### Checklist
- [ ] Enterprise desktop RPA workflows
- [ ] Regex syntax, capture groups, and complex string validation
- [ ] Challenge: Automated data extraction using Regex
"""
    },
    {
        "milestone": "04 - Advanced: RPA, REST APIs & Dashboards",
        "title": "M03: REST APIs & JSON Integration",
        "labels": ["advanced", "api"],
        "body": """### Goal
Consume external RESTful services and build custom backend APIs.

### Checklist
- [ ] Consuming public APIs (Currency Exchange, Geolocation, Public Data)
- [ ] Sending SMS notifications via Twilio API
- [ ] Building custom REST API endpoints in Python
- [ ] Firebase REST API integration
"""
    },
    {
        "milestone": "04 - Advanced: RPA, REST APIs & Dashboards",
        "title": "M04 to M08: Finance, Streamlit Dashboards & AI Agents",
        "labels": ["advanced", "data", "ai"],
        "body": """### Goal
Quantitative portfolio analysis, interactive web dashboards, and AI agents.

### Checklist
- [ ] Investment portfolio modeling, asset returns, and correlation matrices
- [ ] Interactive dashboards with Streamlit
- [ ] Packaging Python scripts into standalone executables (`.exe`) via PyInstaller
- [ ] AI Agents using OpenAI, Hugging Face, and LangChain
"""
    },

    # --- MILESTONE 5 ---
    {
        "milestone": "05 - Masterclass: Industry-Standard Projects",
        "title": "Project 1: Enterprise Process Automation (Stores & KPIs)",
        "labels": ["project", "enterprise"],
        "body": """### Goal
Build a complete automated reporting system: sales consolidation, ticket averages, and automated stakeholder email delivery.

### Checklist
- [ ] Data segmentation and store-level backup generation
- [ ] KPI calculation (Revenue, Product Variety, Average Ticket)
- [ ] Automated HTML formatted email generation with embedded tables
- [ ] Daily and annual performance ranking generation
"""
    },
    {
        "milestone": "05 - Masterclass: Industry-Standard Projects",
        "title": "Project 2: Commercial Web Scraper (Price Comparison Engine)",
        "labels": ["project", "web", "automation"],
        "body": """### Goal
Multi-site price tracking bot with pagination, item matching, and price drop notifications.

### Checklist
- [ ] Dynamic scraping across multiple e-commerce platforms
- [ ] Intelligent product matching algorithms
- [ ] Automated deal alerts and exports
"""
    },
    {
        "milestone": "05 - Masterclass: Industry-Standard Projects",
        "title": "Project 3: Data Science & Machine Learning (Airbnb Rio de Janeiro)",
        "labels": ["project", "data-science", "machine-learning"],
        "body": """### Goal
End-to-end Machine Learning project predicting Airbnb listing prices in Rio de Janeiro.

### Checklist
- [ ] Big data ingestion and multi-file consolidation
- [ ] Data cleaning, missing value imputation, and statistical outlier removal
- [ ] Exploratory Data Analysis (EDA) with Seaborn and geospatial mapping
- [ ] Categorical feature encoding
- [ ] Model training, evaluation, and hyperparameter tuning
- [ ] Model deployment with an interactive user interface
"""
    },
    {
        "milestone": "05 - Masterclass: Industry-Standard Projects",
        "title": "Project 4: Object-Oriented Programming (OOP) Architecture",
        "labels": ["oop", "project"],
        "body": """### Goal
Design production-grade software using Classes, Methods, Encapsulation, and Inheritance.

### Checklist
- [ ] Class definitions, instance attributes, and constructors (`__init__`)
- [ ] Encapsulation, private attributes, and class methods
- [ ] Inheritance and Polymorphism (Banking system with Accounts & Branches)
"""
    },
    {
        "milestone": "05 - Masterclass: Industry-Standard Projects",
        "title": "Projects 5 to 8: Web Applications, Tkinter GUIs & Games",
        "labels": ["project", "gui", "web"],
        "body": """### Goal
Create desktop GUIs with Tkinter, web applications with Flask/Django, and interactive games with Pygame.

### Checklist
- [ ] Desktop GUI with Tkinter (Live exchange rates & Inventory CRUD system)
- [ ] Game development: Flappy Bird clone with Pygame
- [ ] Web application foundations with Flask and Django
"""
    },

    # --- MILESTONE 6 ---
    {
        "milestone": "06 - Specialization, Testing & Final Certification",
        "title": "Specialization: NumPy, Matplotlib, Seaborn & PyTest",
        "labels": ["specialization"],
        "body": """### Goal
Deepen numerical computing with NumPy, master data visualization with Matplotlib/Seaborn, and implement unit tests with PyTest.

### Checklist
- [ ] Multidimensional arrays and vectorized operations with NumPy
- [ ] Custom figure anatomy, color palettes, and styling with Matplotlib
- [ ] Advanced statistical distributions with Seaborn
- [ ] Automated testing suite with PyTest
- [ ] Final 100% course completion and certification
"""
    }
]

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result

def main():
    print("=" * 65)
    print("🚀 Initializing GitHub Roadmap, Milestones & Issues...")
    print("=" * 65)

    # 1. Verify GitHub CLI authentication
    auth_check = run("gh auth status")
    if auth_check.returncode != 0:
        print("\n❌ Error: GitHub CLI (gh) is not authenticated.")
        print("Please run in your terminal: gh auth login\n")
        sys.exit(1)

    # 2. Create custom color-coded labels
    print("\n🏷️  Creating Labels...")
    labels = [
        ("fundamentals", "0E8A16", "Fundamentals & Core Python"),
        ("core", "1D76DB", "Intermediate Language Features"),
        ("advanced", "5319E7", "Advanced Architecture & Systems"),
        ("project", "D93F0B", "Practical Projects & Portfolio"),
        ("data", "0052CC", "Data Analysis, Pandas & ETL"),
        ("database", "006B75", "SQL & Relational Databases"),
        ("automation", "FBCA04", "RPA, PyAutoGUI & Scripts"),
        ("web", "B60205", "Web Scraping & Selenium"),
        ("machine-learning", "006B75", "Machine Learning & Predictive Models"),
        ("data-science", "1F883D", "Data Science & Exploratory Analysis"),
        ("api", "D4C5F9", "REST APIs & Backend Integrations"),
        ("ai", "7057FF", "Artificial Intelligence & Agents"),
        ("oop", "C2E0C6", "Object-Oriented Programming"),
        ("gui", "E99695", "Desktop GUIs & Interfaces"),
        ("enterprise", "5319E7", "Enterprise Applications"),
        ("specialization", "0366D6", "NumPy, Testing & Extras")
    ]
    for name, color, desc in labels:
        run(f'gh label create "{name}" --color "{color}" --description "{desc}" --force')

    # 3. Create Milestones (skip if already created)
    print("\n🎯 Checking / Creating Milestones...")
    existing_milestones = set()
    res_list = run("gh api repos/:owner/:repo/milestones")
    if res_list.returncode == 0:
        for item in json.loads(res_list.stdout):
            existing_milestones.add(item["title"])

    for m in MILESTONES:
        if m["title"] in existing_milestones:
            print(f"  ℹ️  Milestone already exists: {m['title']}")
            continue
        cmd = f'gh api repos/:owner/:repo/milestones -f title="{m["title"]}" -f description="{m["description"]}" -f due_on="{m["due_date"]}"'
        res = run(cmd)
        if res.returncode == 0:
            print(f"  ✅ Milestone created: {m['title']} (Due: {m['due_date'][:10]})")
        else:
            print(f"  ℹ️  Milestone status: {m['title']}")

    # 4. Create Issues (using Milestone title, which `gh issue create` expects)
    print("\n📝 Creating Issues linked to Milestones...")
    for issue in ISSUES:
        m_title = issue["milestone"]
        labels_arg = " ".join([f'--label "{lbl}"' for lbl in issue["labels"]])
        m_arg = f'--milestone "{m_title}"'

        with open("/tmp/issue_body.md", "w") as f:
            f.write(issue["body"])

        cmd = f'gh issue create --title "{issue["title"]}" --body-file "/tmp/issue_body.md" {labels_arg} {m_arg}'
        res = run(cmd)
        if res.returncode == 0:
            print(f"  ✅ Issue created: {issue['title']}")
        else:
            print(f"  ⚠️  Error creating issue: {issue['title']} ({res.stderr.strip()})")

    print("\n" + "=" * 65)
    print("🎉 All Milestones, Labels, and Issues are configured!")
    print("Target Completion Date: December 28, 2026 🏁")
    print("=" * 65)

if __name__ == "__main__":
    main()
