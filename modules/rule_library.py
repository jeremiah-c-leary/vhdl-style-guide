
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
        self.solution = 'Remove spaces before "library" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s\s*library', sLine.lower()):
                self.add_violation(iLineNumber)


class rule_002(library_rule):
    '''Library rule 002 checks for a single space after the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "library" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library\s\s+', sLine.lower()):
                self.add_violation(iLineNumber)


class rule_003(library_rule):
    '''Library rule 003 checks for a blank line above the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above "library" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library', sLine.lower()):
                if not re.match('^\s*$', lines[iLineNumber - 1]):
                    self.add_violation(iLineNumber)


class rule_004(library_rule):
    '''Library rule 004 checks the library keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "library" keyword to lowercase.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*library', sLine.lower()):
                if not re.match('^\s*library', sLine):
                    self.add_violation(iLineNumber)


class rule_005(library_rule):
    '''Library rule 005 checks the use keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Change "use" keyword to lowercase.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if not re.match('^\s*use', sLine):
                    self.add_violation(iLineNumber)


class rule_006(library_rule):
    '''Library rule 006 checks for a single space after the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove extra spaces after "use" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use\s\s+', sLine.lower()):
                self.add_violation(iLineNumber)


class rule_007(library_rule):
    '''Library rule 007 checks for a blank line above the "use" keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove blank line(s) above "use" keyword.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if re.match('^\s*$', lines[iLineNumber - 1]):
                    self.add_violation(iLineNumber)


class rule_008(library_rule):
    '''Library rule 008 checks indentation of the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Change indent of "use" keyword to 2 spaces.'

    def analyze(self, lines):
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*use', sLine.lower()):
                if not re.match('^\s\suse', sLine.lower()):
                    self.add_violation(iLineNumber)
