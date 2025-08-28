Financial Document Analyzer

This project is a FastAPI-based financial document analyzer built using CrewAI
 and OpenAI’s language models.
It accepts financial documents (like invoices, statements, etc.), processes them with AI agents, and returns structured insights.

The system was originally provided as part of the Wingify Internship Debug Challenge. The codebase contained several bugs, which I identified and fixed. This repo contains the corrected, working version.

Features

Upload a financial document (PDF/text) and analyze it with AI
Multi-agent workflow powered by CrewAI
REST API built with FastAPI
Extensible design for future enhancements (queues, DB storage, etc.)

Bugs Found & Fixes
During debugging, I identified and fixed the following issues:
LLM Wrapper Misconfiguration
 The project was trying to use ChatOpenAI for a Gemini API key. This caused constant authentication errors.
 Fixed by switching back to OpenAI with the correct OPENAI_API_KEY.

Environment Variable Handling
 No .env template was provided, which made setup confusing.
 Added a .env.example file so new developers can quickly configure API keys.

Code Structure & Imports
 Some imports were broken due to relative path issues.
 Cleaned up imports and ensured modules load properly when running with uvicorn.
Setup Instructions
1. Clone the Repository
    git clone https://github.com/bhaskarraorajagiri/wingify-ai-document-analyzer.git
cd wingify-ai-document-analyzer
2. Create Virtual Environment
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
3. Install Dependencies
    pip install -r requirements.txt
4. Configure Environment Variables
    OPENAI_API_KEY=your_api_key_here
5. Run the API
    uvicorn app.main:app --reload
API will be available at:
 http://127.0.0.1:8000


API Usage
Health Check
    curl http://127.0.0.1:8000/health
Response:
{"status": "ok"}

Analyze a Document
127.0.0.1:53225 - "POST /analyze
Responses
    curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@TSLA-Q2-2025-Update.pdf;type=application/pdf' \
  -F 'query=Analyze this financial document for investment insights.'
    Request URL
http://127.0.0.1:8000/analyze
Server response
Code	Details
200	
Response body
Download
{
  "status": "success",
  "query": "Analyze this financial document for investment insights.",
  "analysis": "**Tesla Investment Risk Profile - Q2 2025**\n\n**1. Market Risks:**\n- **Revenue Decline**: Total revenue decreased by 12% YoY, primarily due to reduced vehicle deliveries and lower average selling prices.\n- **Competitive Pressure**: Increased competition in the electric vehicle market may impact Tesla's market share and pricing power.\n- **Market Volatility**: Broader economic conditions could lead to fluctuations in Tesla’s stock price and investor sentiment.\n\n**2. Liquidity Risks:**\n- **Cash Flow Concerns**: Free cash flow dropped significantly by 89%, indicating potential liquidity issues amidst capital expenditures and operational challenges.\n- **Operational Costs**: Increased operating expenses related to R&D projects have further strained financial resources.\n\n**3. Company-Specific Risks:**\n- **Legal Challenges**: Ongoing lawsuits regarding misleading FSD marketing claims pose reputational risks and potential financial penalties.\n- **Securities Fraud Class Action**: A pending class action lawsuit could lead to financial liabilities and impact investor trust.\n- **Operational Inefficiencies**: Declining profit margins indicate potential inefficiencies that could affect long-term profitability.\n\n**4. Strategic Risks:**\n- **Investment in R&D**: While Tesla is investing heavily in research and development, the effectiveness of these investments in generating future revenue remains uncertain.\n- **Technological Advancements**: The company’s future success hinges on its ability to innovate, particularly in battery technology and autonomous driving.\n\n**5. Conclusion:**\nWhile Tesla remains a leader in innovation and is committed to expanding its product offerings, the current financial performance indicates significant challenges. Investors should be aware of the risks associated with declining revenues, legal issues, and market volatility. \n\n**Final Risk Score**: 7.5/10 (10 being extremely risky)\n\n**Investment Recommendation**: Hold. Investors should closely monitor Tesla’s developments, legal situations, and market conditions before making further investment decisions.",
  "file_processed": "TSLA-Q2-2025-Update.pdf"
}
Response headers
 content-length: 2275 
 content-type: application/json 
 date: Thu,28 Aug 2025 05:35:22 GMT 
 server: uvicorn 