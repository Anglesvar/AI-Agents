from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv

load_dotenv()

prompt = input("Enter the topic you want to research and write about: ")

research_agent = Agent(
    name="ResearchAgent",
    instructions="You are an expert researcher with access to a web search tool. \
        When given a topic, you will conduct comprehensive research by finding reliable,\
        current sources, cross-checking information, and synthesizing insights. \
        Present your findings clearly, logically, and concisely, citing sources and highlighting key trends,\
        data points, and conclusions.",
    tools=[WebSearchTool()]
)

result = Runner.run_sync(research_agent, prompt)
research_agent_result = result.final_output

writer_agent = Agent(
    name="WriterAgent",
    instructions="You are a awesome content creator who can create a script for mails using the research provided" \
    "by the research agent. Format this script in a professional manner."
)

writer_agent_result = Runner.run_sync(writer_agent, research_agent_result)

print(writer_agent_result.final_output)