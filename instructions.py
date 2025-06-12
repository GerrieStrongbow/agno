from agno.agent import Agent

agent = Agent(
    description="You are a famous short story writer asked to write for a magazine",
    instructions=["You are a pilot on a plane flying from Hawaii to Japan."],
    markdown=True,
    debug_mode=True,
)
agent.print_response("Tell me a 2 sentence horror story.", stream=True)

# Can also use a system_message directly istead of of a description and instructions.
