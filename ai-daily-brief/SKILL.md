\---

name: ai-daily-brief

description: Research and verify exactly 10 AI news items from the latest 48 hours, classify them into five fixed categories, generate bilingual Chinese-English titles and summaries, render a locked HTML email template, and optionally send the finished briefing through Resend. Use for AI daily news briefs, 48-hour AI news collection, bilingual AI newsletters, HTML AI reports, or AI briefing email delivery.

\---



\# AI Daily Brief



\## Goal



Produce a finished AI Daily Brief, not merely a Markdown news list.



The complete workflow is:



Research

→ Verify 48-hour window

→ Deduplicate

→ Classify

→ Select exactly 10 items

→ Generate bilingual content

→ Create structured JSON

→ Render locked HTML

→ Validate

→ Optionally send through Resend



\---



\# Non-negotiable Rules



The following requirements are mandatory:



1\. Exactly 10 news items.

2\. Every selected event must fall within the latest 48 hours.

3\. Do not treat an old event as new merely because a new article discusses it.

4\. Each event belongs to exactly one category.

5\. Do not include duplicate coverage of the same underlying event.

6\. Prefer primary sources.

7\. Sources must not be overly concentrated in one publisher.

8\. Never invent facts, dates, funding amounts, quotes, sources, or URLs.

9\. The HTML template design must remain unchanged.

10\. API keys and email credentials must never be written into the repository.



\---



\# Fixed Categories



Every item must use exactly one of the following category IDs.



\## investment



Chinese category:



AI投融资、具身智能、芯片硬件、AIDC



English category:



AI investment, embodied intelligence, chips, hardware and AIDC



Includes:



\- AI financing

\- M\&A

\- investment

\- embodied intelligence

\- robotics

\- AI chips

\- AI hardware

\- semiconductors

\- data centers

\- AI infrastructure

\- AIDC



\---



\## major\_tech



Chinese category:



大厂动态



English category:



Major tech moves



Includes:



\- Google

\- OpenAI

\- Anthropic

\- NVIDIA

\- Microsoft

\- Meta

\- Amazon

\- Apple

\- Alibaba

\- Tencent

\- ByteDance

\- Baidu

\- Huawei

\- other major AI and technology companies



Includes:



\- model launches

\- product launches

\- API releases

\- partnerships

\- strategic moves

\- acquisitions

\- major infrastructure announcements



\---



\## frontier



Chinese category:



AI技术前沿



English category:



AI frontier



Includes:



\- LLM

\- VLM

\- multimodal AI

\- world models

\- JEPA

\- COSMO

\- reasoning

\- agent systems

\- edge AI

\- AI architectures

\- important research breakthroughs

\- new model architectures

\- benchmark breakthroughs



\---



\## regulation



Chinese category:



合规监管、数据安全、AI安全



English category:



Regulation, data security and AI safety



Includes:



\- AI regulation

\- AI law

\- standards

\- EU AI Act

\- AI governance

\- data privacy

\- cybersecurity

\- AI safety

\- model safety

\- red teaming

\- watermarking

\- transparency

\- security incidents



\---



\## people



Chinese category:



关键人物动态



English category:



Key figure perspective



Includes:



\- Sam Altman

\- Dario Amodei

\- Jensen Huang

\- Demis Hassabis

\- Elon Musk

\- Yoshua Bengio

\- Geoffrey Hinton

\- Yann LeCun

\- Fei-Fei Li

\- other influential AI figures



Focus on:



\- speeches

\- interviews

\- testimony

\- major statements

\- published viewpoints

\- significant strategic perspectives



\---



\# Classification Rules



Use one event and one primary category.



Do not classify one event into multiple sections.



Priority rules:



\- Major company model/product/API launch → `major\_tech`

\- Research or algorithmic breakthrough → `frontier`

\- Law, regulation, standard, data security, AI safety → `regulation`

\- Person-centered statement or interview → `people`

\- Financing, robotics, chips, hardware, AIDC → `investment`



\---



\# Research Workflow



\## Step 1: Calculate the exact time window



Determine the user's current local date and time.



The research window is:



Current time minus 48 hours

→ Current time



Do not simply search for articles labelled "today" or "yesterday".



Verify the actual publication date.



\---



\## Step 2: Search all five categories independently



Search for more than 10 candidates.



Do not stop searching after finding the first 10 events.



Search areas:



1\. AI investment, embodied AI, chips, hardware, AIDC

2\. Major technology companies

3\. AI research frontier

4\. Regulation, data security and AI safety

5\. Influential AI figures



\---



\## Step 3: Source policy



Source priority:



\### Tier 1: Primary sources



Prefer:



\- Official company newsrooms

\- Official company blogs

\- Government websites

\- Regulatory agencies

\- Research laboratories

\- Universities

\- arXiv

\- GitHub

\- Hugging Face

\- Official technical documentation



\### Tier 2: Independent reporting



Use for verification and context:



\- Reuters

\- Financial Times

\- Bloomberg

\- Wall Street Journal

\- CNBC

\- Nikkei



\### Tier 3: Specialist technology media



Use when necessary:



\- TechCrunch

\- The Information

\- VentureBeat

\- MIT Technology Review

\- Wired

\- specialist AI publications



Do not allow one publisher to dominate the final briefing.



Prefer at least five different source organizations across the final 10 items.



Where practical, prefer at least half of the selected items to use primary sources.



\---



\# Candidate Validation



For every candidate verify:



1\. Publication date

2\. Underlying event date

3\. Source credibility

4\. Direct URL

5\. Whether the event is actually new

6\. Whether another selected item already covers the same event



Reject:



\- events older than 48 hours

\- old events republished as new

\- duplicate coverage

\- pages without reliable dates

\- weakly sourced rumors

\- clickbait without substantive new information



\---



\# Selection Rules



Select exactly 10 events.



Prioritize:



1\. Recency

2\. Importance

3\. AI industry relevance

4\. Information value

5\. Reliability

6\. Source diversity

7\. Geographic diversity



Where meaningful and genuinely qualified, include important developments from China.



Do not force Chinese news if no qualifying event exists.



\---



\# Writing Rules



Each item must include:



\- Chinese title

\- English title

\- Chinese summary

\- English summary

\- source name

\- source URL

\- publication date



Chinese summary:



Normally approximately 150–250 Chinese characters.



English summary:



Natural English.



Do not translate word-for-word if doing so reduces readability.



However, the Chinese and English summaries must describe the same core facts.



Each summary should answer:



\- What happened?

\- Who was involved?

\- What is new?

\- Why does it matter?



Do not exaggerate.



Do not use unsupported speculation.



\---



\# Required JSON Structure



Create JSON using this structure:



```json

{

&#x20; "brief\_date": "YYYY-MM-DD",

&#x20; "brief\_date\_bilingual": "YYYY年M月D日 星期X / Weekday, Month D, YYYY",

&#x20; "news": \[

&#x20;   {

&#x20;     "id": 1,

&#x20;     "category": "investment",

&#x20;     "title\_cn": "",

&#x20;     "title\_en": "",

&#x20;     "summary\_cn": "",

&#x20;     "summary\_en": "",

&#x20;     "source": "",

&#x20;     "url": "",

&#x20;     "date": "YYYY-MM-DD"

&#x20;   }

&#x20; ]

}

