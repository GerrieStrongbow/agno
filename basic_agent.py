from agno.agent import Agent
from agno.models.google import Gemini

agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True,
)
agent.print_response("Tell me about a breaking news story from New York.", stream=True)
