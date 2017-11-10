
from vsg import rule
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
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                self._check_indent(oLine, iLineNumber)


class rule_002(library_rule):
    '''Library rule 002 checks for a single space after the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "library" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                if re.match('^\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)


class rule_003(library_rule):
    '''Library rule 003 checks for a blank line above the library keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Add blank line above "library" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_004(library_rule):
    '''Library rule 004 checks the library keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change "library" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_005(library_rule):
    '''Library rule 005 checks the use keyword is lower case.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Change "use" keyword to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_006(library_rule):
    '''Library rule 006 checks for a single space after the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove extra spaces after "use" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                if re.match('^\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)


class rule_007(library_rule):
    '''Library rule 007 checks for a blank line above the "use" keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove blank line(s) above "use" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                self._is_no_blank_line_before(oFile, iLineNumber)


class rule_008(library_rule):
    '''Library rule 008 checks indentation of the use keyword.'''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                self._check_indent(oLine, iLineNumber)
