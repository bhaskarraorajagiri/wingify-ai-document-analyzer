## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from crewai.tools import BaseTool # Correct import for BaseTool
from pypdf import PdfReader
from pydantic import BaseModel, Field

load_dotenv()

# SerperDevTool automatically uses the SERPER_API_KEY environment variable.
search_tool = SerperDevTool()

# Define the input schema for the custom tool
class ReadFinancialDocumentInput(BaseModel):
    """Input for the read_financial_document tool."""
    file_path: str = Field(..., description="The path to the PDF file to be read.")

# Create a custom tool by subclassing BaseTool
class ReadFinancialDocumentTool(BaseTool):
    name: str = "read_financial_document"
    description: str = "A tool to read the full text content of a PDF financial document given a file path."
    args_schema: BaseModel = ReadFinancialDocumentInput
    
    def _run(self, file_path: str) -> str:
        """
        Reads and processes the entire content of a PDF financial document.
        Args:
            file_path (str): The path to the PDF file to be read.
        Returns:
            str: The full text content of the financial document.
        """
        try:
            full_text = ""
            with open(file_path, "rb") as file:
                pdf_reader = PdfReader(file)
                for page in pdf_reader.pages:
                    full_text += page.extract_text() + "\n"
            
            # Clean and format the text
            full_text = full_text.replace("\n\n", "\n").replace("  ", " ").strip()
            
            return full_text
        
        except Exception as e:
            return f"An error occurred while reading the file: {str(e)}"

read_financial_document = ReadFinancialDocumentTool()
