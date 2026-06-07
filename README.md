# 🤖 AI Employee Agent Factory

A production-ready, local-first AI agent system built for the **FTE Hackathon**. This system transforms your **Obsidian** vault into an automated office where AI "Employees" process tasks based on custom skill modules.

---

## 🏗️ Architecture
The system follows a **Trigger -> Brain -> Memory** loop:
- **Trigger:** A Python `watchdog` script that monitors your local file system.
- **Brain:** A logic controller using **OpenRouter** to access state-of-the-art models (Gemini, Llama, Mistral).
- **Memory:** An **Obsidian** vault structure that keeps all tasks organized in a human-readable format.



---

## 🛠️ Features
- **Modular Skills:** AI behavior is defined in `SKILL.md` files, making it easy to "train" your agent for new roles.
- **Failover Logic:** Built-in retry mechanisms and model-switching to handle API rate limits and downtime.
- **Local-First:** Your data stays in your markdown files; only the specific task is sent for processing.
- **Zero-Cost:** Designed to run entirely on Free Tier APIs.

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Obsidian
- OpenRouter API Key

### 2. Installation
```bash
git clone [https://github.com/your-username/agent-factory.git](https://github.com/your-username/agent-factory.git)
cd agent-factory
pip install openai watchdog python-dotenv
