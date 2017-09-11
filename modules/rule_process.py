
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


class rule_012(process_rule):
    '''Process rule 012 checks for the existance of the "is" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Add "is" keyword after the closing parenthesis.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd:
                if not re.match('^.*\)\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_013(process_rule):
    '''Process rule 013 checks the "is" keyword is lowercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Lowercase "is" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd:
                if re.match('^.*\)\s*is', oLine.lineLower):
                    if not re.match('^.*\)\s*is', oLine.line):
                      self.add_violation(iLineNumber)


class rule_014(process_rule):
    '''Process rule 014 checks for a single space between the ) and "is" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '014'
        self.solution = 'Ensure only a single space exists between the ) and "is" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd:
                if re.match('^.*\)\s*is', oLine.lineLower):
                    if not re.match('^.*\)\sis', oLine.lineLower):
                      self.add_violation(iLineNumber)


class rule_015(process_rule):
    '''Process rule 015 checks for a blank line or a comment line above the "process" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Add a space or a comment above the "process" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not oFile.lines[iLineNumber - 1].isBlank and not oFile.lines[iLineNumber - 1].isComment:
                      self.add_violation(iLineNumber)


class rule_016(process_rule):
    '''Process rule 016 checks a process has a label.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Add a label for the process.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if not re.match('^\s*\S+\s*:', oLine.line):
                      self.add_violation(iLineNumber)


class rule_017(process_rule):
    '''Process rule 017 checks the process label is uppercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Uppercase process label.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:', oLine.line):
                    lLine = oLine.line.split(':')
                    if not lLine[0] == lLine[0].upper():
                        self.add_violation(iLineNumber)


class rule_018(process_rule):
    '''Process rule 018 checks the "end process" has a label.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Add a label for the "end process".'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
                      self.add_violation(iLineNumber)


class rule_019(process_rule):
    '''Process rule 019 checks the "end process" label is uppercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Uppercase the label.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
                    lLine = oLine.line.split()
                    if not lLine[2] == lLine[2].upper():
                        self.add_violation(iLineNumber)


class rule_020(process_rule):
    '''Process rule 020 checks the indentation on multiline sensitivity lists.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '020'
        self.solution = 'Fix indentation of sensitivity list.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListBegin and oLine.isSensitivityListEnd:
                continue
            if oLine.insideSensitivityList:
                if oLine.isSensitivityListBegin:
                    iAlignmentColumn = oLine.line.find('(')
                elif oLine.isSensitivityListEnd and re.match('^\s*\)', oLine.line):
                    if not re.match('^\s{' + str(iAlignmentColumn) + '}\S', oLine.line):
                        self.add_violation(iLineNumber)
                else:
                    if not re.match('^\s{' + str(iAlignmentColumn + 1) + '}\S', oLine.line):
                        self.add_violation(iLineNumber)

#TODO:
# check for indentation of declarations between "process" and "begin" keywords

