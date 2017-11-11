
from vsg import rule
import re
from vsg import line


class component_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'


class rule_001(component_rule):
    '''Component rule 001 checks for spaces before the "component" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._check_indent(oLine, iLineNumber)


class rule_002(component_rule):
    '''Component rule 002 checks for a single space after the "component" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "component" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if re.match('^\s*component\s\s+\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_003(component_rule):
    '''Component rule 003 checks for a blank line above the component keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above component keyword.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_004(component_rule):
    '''Component rule 004 checks the component keyword is lower case.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "component" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)


class rule_005(component_rule):
    '''Component rule 005 checks the is keyword is on the same line as the component keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "component" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if not re.match('^.*\s\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)

class rule_006(component_rule):
    '''Component rule 006 checks the "is" keyword is lower case.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change "is" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    if not re.match('^\s*\S+\s+\S+\s\s*is', oLine.line):
                        self.add_violation(iLineNumber)

class rule_007(component_rule):
    '''Component rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove extra spaces before "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if len(oLine.line.split()) > 2:
                    self._is_single_space_before('is', oLine, iLineNumber)


class rule_008(component_rule):
    '''Component rule 008 checks the component name is uppercase in the component declaration line.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change component name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                self._is_uppercase(oLine.line.split()[1], iLineNumber)


class rule_009(component_rule):
    '''Component rule 009 checks for spaces before the "end" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._check_indent(oLine, iLineNumber)


class rule_010(component_rule):
    '''Component rule 010 checks the "end" keyword is lowercase.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Change "end" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._is_lowercase(oLine.line.split()[0], iLineNumber)


class rule_011(component_rule):
    '''Component rule 011 checks for a single space after the "end" keyword'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Reduce spaces after "end" keyword to one.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                if re.match('^\s*end\s+\w', oLine.lineLower):
                    if not re.match('^\s*end\s\w', oLine.lineLower):
                        self.add_violation(iLineNumber)


class rule_012(component_rule):
    '''Component rule 012 checks component name is uppercase in "end" keyword line.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Uppercase component name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if len(lLine) > 2:
                    self._is_uppercase(lLine[2], iLineNumber)


class rule_013(component_rule):
    '''Component rule 013 checks for a single space after the "component" keyword in the closing of the component.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Reduce spaces after "component" keyword to one.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                if len(oLine.line.split()) >= 3:
                   self._is_single_space_after('component', oLine, iLineNumber)


class rule_014(component_rule):
    '''Component rule 014 checks the "component" keyword is lower case in the closing of the component.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Change "component" keyword to lower case.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if len(lLine) >= 3:
                    self._is_lowercase(lLine[1], iLineNumber)


class rule_015(component_rule):
    '''Component rule 015 checks the "end" keyword, "component" keyword, and component name are on the same line.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'The "end" keyword, "component" keyword and component name need to be on the same line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lLine = oLine.line.split()
                if not len(lLine) >= 3:
                    if not (lLine[0] == 'end' and lLine[1] == 'component' and not lLine[2].startswith('--')):
                        self.add_violation(iLineNumber)


class rule_016(component_rule):
    '''Component rule 016 checks for a blank line above the "end component" keywords.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Remove blank line(s) above "end component" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._is_no_blank_line_before(oFile, iLineNumber)


class rule_017(component_rule):
    '''Component rule 017 ensures the alignment of the : operator for every port in the component.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Inconsistent alignment of ":" in port declaration of component.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword and not fGroupFound and not oLine.insideEntity:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndPortMap:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isPortDeclaration:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))


class rule_018(component_rule):
    '''Component rule 018 checks for a blank line below the "end component" keywords.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add blank line after "end component" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                self._is_blank_line_after(oFile, iLineNumber)
