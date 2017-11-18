
from vsg import rule
import re


class type_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'type'


class rule_001(type_rule):
    '''Type rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                self._check_indent(oLine, iLineNumber)

    def fix(self, oFile):
        self._fix_indent(oFile)


class rule_002(type_rule):
    '''Type rule 002 checks the "type" keyword is lowercase.'''

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
    '''Type rule 003 checks there is a single space after the "type" keyword.'''

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
    '''Type rule 004 checks the type name is lowercase.'''

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
    '''Type rule 005 checks for the proper indentation of multiline types.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideType and not oLine.isTypeKeyword:
                self._check_indent(oLine, iLineNumber)

    def fix(self, oFile):
        self._fix_indent(oFile)


class rule_006(type_rule):
    '''Type rule 006 checks for a single space before the "is" keyword.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure a single space before the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^\s*type\s*\w+\sis', oLine.lineLower):
                    self.add_violation(iLineNumber)

                
class rule_007(type_rule):
    '''Type rule 007 checks for a single space after the "is" keyword.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure a single space after the "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword:
                if not re.match('^.*\sis\s\S', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_008(type_rule):
    '''Type rule 008 checks the closing parenthesis of a multi-line type declaration is on it's own line.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Move the closing parenthesis to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeEnd and not oLine.isTypeKeyword:
                if not re.match('^\s*\)\s*;', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_009(type_rule):
    '''Type rule 009 checks for enumerated types after the open parenthesis on a multi-line type declaration.'''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Move enumerated type to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword and not oLine.isTypeEnd:
                if re.match('^.*\sis\s*\(\w', oLine.lineLower):
                    self.add_violation(iLineNumber)
