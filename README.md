\# AI Daily Brief Skill



A reusable Codex/OpenClaw-style Agent Skill for generating a bilingual AI Daily Brief.



\## Features



\- Latest 48-hour AI news

\- Exactly 10 items

\- Five fixed categories

\- Chinese-English Executive Map

\- Chinese-English titles

\- Chinese-English summaries

\- Source URL and publication date

\- Source diversity requirements

\- Primary-source preference

\- Locked HTML template

\- Optional Resend email delivery



\---



\## Categories



1\. AI investment, embodied intelligence, chips, hardware and AIDC

2\. Major tech moves

3\. AI frontier

4\. Regulation, data security and AI safety

5\. Key AI figures



\---



\## Structure



```text

ai-daily-brief/

├── SKILL.md

├── README.md

├── requirements.txt

├── .env.example

├── .gitignore

├── templates/

│   └── template.html

├── scripts/

│   ├── render\_html.py

│   └── send\_email.py

└── examples/

&#x20;   └── news.json

