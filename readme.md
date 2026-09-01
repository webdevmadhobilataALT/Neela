**# 🤖 Neela — AI Team Member**



> \*\*An AI-powered virtual team member that lives inside Telegram.\*\*



Neela is an AI teammate built to help startup teams communicate, plan, brainstorm, solve problems, and stay organized — directly inside Telegram.



Instead of opening another AI chatbot, your team can simply talk to \*\*Neela\*\* where the team already works.



\---



\## ✨ What is Neela?



Neela is a \*\*Telegram-based AI team member\*\* powered by Google's Gemini API.



She is designed to act less like a traditional chatbot and more like a member of the team.



You can ask Neela to:



\* 💡 Brainstorm startup ideas

\* 🧠 Solve problems

\* 💻 Help with programming

\* 📋 Plan projects and tasks

\* ✍️ Write and improve content

\* 📝 Summarize discussions

\* 🎯 Help with decision-making

\* 💬 Participate in team conversations

\* 🚀 Assist with startup planning



\---



\## 🏗️ Architecture



```text

&#x20;               ┌─────────────────┐

&#x20;               │     Telegram    │

&#x20;               └────────┬────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌─────────────────┐

&#x20;               │     Neela       │

&#x20;               │   Telegram Bot  │

&#x20;               └────────┬────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌─────────────────┐

&#x20;               │   Gemini API    │

&#x20;               │    AI Engine    │

&#x20;               └────────┬────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌─────────────────┐

&#x20;               │  AI Response    │

&#x20;               └─────────────────┘

```



\---



\## 🛠️ Tech Stack



\* \*\*Python\*\*

\* \*\*Python Telegram Bot\*\*

\* \*\*Google Gemini API\*\*

\* \*\*Async Programming\*\*

\* \*\*Environment Variables\*\*



No Django or web framework is required.



\---



\## 📁 Project Structure



```text

neela/

│

├── bot.py

├── telegram\_bot.py

├── main.py

├── requirements.txt

└── .gitignore

```



\### `bot.py`



Contains Neela's:



\* AI configuration

\* System prompt

\* Gemini integration

\* Message handling

\* `/start`

\* `/help`



\### `telegram\_bot.py`



Responsible for:



\* Telegram bot initialization

\* Loading the Telegram bot token

\* Creating the Telegram application



\### `main.py`



Responsible for:



\* Registering Telegram handlers

\* Starting the bot

\* Running polling



\---



\## ⚙️ Installation



Clone the repository:



```bash

git clone YOUR\_REPOSITORY\_URL

cd neela

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## 🔐 Environment Variables



Neela requires two environment variables:



```text

neela\_api=YOUR\_GEMINI\_API\_KEY

telegram\_token=YOUR\_TELEGRAM\_BOT\_TOKEN

```



\### Windows PowerShell



```powershell

$env:neela\_api="YOUR\_GEMINI\_API\_KEY"

$env:telegram\_token="YOUR\_TELEGRAM\_BOT\_TOKEN"

```



\*\*Never commit API keys or bot tokens to GitHub.\*\*



\---



\## ▶️ Run Neela



Start the bot with:



```bash

python main.py

```



If everything is configured correctly:



```text

Neela is online...

```



Neela can then be accessed through Telegram.



\---



\## 💬 Example



```text

You:

We need a unique SaaS idea for small businesses.



Neela:

Let's approach this from the problem first...

```



Or inside a team group:



```text

You:

@neela\_ai\_bot summarize what we decided today.

```



Neela can respond based on the conversation available to her.



\---



\## 🚀 Roadmap



Neela is currently in the early development stage.



Planned features include:



\* \[ ] Persistent conversation memory

\* \[ ] Long-term team memory

\* \[ ] Task management

\* \[ ] Deadline tracking

\* \[ ] Automatic reminders

\* \[ ] Meeting summaries

\* \[ ] Decision tracking

\* \[ ] Team member recognition

\* \[ ] Project context

\* \[ ] Scheduled reports

\* \[ ] AI-powered task assignment

\* \[ ] Startup analytics

\* \[ ] Multi-team support

\* \[ ] Production deployment

\* \[ ] Web dashboard

\* \[ ] Tool/function calling

\* \[ ] Database-backed memory



\---



\## 🎯 Vision



Most AI assistants are designed as tools you open when you need them.



\*\*Neela is designed differently.\*\*



The goal is to make Neela feel like an actual part of the team:



```text

&#x20;                Your Team

&#x20;                   │

&#x20;       ┌───────────┼───────────┐

&#x20;       │           │           │

&#x20;     Member      Member      Neela

&#x20;       │           │           │

&#x20;       └───────────┼───────────┘

&#x20;                   │

&#x20;              Telegram

```



The long-term goal is to build an AI teammate that can \*\*understand the team, remember important context, perform useful tasks, and proactively assist the team.\*\*



\---



\## 🔒 Security



Never expose:



\* Gemini API keys

\* Telegram bot tokens

\* `.env` files

\* Private credentials



Use environment variables or a secure secrets manager in production.



\---



\## 📌 Project Status



\*\*Status:\*\* 🚧 Early Development



Neela is currently being developed as a Python-based Telegram AI teammate.



The architecture and feature set will evolve as more team-management capabilities are added.



\---



\## 👩‍💻 Creator



\*\*Soma Jahan Madhobilata\*\*



Built with Python, Telegram, and Gemini.



\---



\## 📄 License



This project is licensed under the \*\*MIT License\*\*.



See the \[LICENSE](LICENSE) file for details.



\### MIT License



Copyright (c) 2026 \*\*Soma Jahan Madhobilata\*\*



Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.



