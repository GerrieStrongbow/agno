from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.google import Gemini
from agno.utils.pprint import pprint_run_response

agent = Agent(model=Gemini(id="gemini-1.5-flash"), markdown=True, monitoring=True)
# agent.print_response("Share a 2 sentence horror story")

# Run agent and return the response as a variable
response: RunResponse = agent.run("Tell me a 100-word short story about a robot")
# Run agent and return the response as a stream
response_stream: Iterator[RunResponse] = agent.run(
    "Tell me a 100-word short story about a lion", stream=True
)

# Print the response in markdown format
pprint_run_response(response, markdown=True)
# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)
