
from vsg import rule
import re


class variable_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'variable'


class rule_001(variable_rule):
    '''Signal rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._check_indent(oLine, iLineNumber)


class rule_002(variable_rule):
    '''Signal rule 002 checks the "variable" keyword is lowercase.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "variable" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_003(variable_rule):
    '''Signal rule 003 checks there is a single space after the "variable" keyword.'''

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


class rule_004(variable_rule):
    '''Signal rule 004 checks the variable name is lowercase.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change variable name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)


class rule_005(variable_rule):
    '''Signal rule 005 checks there is a single space after the colon.'''

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


class rule_006(variable_rule):
    '''Signal rule 006 checks there is at least a single space before the colon.'''

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


class rule_007(variable_rule):
    '''Signal rule 007 checks for default assignments in variable declarations.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)


#class rule_008(variable_rule):
#    '''Signal rule 008 checks for prefixes in variable names.'''
#
#    def __init__(self):
#        variable_rule.__init__(self)
#        self.identifier = '008'
#        self.solution = 'Remove default assignment.'
#        self.prefixes = None
#        self.phase = 7
#
#    def analyze(self, oFile):
#        if not self.prefixes:
#            return
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if not oLine.isVariable:
#                continue
#            for sSignalName in oLine.line.split(':')[0].split():
#                if sSignalName.lower() == 'variable':
#                    continue
#                fPrefixFound = False
#                for sPrefixName in self.prefixes:
#                    if sSignalName.startswith(sPrefixName):
#                        fPrefixFound = True
#                        break
#                if not fPrefixFound:
#                    self.add_violation(iLineNumber)


class rule_009(variable_rule):
    '''Signal rule 009 checks the colons are in the same column for all variables.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'
        self.phase = 5

    def analyze(self, oFile):
        iMaximumColumn = 0
        # Search for the largest column that contains the first colon
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isVariable:
                continue
            iCurrentColumn = oLine.line.find(':')
            if iMaximumColumn < iCurrentColumn:
                iMaximumColumn = iCurrentColumn
        self.solution = 'Align colon to column ' + str(iMaximumColumn + 1) + '.'
        # Compare each variables colon column to the largest found
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isVariable:
                continue
            iCurrentColumn = oLine.line.find(':')
            if not iMaximumColumn == oLine.line.find(':'):
                self.add_violation(iLineNumber)


class rule_010(variable_rule):
    '''Signal rule 010 checks the variable type is lowercase.'''

    def __init__(self):
        variable_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change variable type to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariable:
                if re.match('^\s*variable\s+\w+\s+:\s+\w', oLine.lineLower):
                    sLine = oLine.line.split()[3]
                    if '(' in sLine:
                        self._is_lowercase(sLine.split('(')[0], iLineNumber)
                    else:
                        self._is_lowercase(oLine.line.split()[3], iLineNumber)

