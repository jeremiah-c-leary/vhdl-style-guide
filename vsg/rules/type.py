
from vsg import rule
import re


class type_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'type'


class rule_001(type_rule):
    '''Signal rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_002(type_rule):
    '''Signal rule 002 checks the "type" keyword is lowercase.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Lowercase "type" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_003(type_rule):
    '''Signal rule 003 checks there is a single space after the "type" keyword.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "type" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^\s*type\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_004(type_rule):
    '''Signal rule 004 checks the type name is lowercase.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change type name to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                self._is_lowercase(oLine.line.split()[1], iLineNumber)


class rule_005(type_rule):
    '''Signal rule 005 checks for the proper indentation of multiline types.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideType and not oLine.isTypeKeyword:
                self._check_indent(oLine, iLineNumber)
