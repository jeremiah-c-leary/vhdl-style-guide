
import rule
import re


class library_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'library'


class rule_001(library_rule):
    '''Library rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '001'
        self.description = 'Remove spaces before library keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s\s*library', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_002(library_rule):
    '''Library rule 002 checks for a single space after the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '002'
        self.description = 'Remove extra spaces after library keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library\s\s+', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_003(library_rule):
    '''Library rule 003 checks for a blank line above the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '003'
        self.description = 'Add blank line above library keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library', sLine.lower()):
                if not re.match('^\s*$', lines[iLineNumber - 1]):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_004(library_rule):
    '''Library rule 004 checks the library keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '004'
        self.description = 'Change library keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library', sLine.lower()):
                if not re.match('^\s*library', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_005(library_rule):
    '''Library rule 005 checks the use keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '005'
        self.description = 'Change use keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if not re.match('^\s*use', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_006(library_rule):
    '''Library rule 006 checks for a single space after the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '006'
        self.description = 'Remove extra spaces after use keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use\s\s+', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_007(library_rule):
    '''Library rule 007 checks for a blank line above the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '007'
        self.description = 'Remove blank line above use keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if re.match('^\s*$', lines[iLineNumber - 1]):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_008(library_rule):
    '''Library rule 008 checks indentation of the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '008'
        self.description = 'Change indent of use keyword to 2 spaces.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if not re.match('^\s\suse', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines
