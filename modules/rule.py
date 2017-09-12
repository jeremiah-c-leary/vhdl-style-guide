
import re

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2

    def report_violations(self,filename):
        if len(self.violations) > 0:
            for violation in self.violations:
                print filename + ":" + str(violation) + ":" + self.name + "_" + self.identifier + ": " + self.solution

    def add_violation(self, lineNumber):
        self.violations.append(lineNumber)

    def _isLowercase(self, sString):
        if sString == sString.lower():
            return True
        else:
            return False

    def _checkIndent(self, oLine, iLineNumber):
        if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
            self.add_violation(iLineNumber)

    def _check_no_blank_line_after(self, oFile, iLineNumber): 
        if oFile.lines[iLineNumber + 1].isBlank:
            self.add_violation(iLineNumber)

    def _check_no_blank_line_before(self, oFile, iLineNumber): 
        if oFile.lines[iLineNumber - 1].isBlank:
            self.add_violation(iLineNumber)
