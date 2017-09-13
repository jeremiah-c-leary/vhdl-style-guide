
import rule
import re


class generic_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'


class rule_001(generic_rule):
    '''Entity rule 001 checks for a blank line above the "generic" keyword.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove blank lines above "generic" keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._check_no_blank_line_before(oFile, iLineNumber)


class rule_002(generic_rule):
    '''Entity rule 002 checks indentation of the "generic" keyword.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Change indent of "generic" keyword to 2 spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_003(generic_rule):
    '''Entity rule 003 checks spacing between "generic" keyword and the open parenthesis.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Change spacing between "generic" and "(" to one space.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(generic_rule):
    '''Entity rule 004 checks indentation of generics.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change indent of generic to 4 spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isEndGenericMap:
                self._check_indent(oLine, iLineNumber)


class rule_005(generic_rule):
    '''Entity rule 005 checks for a single space after the colon in a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                        self.add_violation(iLineNumber)


class rule_006(generic_rule):
    '''Entity rule 006 checks for a single space after the default assignment in a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Reduce number of spaces after the default assignment to 1.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s*\S+\s*:=\s[\S\'"]', oLine.line):
                        self.add_violation(iLineNumber)


class rule_007(generic_rule):
    '''Entity rule 007 checks generic names are uppercase.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Uppercase generic name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)


class rule_008(generic_rule):
    '''Entity rule 008 checks the indentation of closing parenthesis for generic maps.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Closing parenthesis should be 2 spaces.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap and not oLine.isGenericDeclaration:
                self._check_indent(oLine, iLineNumber)


class rule_009(generic_rule):
    '''Entity rule 009 checks the "generic" keyword is lowercase.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Lowercase "generic" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)


class rule_010(generic_rule):
    '''Entity rule 010 checks the closing parenthesis for generics are on a line by itself.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Closing parenthesis must be on a line by itself.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap:
                if not re.match('^\s*\)', oLine.line):
                    self.add_violation(iLineNumber)


class rule_011(generic_rule):
    '''Entity rule 011 checks generic names have G_ prefixe.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add G_ to generic name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if not oLine.lineLower.split()[0].startswith('g_'):
                    self.add_violation(iLineNumber)
