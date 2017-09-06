
import rule
import re


class constant_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'constant'

    def _isConstant(self, sString):
        return re.match('^\s*constant', sString.lower())


class rule_001(constant_rule):
    '''Constant rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure there are only two spaces before constant keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not re.match('^\s\sconstant', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_002(constant_rule):
    '''Constant rule 002 checks the "constant" keyword is lowercase.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lower case "constant" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not re.match('^\s*constant', sLine):
                    self.add_violation(iLineNumber)


class rule_003(constant_rule):
    '''Constant rule 003 checks there is a single space after the "constant" keyword.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "constant" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not re.match('^\s*constant\s\w', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_004(constant_rule):
    '''Constant rule 004 checks the constant name is lowercase.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change constant name to lowercase.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not self._isLowercase(sLine.split()[1]):
                    self.add_violation(iLineNumber)


class rule_005(constant_rule):
    '''Constant rule 005 checks there is a single space after the colon.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a single space after the colon.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not re.match('^\s*constant\s+\w+\s*:\s\w', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_006(constant_rule):
    '''Constant rule 006 checks there is at least a single space before the colon.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if re.match('^\s*constant\s+\w+:', sLine.lower()):
                    self.add_violation(iLineNumber)


class rule_007(constant_rule):
    '''Constant rule 007 checks for assignments in constant declarations.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'move assignment to same line as constant declaration.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not ':=' in sLine:
                    self.add_violation(iLineNumber)


class rule_008(constant_rule):
    '''Constant rule 008 checks for prefixes in constant names.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Add c_ prefix to constant.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if self._isConstant(sLine):
                if not re.match('^\s*constant\s+c_', sLine.lower()):
                    self.add_violation(iLineNumber)

class rule_009(constant_rule):
    '''Constant rule 009 checks the colons are in the same column for all constants.'''

    def __init__(self):
        constant_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'

    def analyze(self, lines):
        iMaximumColumn = 0
        # Search for the largest column that contains the first colon
        for iLineNumber, sLine in enumerate(lines):
            if not self._isConstant(sLine):
                continue
            iCurrentColumn = sLine.find(':')
            if iMaximumColumn < iCurrentColumn:
                iMaximumColumn = iCurrentColumn
        self.solution = 'Align colon to column ' + str(iMaximumColumn + 1) + '.'
        # Compare each constants colon column to the largest found
        for iLineNumber, sLine in enumerate(lines):
            if not self._isConstant(sLine):
                continue
            iCurrentColumn = sLine.find(':')
            if not iMaximumColumn == sLine.find(':'):
                self.add_violation(iLineNumber)
