
import re

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []

    def report_violations(self,filename):
        if len(self.violations) > 0:
            for violation in self.violations:
                print filename + ":" + str(violation) + ":" + self.name + "_" + self.identifier + ": " + self.solution

    def add_violation(self, lineNumber):
        self.violations.append(lineNumber + 1)

    def _isLowercase(self, sString):
        if sString == sString.lower():
            return True
        else:
            return False

    def _insideProcess(self, sString, fFlag):
        if re.match('^\s*process', sString.lower()) or re.match('^\s*\w+\s*:\s*process', sString.lower()):
            return True
        elif re.match('^\s*end\s+process', sString.lower()):
            return False
        else:
            return fFlag

    def _isConcurrent(self, sString):
        if re.match('^\s*\w+\s*<=', sString):
            return True
        else:
            return False

