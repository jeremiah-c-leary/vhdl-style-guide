
import rule
import re
import line


class instantiation_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'


class rule_001(instantiation_rule):
    '''Instantiation rule 001 checks for proper indent of instnatiations.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Improper indentation.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration or oLine.isInstantiationPortAssignment or oLine.isInstantiationPortEnd or oLine.isInstantiationPortKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_002(instantiation_rule):
    '''Instantiation rule 002 checks for a single space after the :'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure only one space after the :.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                self._is_single_space_after(':', oLine, iLineNumber)


class rule_003(instantiation_rule):
    '''Instantiation rule 003 checks for a single space before the :'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure only one space before the :.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if not re.match('^\s*\S+\s:', oLine.line):
                    self.add_violation(iLineNumber)


class rule_004(instantiation_rule):
    '''Instantiation rule 004 checks for a blank line above the instantiation keyword.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Add blank line above instantiation keyword.'

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_005(instantiation_rule):
    '''Instantiation rule 005 checks the instantiation declaration and "port map" keywords are not on the same line.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Place "port map" keywords on the next line by itself'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if oLine.isInstantiationPortKeyword:
                    self.add_violation(iLineNumber)


class rule_006(instantiation_rule):
    '''Instantiation rule 006 checks the "port map" keywords are lower case.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change "port map" keywords to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortKeyword:
                if not re.match('^.*port\s+map', oLine.line):
                    self.add_violation(iLineNumber)


class rule_007(instantiation_rule):
    '''Instantiation rule 007 checks the closing ) for the port map is on it's own line.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Place closing ); on it\'s own line.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortEnd and oLine.isInstantiationPortAssignment:
                self.add_violation(iLineNumber)


class rule_008(instantiation_rule):
    '''Instantiation rule 008 checks the instance name is uppercase in the instantiation declaration line.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change instance name to all uppercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)


class rule_009(instantiation_rule):
    '''Instantiation rule 009 checks the entity name is uppercase in the instantiation declaration line.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Change entity name to all uppercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if re.match('^\s*\w+\s+:\s+\w+', oLine.line):
                    self._is_uppercase(oLine.line.split()[2], iLineNumber)
                elif re.match('^\s*\w+:\w+', oLine.line):
                    lLine = oLine.line.split(':')[1].split()
                    self._is_uppercase(lLine[0], iLineNumber)
                else:
                    self._is_uppercase(oLine.line.split()[1], iLineNumber)


class rule_010(instantiation_rule):
    '''Instantiation rule 010 ensures the alignment of the => operator for every port in the instantiation.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Inconsistent alignment of "=>" in port assignments of instantiation.'

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isInstantiationPortEnd:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '=>', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isInstantiationPortAssignment:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))

class rule_011(instantiation_rule):
    '''Instantiation rule 011 checks the port name is uppercase.'''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Uppercase port name.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment:
                self._is_uppercase(oLine.line.split()[0], iLineNumber)


#class rule_012(instantiation_rule):
#    '''Instantiation rule 012 checks instantiation name is uppercase in "end" keyword line.'''
#
#    def __init__(self):
#        instantiation_rule.__init__(self)
#        self.identifier = '012'
#        self.solution = 'Uppercase instantiation name.'
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isInstantiationEnd:
#                lLine = oLine.line.split()
#                if len(lLine) > 2:
#                    self._is_uppercase(lLine[2], iLineNumber)
#
#
#class rule_013(instantiation_rule):
#    '''Instantiation rule 013 checks for a single space after the "instantiation" keyword in the closing of the instantiation.'''
#
#    def __init__(self):
#        instantiation_rule.__init__(self)
#        self.identifier = '013'
#        self.solution = 'Reduce spaces after "instantiation" keyword to one.'
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isInstantiationEnd:
#                if len(oLine.line.split()) >= 3:
#                   self._is_single_space_after('instantiation', oLine, iLineNumber)
#
#
#class rule_014(instantiation_rule):
#    '''Instantiation rule 014 checks the "instantiation" keyword is lower case in the closing of the instantiation.'''
#
#    def __init__(self):
#        instantiation_rule.__init__(self)
#        self.identifier = '014'
#        self.solution = 'Change "instantiation" keyword to lower case.'
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isInstantiationEnd:
#                lLine = oLine.line.split()
#                if len(lLine) >= 3:
#                    self._is_lowercase(lLine[1], iLineNumber)
#
#
#class rule_015(instantiation_rule):
#    '''Instantiation rule 015 checks the "end" keyword, "instantiation" keyword, and instantiation name are on the same line.'''
#
#    def __init__(self):
#        instantiation_rule.__init__(self)
#        self.identifier = '015'
#        self.solution = 'The "end" keyword, "instantiation" keyword and instantiation name need to be on the same line.'
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isInstantiationEnd:
#                lLine = oLine.line.split()
#                if not len(lLine) >= 3:
#                    if not (lLine[0] == 'end' and lLine[1] == 'instantiation' and not lLine[2].startswith('--')):
#                        self.add_violation(iLineNumber)
#
#
#class rule_016(instantiation_rule):
#    '''Instantiation rule 016 checks for a blank line above the "end instantiation" keywords.'''
#
#    def __init__(self):
#        instantiation_rule.__init__(self)
#        self.identifier = '016'
#        self.solution = 'Remove blank line(s) above "end instantiation" keywords.'
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isInstantiationEnd:
#                self._is_no_blank_line_before(oFile, iLineNumber)
#
#
