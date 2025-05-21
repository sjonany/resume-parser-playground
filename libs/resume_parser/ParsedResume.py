class ParsedResume:
    def __init__(self, person_name: str, general_skills: list[str], job_details: list['JobDetail']):
        self._person_name = person_name
        self._general_skills = general_skills
        self._job_details = job_details

    @property
    def person_name(self) -> str:
        return self._person_name

    @property
    def general_skills(self) -> list[str]:
        return self._general_skills

    @property
    def job_details(self) -> list['JobDetail']:
        return self._job_details

    def __str__(self) -> str:
        return (f"ParsedResume(person_name={self._person_name}, "
                f"general_skills={self._general_skills}, "
                f"job_details={self._job_details})")

    def __repr__(self) -> str:
        return self.__str__()
    
class JobDetail:
    def __init__(self, skills: list[str], start_year: int, end_year: int):
        self._skills = skills
        self._start_year = start_year
        self._end_year = end_year

    @property
    def skills(self) -> list[str]:
        return self._skills

    @property
    def start_year(self) -> int:
        return self._start_year

    @property
    def end_year(self) -> int:
        return self._end_year

    def __str__(self) -> str:
        return (f"JobDetail(skills={self._skills}, "
                f"start_year={self._start_year}, "
                f"end_year={self._end_year})")

    def __repr__(self) -> str:
        return self.__str__()
