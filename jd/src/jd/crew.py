from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from jd.tools.custom_tool import PDFReaderTool
from crewai_tools import FileReadTool, SerperDevTool
from crewai import LLM
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Tools
serper_tool = SerperDevTool()
file_tool = FileReadTool()

# LLM setup
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key=os.getenv('GEMINI_API_KEY')
)

@CrewBase
class Jd():
    """Jd crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[serper_tool],
            llm=llm
        )

    @agent
    def resume_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_analyzer'],
            verbose=True,
            tools=[PDFReaderTool()],
            llm=llm
        )

    @agent
    def grader(self) -> Agent:
        return Agent(
            config=self.agents_config['grader'],
            verbose=True,
            llm=llm
        )

    @task
    def job_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_research_task']
        )

    @task
    def resume_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_analysis_task'],
            output_file='analysis_report.md'
        )

    @task
    def resume_grading_task(self) -> Task:
        return Task(
            config=self.tasks_config['resume_grading_task'],
            context=[
                self.job_research_task(),
                self.resume_analysis_task()
            ],
            output_file='grading_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Jd crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
