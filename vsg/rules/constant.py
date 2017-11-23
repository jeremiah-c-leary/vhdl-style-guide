
from vsg import rule
from vsg import line
import re


class constant_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'constant'


class rule_001(constant_rule):
    '''
    Constant rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                self._check_indent(oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])


class rule_002(constant_rule):
    '''
    Constant rule 002 checks the "constant" keyword is lowercase.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lower case "constant" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'constant')


class rule_003(constant_rule):
    '''
    Constant rule 003 checks there is a single space after the "constant" keyword.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "constant" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'constant')


class rule_004(constant_rule):
    '''
    Constant rule 004 checks the constant name is lowercase.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change constant name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])


class rule_005(constant_rule):
    '''
    Constant rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a single space after the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant\s+\w+\s*:\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')


class rule_006(constant_rule):
    '''
    Constant rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if re.match('^\s*constant\s+\S+:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')


class rule_007(constant_rule):
    '''
    Constant rule 007 checks for assignments in constant declarations.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1
        self.fixable = False  # Too complicated at the moment to fix.

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if ':=' not in oLine.line:
                    self.add_violation(iLineNumber)


class rule_009(constant_rule):
    '''
    Constant rule 009 checks the colons are in the same column for all constants.
    '''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndArchitecture:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isConstant:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
