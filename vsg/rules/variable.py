
from vsg import rule
from vsg import line
import re


class variable_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'variable'


class rule_001(variable_rule):
    '''
    Signal rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._check_indent(oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])


class rule_002(variable_rule):
    '''
    Signal rule 002 checks the "variable" keyword is lowercase.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "variable" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'variable')


class rule_003(variable_rule):
    '''
    Signal rule 003 checks there is a single space after the "variable" keyword.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "variable" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if not re.match('^\s*variable\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'variable')


class rule_004(variable_rule):
    '''
    Signal rule 004 checks the variable name is lowercase.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change variable name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])


class rule_005(variable_rule):
    '''
    Signal rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a variable space after the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if not re.match('^\s*variable\s+.*\s*:\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], ':')


class rule_006(variable_rule):
    '''
    Signal rule 006 checks there is at least a single space before the colon.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+.*\S:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_before_word(oFile.lines[iLineNumber], ':')


class rule_007(variable_rule):
    '''
    Signal rule 007 checks for default assignments in variable declarations.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'
        self.phase = 1
        self.fixable = False  # Allow the user to decide if these should be removed

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)


class rule_009(variable_rule):
    '''
    Signal rule 009 checks the colons are in the same column for all variables.
    '''

    def __init__(self):
        variable_rule.__init__(self)
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
                if oLine.isVariable:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)


class rule_010(variable_rule):
    '''
    Signal rule 010 checks the variable type is lowercase.
    '''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change variable type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+.*:\s*\w', oLine.lineLower):
                    sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
                    if '(' in sLine:
                        self._is_lowercase(sLine.split('(')[0], iLineNumber)
                    else:
                        self._is_lowercase(sLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].lstrip().rstrip().replace(';', '')
            if '(' in sLine:
                self._lower_case(oFile.lines[iLineNumber], sLine.split('(')[0])
            else:
                self._lower_case(oFile.lines[iLineNumber], sLine)
