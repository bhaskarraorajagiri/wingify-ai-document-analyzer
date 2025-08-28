## Importing libraries and files
from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import read_financial_document, search_tool # Import search_tool here

## Creating a task to verify the document
verify_document_task = Task(
    description="Verify that the provided file at `{file_path}` is a financial document. "
                "If it is, confirm its validity. If it is not, report that it's "
                "not a financial document and state why. "
                "Use the `read_financial_document` tool to inspect the file content.",
    expected_output="A clear statement confirming if the file is a valid financial document "
                     "or not, and a brief summary of the initial findings.",
    agent=verifier,
    tools=[read_financial_document],
    async_execution=False
)

## Creating a task to analyze the financial document
analyze_document_task = Task(
    description="Carefully read and analyze the financial document at `{file_path}` to extract "
                "key financial metrics such as revenue, net income, assets, liabilities, "
                "and cash flow. Identify trends over time and prepare a detailed summary "
                "of the company's financial health. "
                "Use the `read_financial_document` tool to get the document content.",
    expected_output="A structured report including key financial figures, a trend analysis, "
                     "and a summary of the company's financial performance.",
    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False
)

## Creating an investment analysis task
investment_analysis_task = Task(
    description="""Based on the detailed financial analysis, provide professional,
                 data-driven investment recommendations. Evaluate the company's
                 potential for growth and its competitive position in the market.
                 Consider the user's query: {query} when formulating advice.
                 Use the search tool to find relevant market news and analyst ratings.""",
    expected_output="A comprehensive investment recommendation report with clear "
                     "reasons for each suggestion, supported by financial data and external research.",
    agent=investment_advisor,
    tools=[search_tool], # FIX: Add search tool to the task
    async_execution=False
)

## Creating a risk assessment task
risk_assessment_task = Task(
    description="""Based on the financial analysis, identify and quantify the
                 potential risks associated with investing in the company.
                 Provide a clear risk profile, including market risks, liquidity risks,
                 and company-specific risks. The user's query is: {query}.
                 Use the search tool to research potential risks, legal issues, or market volatility.""",
    expected_output="A detailed risk assessment report that outlines all potential risks "
                     "and their potential impact, along with a final risk score.",
    agent=risk_assessor,
    tools=[search_tool], # FIX: Add search tool to the task
    async_execution=False
)