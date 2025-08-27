from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
# Use the correct import for OpenAI
from langchain_openai import ChatOpenAI
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import verify_document_task, analyze_document_task, investment_analysis_task, risk_assessment_task
from tools import read_financial_document

# Initialize the LLM once with the OpenAI model
llm_instance = ChatOpenAI(
    model="gpt-4o",  # Use a powerful model for best results
    temperature=0.7 # Optional: Add a temperature to control creativity
)

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str):
    """To run the whole crew"""
    
    financial_crew = Crew(
        agents=[verifier, financial_analyst, investment_advisor, risk_assessor],
        tasks=[verify_document_task, analyze_document_task, investment_analysis_task, risk_assessment_task],
        process=Process.sequential,
        manager_llm=llm_instance
    )
    
    result = financial_crew.kickoff({
        'query': query, 
        'file_path': file_path
    })
    return result

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_financial_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights.")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"
    
    os.makedirs("data", exist_ok=True)
    
    try:
        content = await file.read()
        await asyncio.to_thread(lambda: open(file_path, "wb").write(content))
        
        if not query.strip():
            query = "Analyze this financial document for investment insights."
            
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        print(f"Error processing financial document: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error removing file {file_path}: {e.strerror}")