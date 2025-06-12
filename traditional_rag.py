from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType


knowledge_base = PDFKnowledgeBase(
    path="data/Bekker_et_al_ATE_2022_213_118703.pdf",
    # vector_db=PgVector(
    #     table_name="articles",
    #     db_url=db_url,
    # ),
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Enable RAG by adding references from AgentKnowledge to the user prompt.
    add_references=True,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=False,
    markdown=True,
    # debug_mode=True,
)
agent.print_response("How can the efficiency of ACCs be improved?")


# from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
# from agno.vectordb.pgvector import PgVector, SearchType

# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
# knowledge_base = PDFUrlKnowledgeBase(
#     # Read PDF from this URL
#     urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
#     # Store embeddings in the `ai.recipes` table
#     vector_db=PgVector(
#         table_name="recipes", db_url=db_url, search_type=SearchType.hybrid
#     ),
# )
# # Load the knowledge base: Comment after first run
# knowledge_base.load(upsert=True)

# agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),
#     knowledge=knowledge_base,
#     # Enable RAG by adding references from AgentKnowledge to the user prompt.
#     add_references=True,
#     # Set as False because Agents default to `search_knowledge=True`
#     search_knowledge=False,
#     markdown=True,
#     # debug_mode=True,
# )
# agent.print_response("How do I make chicken and galangal in coconut milk soup")
