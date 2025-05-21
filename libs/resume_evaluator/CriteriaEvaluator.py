from abc import ABC, abstractmethod

from libs.resume_parser import ParsedResume

class CriteriaEvaluator(ABC):
    @abstractmethod
    def evaluate(self, parsed_resume: ParsedResume, required_skills: list[str], options: dict) -> float:
        """
        Evaluate the parsed resume against the required skills and return a score as a float.

        :param parsed_resume: ParsedResume object containing resume details.
        :param required_skills: List of skills required for the job.
        :return: A float score representing the evaluation.
        """
        pass