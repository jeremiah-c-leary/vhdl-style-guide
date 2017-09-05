

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
