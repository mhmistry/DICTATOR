# DICTATOR

### AI-enabled custom password dictionary generator for brute-force attack simulation

DICTATOR is an educational cybersecurity + Generative AI project that demonstrates how AI can generate highly personalized password dictionaries for simulated brute-force attacks.

The project highlights password vulnerabilities using ethical simulations and aims to raise awareness about weak password practices and poor password hygiene.

---

# Features

* AI-powered dictionary generation using Ollama
* Personalized password generation based on user-provided information
* Platform-specific password policy inference
* Hybrid dictionary generation using:

  * Database retrieval
  * AI-generated variants
* Large-scale password wordlist support (~15M entries)
* Automatic dictionary export as `.txt`

---

# Tech Stack

* Python
* Django
* SQLite
* Ollama
* Llama 3.1 8B
* HTML / CSS

---

# Project Workflow

## Step 1: User Input Collection

The user provides information related to a hypothetical password:

* Platform (Google, Instagram, etc.)
* Username
* Password length
* Specific characters
* Character types
* Owner name
* Date of birth
* Additional personal information

---

## Step 2: Policy Inference

AI infers likely password policy based on platform.

Examples:

* Minimum password length
* Required character types
* Common platform restrictions

---

## Step 3: Database Retrieval

The system searches a large SQLite database containing millions of real-world password entries.

Filtering is based on:

* Length constraints
* Specific characters
* Character types
* User-related information

---

## Step 4: AI Variant Generation

Llama 3.1 8B generates additional personalized password candidates using contextual inputs.

Examples:

* Name variations
* DOB combinations
* Character substitutions
* Mixed patterns

---

## Step 5: Dictionary Generation

Database matches and AI-generated passwords are merged, cleaned, deduplicated, and exported into a custom dictionary.

Output:

* `custom_dict.txt`

---

# Setup Instructions

## Clone Repository

```bash
git clone <repo-url>
cd DICTATOR
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Ollama

```bash
ollama serve
```

Pull model:

```bash
ollama pull llama3.1:8b
```

---

## Start Server

```bash
python manage.py runserver
```

Open browser:

```text
http://127.0.0.1:8000/
```

---

# Wordlist Setup

## Merge Wordlists

```bash
python merge_wordlists.py
```

---

## Load into Database

```bash
python manage.py load_wordlist master_wordlist.txt
```

---

# Educational Disclaimer

This project is strictly intended for educational and research purposes.

DICTATOR demonstrates how attackers may use personal information and password patterns to generate targeted password dictionaries.

No real password cracking is performed.

The project exists solely to promote cybersecurity awareness and stronger password practices.
