class ResumeEvaluationResult:
    def __init__(self, person_name: str, total_year_of_experience: int, criteria_score: float):
        self.person_name = person_name
        self.total_year_of_experience = total_year_of_experience
        self.criteria_score = criteria_score

    def __repr__(self):
        return (f"ResumeEvaluationResult(person_name={self.person_name!r}, "
                f"total_year_of_experience={self.total_year_of_experience}, "
                f"criteria_score={self.criteria_score})")