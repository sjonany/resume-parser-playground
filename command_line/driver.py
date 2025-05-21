import argparse
import os
from libs.resume_evaluator.ResumeEvaluator import ResumeEvaluator
from libs.resume_evaluator.UnweightedCriteriaEvaluator import UnweightedCriteriaEvaluator
from libs.resume_parser.AIResumeParser import AIResumeParser


"""
This script is designed to parse resume and evaluate compatibility with required skills.

Example command:
poetry run python -m command-line.driver java,c++ test.pdf
"""
def main():
    parser = argparse.ArgumentParser(description="Process required skills and resume path.")
    parser.add_argument("skills", type=str, help="Comma-separated list of required skills (e.g., java,c++)")
    parser.add_argument("resume_path", type=str, help="Path to the resume PDF file")

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    
    args = parser.parse_args()

    required_skills = args.skills.split(",")
    resume_path = args.resume_path

    resume_parser = AIResumeParser(openai_api_key=openai_api_key)
    parsed_resume = resume_parser.parseResume(resume_path)
    print("Parsed resume:", parsed_resume)
    evaluator = ResumeEvaluator(UnweightedCriteriaEvaluator())
    result = evaluator.evaluate(parsed_resume, required_skills)
    print(f"Resume Evaluation Result: {result}")

if __name__ == "__main__":
    main()