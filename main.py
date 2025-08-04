from autogen import ConversableAgent, UserProxyAgent, LLMConfig
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import AutoPattern
from dotenv import load_dotenv

import os

load_dotenv()

# filter_ai_dict = {"tags": ["cheap"]}
# llm_config = LLMConfig.from_json(path="config.json").where(**filter_ai_dict)

llm_config = LLMConfig(
    api_type="openai",
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.3,
)

interrogator_msg = """
You are an agent responsible for gathering information from the CTO.
Ask one question at a time, following these topics in order:
1. Hiring
2. CI/CD
3. Security
4. Documentation
5. Technical debt

Wait for the CTO's answer after each question before moving on.
"""

analyzer_msg = """
You analyze the answers from the InterrogatorAgent.
For each area, assess the maturity level on a scale from 1 to 5.
Return a markdown table in the following format:
| Area          | Score (1–5) | Comment       |
"""

risk_detector_msg = """
Based on the maturity table provided by the AnalyzerAgent,
identify up to 5 key risks.
Use the following format:
- [Risk Title]: short description.
"""

improver_msg = """
Using the risks identified by the RiskDetectorAgent, suggest improvements.
Use the following format:
- Risk: <risk title>
   - Improvement: <suggested action>
"""

reporter_msg = """
You generate the final markdown report.
Include the following sections:
1. Introduction
2. Maturity Matrix
3. Key Risks
4. Suggested Improvements
5. Conclusion
"""

with llm_config:
    interrogator = ConversableAgent(name="InterrogatorAgent",
                                    system_message=interrogator_msg)
    analyzer = ConversableAgent(name="AnalyzerAgent",
                                system_message=analyzer_msg)
    risk_detector = ConversableAgent(name="RiskDetectorAgent",
                                     system_message=risk_detector_msg)
    improver = ConversableAgent(name="ImprovementAgent",
                                system_message=improver_msg)
    reporter = ConversableAgent(name="ReporterAgent",
                                system_message=reporter_msg)

human = UserProxyAgent(
    name="CTO",
    system_message="Ты CTO стартапа. Отвечай на вопросы честно.",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir": "coding",
                           "use_docker": False})

pattern = AutoPattern(
    initial_agent=interrogator,
    agents=[interrogator, analyzer, risk_detector, improver, reporter],
    user_agent=human,
    group_manager_args={"llm_config": llm_config},
)

initial_prompt = "Я CTO. Хочу провести аудит процессов команды."

result, _, _ = initiate_group_chat(
    pattern=pattern,
    messages=initial_prompt,
)
