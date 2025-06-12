from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
