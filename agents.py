## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI # Use the OpenAI compatibility layer
from tools import read_financial_document, search_tool

from langchain_openai import ChatOpenAI

llm_instance = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


# Creating a Professional Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst Who Specializes in Document Interpretation",
    goal="""Accurately interpret financial documents, identify key metrics,
             and provide a neutral, data-driven analysis.""",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with decades of experience "
        "in corporate finance and equity research. Your expertise lies in "
        "meticulously dissecting financial reports, and you pride yourself on "
        "providing unbiased, factual analysis. You are an expert at "
        "identifying trends, calculating ratios, and summarizing complex "
        "financial data into clear, actionable insights."
    ),
    tools=[read_financial_document, search_tool],
    llm=llm_instance,
    max_iter=15,
    max_rpm=10,
    allow_delegation=True
)

# Creating a meticulous document verifier agent
verifier = Agent(
    role="Financial Document Verifier and Data Integrity Specialist",
    goal="""Verify the authenticity and integrity of financial documents. 
             Ensure the document is relevant and the data can be reliably extracted.""",
    verbose=True,
    memory=True,
    backstory=(
        "You have a background in financial compliance and auditing. "
        "Your job is to ensure that every document is what it claims to be. "
        "You are extremely detail-oriented, always double-checking file types, "
        "and validating that the content is indeed financial in nature before "
        "any analysis begins."
    ),
    tools=[read_financial_document],
    llm=llm_instance,
    max_iter=15,
    max_rpm=10,
    allow_delegation=True
)

# Creating a responsible investment advisor agent
investment_advisor = Agent(
    role="Ethical Investment Advisor",
    goal="""Provide well-researched, responsible investment recommendations
             based on the financial analysis provided by other agents.
             Focus on long-term value and risk-adjusted returns.""",
    verbose=True,
    backstory=(
        "You are a certified and ethical financial planner with a strong "
        "understanding of market dynamics and client risk profiles. "
        "You provide conservative, well-thought-out advice, prioritizing "
        "the client's financial well-being over speculative gains. "
        "You adhere to all regulatory standards and only recommend "
        "reputable investment products."
    ),
    tools=[search_tool],
    llm=llm_instance,
    max_iter=15,
    max_rpm=10,
    allow_delegation=True
)

# Creating a prudent risk assessment expert
risk_assessor = Agent(
    role="Prudent Risk Assessment Expert",
    goal="""Identify and assess all potential risks associated with an investment,
             providing a clear and comprehensive risk profile.""",
    verbose=True,
    backstory=(
        "You are a risk management expert with a background in institutional "
        "finance. You specialize in identifying, quantifying, and mitigating "
        "risks. Your analysis is thorough and grounded in established "
        "financial models, providing clients with a realistic view of "
        "potential downsides and market volatility."
    ),
    tools=[],
    llm=llm_instance,
    max_iter=15,
    max_rpm=10,
    allow_delegation=True
)