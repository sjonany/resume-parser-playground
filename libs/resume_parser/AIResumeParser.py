from abc import ABC, abstractmethod

from libs.resume_parser.ParsedResume import ParsedResume, JobDetail
from libs.resume_parser.ResumeParser import ResumeParser
from openai import OpenAI

import pdb
import os
import json
import base64

# TODO: Remove. This is just for demo.
STUB_JSON_STR = """
    {
    "person_name": "Stephen Joe Jonany",
    "general_skills": [
        "software engineering",
        "team leadership",
        "k-anonymization",
        "differential privacy",
        "classification",
        "AI-powered object description",
        "LLM (large language models)",
        "statistics",
        "management systems",
        "API development",
        "crowdsourcing",
        "named entity recognition",
        "multiclass classification",
        "OCR (optical character recognition)"
    ],
    "job_details": [
        {
            "skills": [
                "k-anonymization",
                "differential privacy",
                "classification",
                "AI-powered object description",
                "LLM",
                "statistics"
            ],
            "start_year": 2022,
            "end_year": 2024
        },
        {
            "skills": [
                "license management systems",
                "API services",
                "gatekeeping",
                "compliance (GDPR)",
                "admin console development",
                "chrome device management"
            ],
            "start_year": 2015,
            "end_year": 2019
        },
        {
            "skills": [
                "personalized service health",
                "early design documentation"
            ],
            "start_year": 2019,
            "end_year": 2022
        },
        {
            "skills": [
                "crowdsourcing",
                "named entity recognition",
                "data aggregation",
                "behavioral traces"
            ],
            "start_year": 2013,
            "end_year": 2014
        },
        {
            "skills": [
                "multiclass classification",
                "feedback categorization"
            ],
            "start_year": 2013,
            "end_year": 2013
        },
        {
            "skills": [
                "OCR",
                "reverse engineering",
                "screen-rendered text recognition"
            ],
            "start_year": 2012,
            "end_year": 2013
        }
    ]
}
    """

class AIResumeParser(ResumeParser):

    PROMPT_STRING = """
    Extract the candidate's name, general skills, and job details (skills, start year, end year) from this resume.
    Please return this in a structured JSON format so I can parse it like so:

    parsed_data = json.loads(output)

    parsed_resume = ParsedResume(
        person_name=parsed_data["person_name"],
        general_skills=parsed_data["general_skills"],
        job_details=[
            JobDetail(
                skills=job["skills"],
                start_year=job["start_year"],
                end_year=job["end_year"]
            ) for job in parsed_data["job_details"]
        ]
    )
    """
    # TODO: Provide few shot examples

    def __init__(self, model: str = "gpt-4.1", openai_api_key: str = None):
        """
        Initialize the AIResumeParser with a specific model.
        
        Args:
            model (str): The model to use for parsing resumes. Defaults to "gpt-4.1".
        """
        self.model = model
        self.openai_api_key = openai_api_key
        self.client = OpenAI(api_key=self.openai_api_key)


    # Function to encode the image
    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    
    def parse_resume_as_json_str(self, resume_path: str) -> str:
        resume_data_url = self.encode_image(resume_path)
        response = self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "user",
                    "content": [
                        { "type": "input_text", "text": self.PROMPT_STRING},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{resume_data_url}",
                        },
                    ],
                }
            ],
        )

        # TODO: output validation - multiple choices? 1 choice, what if not json? what if missing json fields?
        raw_json_str = response.output[0].content[0].text  # This is the JSON string inside the ```json ... ``` block

        # Step 2: Strip the markdown formatting
        json_str = raw_json_str.strip("```json\n").strip("```")
        return json_str

    """
    TODO: Implement. 
    """
    def parseResume(self, resume_path: str) -> ParsedResume:
        # TODO: Re-enable.
        # json_str = self.parse_resume_as_json_str(resume_path)
        # For now, use the stub JSON string.
        json_str = STUB_JSON_STR
        
        parsed_data = json.loads(json_str)

        parsed_resume = ParsedResume(
            person_name=parsed_data["person_name"],
            general_skills=parsed_data["general_skills"],
            job_details=[
            JobDetail(
                skills=job["skills"],
                start_year=job["start_year"],
                end_year=job["end_year"]
            ) for job in parsed_data["job_details"]
            ]
        )

        return parsed_resume