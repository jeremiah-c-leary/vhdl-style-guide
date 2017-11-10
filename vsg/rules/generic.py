
from vsg import rule
import re
from vsg import line


class generic_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'


class rule_001(generic_rule):
    '''Generic rule 001 checks for a blank line above the "generic" keyword.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Remove blank lines above "generic" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._is_no_blank_line_before(oFile, iLineNumber)


class rule_002(generic_rule):
    '''Generic rule 002 checks indentation of the "generic" keyword.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_003(generic_rule):
    '''Generic rule 003 checks spacing between "generic" keyword and the open parenthesis.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Change spacing between "generic" and "(" to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(generic_rule):
    '''Generic rule 004 checks indentation of generics.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isEndGenericMap:
                self._check_indent(oLine, iLineNumber)


class rule_005(generic_rule):
    '''Generic rule 005 checks for a single space after the colon in a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Reduce number of spaces after the colon to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                        self.add_violation(iLineNumber)


class rule_006(generic_rule):
    '''Generic rule 006 checks for a single space after the default assignment in a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Reduce number of spaces after the default assignment to 1.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s*:\s*\S+\s*:=\s[\S\'"]', oLine.line):
                        self.add_violation(iLineNumber)


class rule_007(generic_rule):
    '''Generic rule 007 checks generic names are uppercase.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Uppercase generic name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isGenericKeyword:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)


class rule_008(generic_rule):
    '''Generic rule 008 checks the indentation of closing parenthesis for generic maps.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap and not oLine.isGenericDeclaration:
                self._check_indent(oLine, iLineNumber)


class rule_009(generic_rule):
    '''Generic rule 009 checks the "generic" keyword is lowercase.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Lowercase "generic" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)


class rule_010(generic_rule):
    '''Generic rule 010 checks the closing parenthesis for generics are on a line by itself.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Closing parenthesis must be on a line by itself.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap:
                if not re.match('^\s*\)', oLine.line):
                    self.add_violation(iLineNumber)


class rule_011(generic_rule):
    '''Generic rule 011 checks generic names have G_ prefixe.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add G_ to generic name.'
        self.phase = 7

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isGenericKeyword and not oLine.insideComponent:
                if not oLine.lineLower.split()[0].startswith('g_'):
                    self.add_violation(iLineNumber)


class rule_012(generic_rule):
    '''Generic rule 012 ensures the alignment of the : operator for every generic in the entity.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Inconsistent alignment of ":" in generic declaration of entity.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword and not fGroupFound and not oLine.isGenericDeclaration:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndGenericMap and fGroupFound:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isGenericDeclaration:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))


class rule_013(generic_rule):
    '''Generic rule 013 checks for a generic keyword on the same line as a generic declaration.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Move generic declaration to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and oLine.isGenericKeyword:
                self.add_violation(iLineNumber)


class rule_014(generic_rule):
    '''Generic rule 014 checks for at least a single space before the :.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Add a space before the :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\S+\s*:\s*\S+\s*:=', oLine.line):
                    if not re.match('^\s*\S+\s+:', oLine.line):
                        self.add_violation(iLineNumber)


class rule_015(generic_rule):
    '''Generic rule 015 ensures the alignment of the := operator for every generic in the entity.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Inconsistent alignment of ":=" in generic declaration of entity.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword and not fGroupFound and not oLine.isGenericDeclaration:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndGenericMap and fGroupFound:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isGenericDeclaration:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))


class rule_016(generic_rule):
    '''Generic rule 016 checks for multiple generate terms on a single line.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Move multiple generates to their own lines.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration:
                if re.match('^\s*\w+\s*:.*;\s*\w+\s*:', oLine.line):
                    self.add_violation(iLineNumber)
