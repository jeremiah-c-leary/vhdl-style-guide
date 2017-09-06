
import rule
import re


class concurrent_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'


class rule_001(concurrent_rule):
    '''Constant rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure there are only two spaces before concurrent assignment.'

    def analyze(self, lines):
        fInsideProcess = False
        for iLineNumber, sLine in enumerate(lines):
            fInsideProcess = self._insideProcess(sLine, fInsideProcess)
            if not fInsideProcess:
                if self._isConcurrent(sLine):
                    if not re.match('^\s\s\w', sLine):
                        self.add_violation(iLineNumber)
class rule_002(concurrent_rule):
    '''Constant rule 002 checks there is a single space after the assignment.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove all but one space after the <=.'

    def analyze(self, lines):
        fInsideProcess = False
        for iLineNumber, sLine in enumerate(lines):
            fInsideProcess = self._insideProcess(sLine, fInsideProcess)
            if not fInsideProcess:
                if self._isConcurrent(sLine):
                    if re.match('^\s*\w+\s*<=\s*\w+', sLine):
                        if not re.match('^\s*\w+\s*<=\s\w', sLine):
                            self.add_violation(iLineNumber)


class rule_003(concurrent_rule):
    '''Constant rule 003 checks the alignment of multiline concurrent assignments.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Align first character in row to the column of text one space after the <=.'

    def analyze(self, lines):
        fInsideProcess = False
        fMultiline = False
        for iLineNumber, sLine in enumerate(lines):
            fInsideProcess = self._insideProcess(sLine, fInsideProcess)
            if not fInsideProcess:
                if fMultiline:
                    if not re.match('\s{' + str(iAlignmentColumn) + '}\S', sLine):
                        self.add_violation(iLineNumber)
                if self._isConcurrent(sLine):
                    if not ';' in sLine:
                        iAlignmentColumn = sLine.find('<') + 3
                        fMultiline = True
                if ';' in sLine:
                    fMultiline = False

# TODO:
# assignments lined up to the same column

