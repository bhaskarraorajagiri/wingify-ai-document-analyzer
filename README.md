# AI Financial Document Analyzer - Debug Challenge Submission

This project is a debugged and enhanced version of the "AI Internship Assignment – Debug Challenge" provided by Wingify Software Pvt. Ltd. The original application, a financial document analysis system built with CrewAI and FastAPI, was intentionally bugged. This repository contains the corrected, fully functional code, along with documentation detailing the bugs found, the fixes implemented, and a clear guide for setup and usage.

<br>

## 🐛 Bugs Found & How I Fixed Them

The provided codebase contained numerous bugs and anti-patterns that prevented the application from functioning correctly and professionally. My debugging process involved a systematic review of each file to identify and resolve these issues.

### 1. Flawed Agent Personalities & Goals
The agents were designed to be incompetent, with goals that intentionally led to bad advice, false information, and a lack of collaboration.
* **Fix:** I completely redefined the `role`, `goal`, and `backstory` for each agent (`financial_analyst`, `verifier`, `investment_advisor`, and `risk_assessor`) in `agents.py`. They now have professional, ethical, and collaborative personalities, aligning their purpose with the project's goal of providing accurate financial analysis.

### 2. Incorrect & Incomplete Tool Implementation
The `tools.py` file had missing imports, incorrect class methods, and an outdated approach to reading PDF files. The original `Pdf` class was not a standard part of the libraries, causing runtime errors.
* **Fix:** I replaced the custom, non-functional `Pdf` reader with a reliable, standard approach using the `PyPDF2` library. The `read_financial_document` function was corrected to be a proper CrewAI `tool`, ensuring it can be correctly called by the agents.

### 3. Flawed Task Descriptions & Agent Assignments
The tasks in `task.py` were designed to produce misleading outputs and were all assigned to a single, flawed agent.
* **Fix:** I created a logical, sequential workflow of four distinct tasks: `verify_document_task`, `analyze_document_task`, `investment_analysis_task`, and `risk_assessment_task`. Each task now has a clear description, a professional `expected_output`, and is assigned to the correct, specialized agent (`verifier`, `financial_analyst`, `investment_advisor`, and `risk_assessor`).

### 4. Incomplete Crew & Process
The `main.py` file only initialized the crew with a single agent and task, preventing the full multi-agent system from working.
* **Fix:** The `run_crew` function was updated to include all four specialized agents and the new, sequential task workflow. The file upload handling was also refined to use `asyncio.to_thread`, preventing the API from blocking during file operations.

### 5. Dependency Conflicts
The original `requirements.txt` file was overly restrictive and had conflicting dependencies, specifically with `onnxruntime` and `crewai`, which prevented a successful installation. It also lacked key dependencies like `pypdf2` and the LLM library.
* **Fix:** I simplified the `requirements.txt` to include only the core, top-level libraries. This allows `pip` to automatically resolve all compatible sub-dependencies, ensuring a smooth and conflict-free installation process.

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### 1. Clone the Repository

```sh
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name