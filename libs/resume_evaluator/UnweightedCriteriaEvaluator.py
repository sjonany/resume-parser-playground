from libs.resume_evaluator.CriteriaEvaluator import CriteriaEvaluator
from libs.resume_parser.ParsedResume import ParsedResume
from abc import ABC


class UnweightedCriteriaEvaluator(CriteriaEvaluator):
    def evaluate(self, parsed_resume: ParsedResume, required_skills: list[str], options: dict = None) -> float:
        """
        Evaluate the parsed resume against the required skills and return a score as a float.

        :param parsed_resume: PasrsedResume object containing resume details.
        :param required_skills: List of skills required for the job.
        :param options: Additional options (not used in this implementation).
        :return: A float score representing the evaluation.
        """
        # Combine general skills and job-specific skills into a single set (case insensitive)
        all_skills = set(skill.lower() for skill in parsed_resume.general_skills)
        for job_detail in parsed_resume.job_details:
            all_skills.update(skill.lower() for skill in job_detail.skills)

        # Count how many required skills are present in the combined skills
        required_skills_lower = [skill.lower() for skill in required_skills]
        matched_skills = sum(1 for skill in required_skills_lower if skill in all_skills)

        # Calculate the score
        num = matched_skills
        den = len(required_skills) if required_skills else 1  # Avoid division by zero
        return num / den
