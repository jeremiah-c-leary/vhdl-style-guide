
from vsg import rule
import re


class concurrent_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'


class rule_001(concurrent_rule):
    '''Concurrent rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                self._check_indent(oLine, iLineNumber)


class rule_002(concurrent_rule):
    '''Concurrent rule 002 checks there is a single space after the assignment.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove all but one space after the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*<=\s*\S+', oLine.line):
                    if not re.match('^\s*\w+\s*<=\s\S', oLine.line):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*\w+\s*:\s*\w+\s*<=\s*\S+', oLine.line):
                    if not re.match('^\s*\w+\s*:\s*\w+\s*<=\s\S', oLine.line):
                        self.add_violation(iLineNumber)


class rule_003(concurrent_rule):
    '''Concurrent rule 003 checks the alignment of multiline concurrent assignments.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Align first character in row to the column of text one space after the <=.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideConcurrent:
                if oLine.isConcurrentBegin and oLine.isEndConcurrent:
                    continue
                if oLine.isConcurrentBegin:
                    iAlignmentColumn = oLine.line.find('<') + 3
                else:
                    self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)


class rule_004(concurrent_rule):
    '''Concurrent rule 004 checks there is at least a single space before the assignment.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add a single space before the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*<=', oLine.line):
                    if not re.match('^\s*\w+\s+<=', oLine.line):
                        self.add_violation(iLineNumber)
                elif re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                    if not re.match('^\s*\w+\s*:\s*\w+\s+<=', oLine.line):
                        self.add_violation(iLineNumber)


class rule_005(concurrent_rule):
    '''Concurrent rule 005 checks for labels on concurrent assignments.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Remove label on concurrent assignment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                if re.match('^\s*\w+\s*:\s*\w+\s*<=', oLine.line):
                    self.add_violation(iLineNumber)


class rule_006(concurrent_rule):
    '''Sequential rule 006 ensures the alignment of the "<=" keyword over multiple lines.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideConcurrent and fGroupFound:
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '<=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                lGroup.append(oLine)


class rule_007(concurrent_rule):
    '''Concurrent rule 007 checks for code after the "else" keyword.'''

    def __init__(self):
        concurrent_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Move code after "else" to the next line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideConcurrent:
                if re.match('^.*\selse\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)
