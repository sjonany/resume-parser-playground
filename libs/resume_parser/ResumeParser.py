from abc import ABC, abstractmethod
from typing import Any

from libs.resume_parser import ParsedResume

"""
Given path to resume pdf, return a parsed resume object.
"""
class ResumeParser(ABC):
    @abstractmethod
    def parseResume(self, resume_path: str) -> ParsedResume:
        pass