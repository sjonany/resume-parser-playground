from libs.resume_evaluator.CriteriaEvaluator import CriteriaEvaluator
from libs.resume_evaluator.ResumeEvaluationResult import ResumeEvaluationResult
from libs.resume_parser.ParsedResume import ParsedResume


class ResumeEvaluator():

    def __init__(self, criteria_evaluator: CriteriaEvaluator):
        self.criteria_evaluator = criteria_evaluator

    def evaluate(self, resume: ParsedResume, required_skills: list[str]) -> ResumeEvaluationResult:
        """
        Evaluate the resume against the required skills and return a score.
        """
        total_year_of_experience = self.calc_total_year_of_experience(resume)
        criteria_score = self.criteria_evaluator.evaluate(resume, required_skills)
        return ResumeEvaluationResult(resume.person_name, total_year_of_experience, criteria_score)
    
    def calc_total_year_of_experience(self, resume: ParsedResume) -> int:
        """
        Calculate the total years of experience from the job details in the resume.
        """
        total_years = 0
        # TODO: Improve the accuracy. What if multiple jobs in the same year. Don't want to overcount.
        for job in resume.job_details:
            total_years += job.end_year - job.start_year
        return total_years

