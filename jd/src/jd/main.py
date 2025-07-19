#!/usr/bin/env python
import sys
import warnings
from jd.crew import Jd
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def load_job_description(file_path="job_description.txt"):
    try:
        return Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        raise Exception(f"Could not load job description from {file_path}: {e}")

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_description': load_job_description(),
        'folder_path': 'resumes'
    }

    try:
        Jd().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_description': load_job_description(),
        'folder_path': 'resumes'
    }

    try:
        Jd().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Jd().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return results.
    """
    inputs = {
        'job_description': load_job_description(),
        'folder_path': 'resumes'
    }

    try:
        Jd().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
