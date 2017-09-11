
import rule
import re


class process_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'

  

class rule_001(process_rule):
    '''Process rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure there are only two spaces before process declaration.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                self._checkIndent(oLine, iLineNumber)


class rule_002(process_rule):
    '''Process rule 002 checks there is a single space between the process keyword and the (.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove all but one space between the "process" keyword and the (.' 

    def analyze(self, oFile):
        fInsideProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not re.match('^\s*.*process\s\(', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_003(process_rule):
    '''Process rule 003 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure there are only two spaces before "begin" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                self._checkIndent(oLine, iLineNumber)


class rule_004(process_rule):
    '''Process rule 004 checks the "begin" keyword is lower case.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.' 

    def analyze(self, oFile):
        fInsideProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                if not re.match('^.*begin', oLine.line):
                    self.add_violation(iLineNumber)


class rule_005(process_rule):
    '''Process rule 004 checks the "process" keyword is lower case.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Lowercase the "process" keyword.' 

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not re.match('^\s*.*process', oLine.line):
                    self.add_violation(iLineNumber)


class rule_006(process_rule):
    '''Process rule 006 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Ensure there are only two spaces before "end" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                self._checkIndent(oLine, iLineNumber)


class rule_007(process_rule):
    '''Process rule 007 checks for a single space between the "end" and "process" keywords.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure there are only one space between the "end" and "process" keywords.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\w+\s\w', oLine.line):
                    self.add_violation(iLineNumber)


class rule_008(process_rule):
    '''Process rule 008 checks the "end" keyword is lowercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Lowercase the "end" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*end', oLine.line):
                    self.add_violation(iLineNumber)


class rule_009(process_rule):
    '''Process rule 009 checks the "process" keyword is lowercase on the closing of a process.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Lowercase the "process" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\w+\s+process', oLine.line):
                    self.add_violation(iLineNumber)


class rule_010(process_rule):
    '''Process rule 010 checks the "begin" keyword is on it's own line.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '010'
        self.solution = 'Place "begin" keyword on seperate line.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                if not re.match('^\s*begin', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_011(process_rule):
    '''Process rule 010 checks for a blank line after the "end process" keywords.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Add a blank line after the "end process" keywords.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not oFile.lines[iLineNumber + 1].isBlank:
                    self.add_violation(iLineNumber)

#TODO:
# check for indentation of declarations between "process" and "begin" keywords
# check of "is" keyword
# Empty space or comment on line above "process" keyword
# Processes should be named
# Process names should be capitalized
# "end process" line should have Process name
# Process name in "end process" line should be capitalized
# Single space between ( and "is" keyword

