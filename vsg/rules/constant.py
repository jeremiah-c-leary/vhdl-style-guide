
from vsg import rule
import re


class constant_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'constant'


class rule_001(constant_rule):
    '''Constant rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                self._check_indent(oLine, iLineNumber)


class rule_002(constant_rule):
    '''Constant rule 002 checks the "constant" keyword is lowercase.'''

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


class rule_003(constant_rule):
    '''Constant rule 003 checks there is a single space after the "constant" keyword.'''

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


class rule_004(constant_rule):
    '''Constant rule 004 checks the constant name is lowercase.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change constant name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)


class rule_005(constant_rule):
    '''Constant rule 005 checks there is a single space after the colon.'''

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


class rule_006(constant_rule):
    '''Constant rule 006 checks there is at least a single space before the colon.'''

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


class rule_007(constant_rule):
    '''Constant rule 007 checks for assignments in constant declarations.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'move assignment to same line as constant declaration.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not ':=' in oLine.line:
                    self.add_violation(iLineNumber)


class rule_008(constant_rule):
    '''Constant rule 008 checks for prefixes in constant names.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Add c_ prefix to constant.'
        self.phase = 7

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConstant:
                if not re.match('^\s*constant\s+c_', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_009(constant_rule):
    '''Constant rule 009 checks the colons are in the same column for all constants.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.phase = 5

    def analyze(self, oFile):
        iMaximumColumn = 0
        # Search for the largest column that contains the first colon
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isConstant:
                continue
            iCurrentColumn = oLine.line.find(':')
            if iMaximumColumn < iCurrentColumn:
                iMaximumColumn = iCurrentColumn
        self.solution = 'Align colon to column ' + str(iMaximumColumn + 1) + '.'
        # Compare each constants colon column to the largest found
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isConstant:
                continue
            if not iMaximumColumn == oLine.line.find(':'):
                self.add_violation(iLineNumber)
