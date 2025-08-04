# 🧠 Startup Process Audit Agents (AG2)

## Overview

This project is an interactive **multi-agent audit system**, built using the **[AG2 (Autogen) framework](https://github.com/ag2ai/ag2)**. It simulates a scenario where a **CTO wants to assess the maturity of internal team processes** in five critical areas: hiring, CI/CD, security, documentation, and technical debt.

Using natural language and LLM agents, this system performs an automated cycle of:

1. Interviewing the CTO step-by-step  
2. Analyzing the maturity level of each area  
3. Identifying the key risks  
4. Suggesting improvements  
5. Compiling a structured final report  

## 🔁 Flow

| Agent               | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| **UserProxyAgent (CTO)** | Simulates a human CTO answering questions honestly                     |
| **InterrogatorAgent**    | Asks questions in five categories one by one                        |
| **AnalyzerAgent**        | Evaluates maturity level (1–5) based on answers                     |
| **RiskDetectorAgent**    | Identifies up to 5 key risks from the maturity scores               |
| **ImprovementAgent**     | Suggests improvements for each identified risk                     |
| **ReporterAgent**        | Compiles a final markdown report with all findings                 |

## 🧪 Example Use Case

Suppose you're CTO of a small startup and want to quickly assess the state of your internal practices. This agentic system guides you through the questions and autonomously generates a helpful audit report.

