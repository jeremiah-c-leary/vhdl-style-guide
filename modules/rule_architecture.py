
import rule
import re


class architecture_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'


class rule_001(architecture_rule):
    '''Architecture rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '001'
        self.description = 'Remove spaces before architecture keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s\s*architecture', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_002(architecture_rule):
    '''Architecture rule 002 checks for a single space between "architecture", "of", and "is" keywords.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '002'
        self.description = 'Remove extra spaces after architecture keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*architecture', sLine.lower()):
                if re.match('^\s*architecture\s\s*\w\w+\s\s*of\s\s*\w\w+\s\s*is', sLine.lower()):
                    if not re.match('^\s*architecture\s\w\w+\sof\s\w\w+\sis', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_003(architecture_rule):
    '''Architecture rule 003 checks for a blank line above the architecture keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '003'
        self.description = 'Add blank line above architecture keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*architecture', sLine.lower()):
                if not re.match('^\s*$', lines[iLineNumber - 1]):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_004(architecture_rule):
    '''Architecture rule 004 checks the architecture keyword is lower case.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '004'
        self.description = 'Change architecture keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*architecture', sLine.lower()):
                if not re.match('^\s*architecture', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_005(architecture_rule):
    '''Architecture rule 005 checks if the "of" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '005'
        self.description = 'Change use keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*architecture', sLine.lower()):
                lLine = sLine.lower().split()
                if len(lLine) < 3:
                    lFailureLines.append(iLineNumber + 1)
                elif not lLine[2] == "of":
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_006(architecture_rule):
    '''Architecture rule 006 checks if the "is" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        architecture_rule.__init__(self)
        self.identifier = '006'
        self.description = 'Change use keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*architecture', sLine.lower()):
                lLine = sLine.lower().split()
                if len(lLine) < 5:
                    lFailureLines.append(iLineNumber + 1)
                elif not lLine[4] == "is":
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines



#class rule_006(architecture_rule):
#    '''Architecture rule 006 checks for a single space after the use keyword.'''
#
#    def __init__(self):
#        architecture_rule.__init__(self)
#        self.identifier = '006'
#        self.description = 'Remove extra spaces after use keyword.'
#
#    def analyze(self, lines):
#        lFailureLines = []
#        for iLineNumber, sLine in enumerate(lines):
#            if re.match('^\s*use\s\s+', sLine.lower()):
#                lFailureLines.append(iLineNumber + 1)
#        self.violations = lFailureLines
#
#
#class rule_007(architecture_rule):
#    '''Architecture rule 007 checks for a blank line above the "use" keyword.'''
#
#    def __init__(self):
#        architecture_rule.__init__(self)
#        self.identifier = '007'
#        self.description = 'Remove blank line above use keyword.'
#
#    def analyze(self, lines):
#        lFailureLines = []
#        for iLineNumber, sLine in enumerate(lines):
#            if re.match('^\s*use', sLine.lower()):
#                if re.match('^\s*$', lines[iLineNumber - 1]):
#                    lFailureLines.append(iLineNumber + 1)
#        self.violations = lFailureLines
#
#
#class rule_008(architecture_rule):
#    '''Architecture rule 008 checks indentation of the use keyword.'''
#
#    def __init__(self):
#        architecture_rule.__init__(self)
#        self.identifier = '008'
#        self.description = 'Change indent of use keyword to 2 spaces.'
#
#    def analyze(self, lines):
#        lFailureLines = []
#        for iLineNumber, sLine in enumerate(lines):
#            if re.match('^\s*use', sLine.lower()):
#                if not re.match('^\s\suse', sLine.lower()):
#                    lFailureLines.append(iLineNumber + 1)
#        self.violations = lFailureLines
