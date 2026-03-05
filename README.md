# AI Vacation Planner

> **4-agent CrewAI pipeline that researches, plans, and compiles a complete personalised travel itinerary** — with real-time web search, PDF export, and email delivery.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-DC2626)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-10A37F)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit)](https://streamlit.io)

---

## What It Does

Enter your destination, travel dates, and interests — a crew of 4 specialized AI agents takes over. One researches the best city, one plans your day-by-day itinerary, one finds flights and hotels, and one compiles everything into a branded PDF you can download or receive by email.

The entire pipeline uses **real-time web search** (Serper / Google Search API) — not static data.

---

## Agent Pipeline

```
User Input (destination, dates, interests)
         │
         ▼
┌─────────────────────┐
│  Expert Travel      │  Researches best city/region based on
│  Agent              │  interests, season, budget
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Local Tour Guide   │  Plans day-by-day itinerary:
│  Agent              │  attractions, dining, experiences
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Travel Logistics   │  Finds flight options + hotel
│  Manager Agent      │  recommendations with estimated costs
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Travel Plan        │  Compiles everything into a
│  Compiler Agent     │  formatted travel document
└──────────┬──────────┘
           │
           ▼
  Branded PDF + Email Delivery
```

Each agent uses **SerperDev** (Google Search) to fetch real-time travel information.

---

## Features

| Feature | Details |
|---|---|
| **4-Agent CrewAI Pipeline** | Sequential agent execution with task handoffs |
| **Real-time Web Search** | Serper API — live flight prices, hotel options, attractions |
| **PDF Generation** | Branded itinerary document with FPDF |
| **Email Delivery** | Send plan directly to any email via Gmail SMTP |
| **Personalised** | Takes name, age, interests, departure city, travel dates |
| **Streamlit UI** | Clean web interface with progress indicators |

---

## Tech Stack

| Component | Technology |
|---|---|
| **AI Agents** | CrewAI |
| **LLM** | OpenAI GPT |
| **Web Search** | SerperDev Tool (Google Search API) |
| **UI** | Streamlit |
| **PDF Generation** | FPDF |
| **Email** | SMTP (Gmail App Password) |

---

## Quick Start

```bash
git clone https://github.com/apuroopy1-prog/AI-Vacation-Planner.git
cd AI-Vacation-Planner

python -m venv venv
source venv/bin/activate
pip install streamlit crewai crewai-tools fpdf python-dotenv
```

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your_openai_api_key"
SERPER_API_KEY = "your_serper_api_key"
SENDER_EMAIL = "your_gmail@gmail.com"
SENDER_PASSWORD = "your_gmail_app_password"
```

```bash
streamlit run Streamlit.py
```

Open [http://localhost:8501](http://localhost:8501)

---

## How to Use

1. Enter your **name, age, gender**
2. Set **departure city** and **destination**
3. Pick **travel dates**
4. Describe your **interests** (food, history, adventure, beach, etc.)
5. Click **Plan My Trip!**
6. Wait ~2 minutes while the AI crew works
7. **Download PDF** or **email the plan** to yourself

> Note: Flight prices and hotel rates shown are AI-generated estimates. Always verify through official booking platforms.

---

## Built By

**Apuroop Yarabarla** — AI/ML Engineer & AI Product Owner

[![LinkedIn](https://img.shields.io/badge/LinkedIn-apuroopyarabarla-0077B5?logo=linkedin)](https://linkedin.com/in/apuroopyarabarla)
[![GitHub](https://img.shields.io/badge/GitHub-apuroopy1--prog-181717?logo=github)](https://github.com/apuroopy1-prog)
