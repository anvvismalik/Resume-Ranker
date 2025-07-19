# src/jd/tools/pdf_reader.py

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import fitz 
import json  

class FolderReaderInput(BaseModel):
    folder_path: str = Field(..., description="Path to the folder containing PDF resumes")

class PDFReaderTool(BaseTool):
    name: str = "PDF Resume Folder Reader"
    description: str = "Reads all PDF files in a folder and extracts text from each"
    args_schema: Type[BaseModel] = FolderReaderInput

    def _run(self, folder_path: str) -> str:
        results = {}
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf"):
                full_path = os.path.join(folder_path, filename)
                try:
                    with fitz.open(full_path) as doc:
                        text = ""
                        for page in doc:
                            text += page.get_text()
                        results[filename] = text.strip()
                except Exception as e:
                    results[filename] = f"Error reading file: {str(e)}"
        return json.dumps(results, indent=2)
