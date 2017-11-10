
from vsg import rule
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
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                self._check_indent(oLine, iLineNumber)


class rule_002(process_rule):
    '''Process rule 002 checks there is a single space between the process keyword and the (.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists between the "process" keyword and the (.' 
        self.phase = 2

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
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                self._check_indent(oLine, iLineNumber)


class rule_004(process_rule):
    '''Process rule 004 checks the "begin" keyword is lower case.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.' 
        self.phase = 6

    def analyze(self, oFile):
        fInsideProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_005(process_rule):
    '''Process rule 004 checks the "process" keyword is lower case.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Lowercase the "process" keyword.' 
        self.phase = 6

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
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                self._check_indent(oLine, iLineNumber)


class rule_007(process_rule):
    '''Process rule 007 checks for a single space between the "end" and "process" keywords.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Ensure there are only one space between the "end" and "process" keywords.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\S+\s\S', oLine.line):
                    self.add_violation(iLineNumber)


class rule_008(process_rule):
    '''Process rule 008 checks the "end" keyword is lowercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Lowercase the "end" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_009(process_rule):
    '''Process rule 009 checks the "process" keyword is lowercase on the closing of a process.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Lowercase the "process" keyword.'
        self.phase = 6

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
        self.phase = 1

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
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_012(process_rule):
    '''Process rule 012 checks for the existance of the "is" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Add "is" keyword after the closing parenthesis.'
        self.phase = 1

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
        self.phase = 6

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
        self.phase = 2

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
        self.phase = 3

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
        self.phase = 1

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
        self.phase = 6

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
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                      self.add_violation(iLineNumber)


class rule_019(process_rule):
    '''Process rule 019 checks the "end process" label is uppercase.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '019'
        self.solution = 'Uppercase the label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                if re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
                    self._is_uppercase(oLine.line.split()[2], iLineNumber)


class rule_020(process_rule):
    '''Process rule 020 checks the indentation on multiline sensitivity lists.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '020'
        self.solution = 'Fix indentation of sensitivity list.'
        self.phase = 5

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListBegin and oLine.isSensitivityListEnd:
                continue
            if oLine.insideSensitivityList:
                if oLine.isSensitivityListBegin:
                    iAlignmentColumn = oLine.line.find('(')
                elif oLine.isSensitivityListEnd and re.match('^\s*\)', oLine.line):
                    self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)
                else:
                    self._check_multiline_alignment(iAlignmentColumn + 1, oLine, iLineNumber)


class rule_022(process_rule):
    '''Process rule 022 checks for a blank line below the "begin" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '022'
        self.solution = 'Add blank line below the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                self._is_blank_line_after(oFile, iLineNumber)


class rule_021(process_rule):
    '''Process rule 021 checks for blank lines between the end of the sensitivity list and before the "begin" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '021'
        self.solution = 'Remove blank lines between the end of the sensitivity list and before the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                if oLine.isProcessBegin and oLine.isSensitivityListEnd:
                    fSkipProcess = True
                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
                    fSkipProcess = True
                if fSkipProcess:
                    if oLine.isEndProcess:
                        fSkipProcess = False
                    continue
                if oLine.isProcessBegin:
                    if fBlanksFound and not fNonBlanksFound:
                        self.add_violation(iLineNumber)
                    fCheckForBlanks = False
                    fBlanksFound = False
                    fNonBlanksFound = False
                    fSkipProcess = True
                if fCheckForBlanks:
                    if oLine.isBlank:
                        fBlanksFound = True
                    else:
                        fNonBlanksFound = True
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True


class rule_023(process_rule):
    '''Process rule 023 checks for a blank line above the "end process" keywords.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '023'
        self.solution = 'Add blank line above the "end process" keywords.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess:
                self._is_blank_line_before(oFile, iLineNumber)


class rule_024(process_rule):
    '''Process rule 024 checks for a single space after the process label and the :.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '024'
        self.solution = 'Ensure a single space exists between process label and :.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:', oLine.line):
                    if not re.match('^\s*\S+\s:', oLine.line):
                        self.add_violation(iLineNumber)


class rule_025(process_rule):
    '''Process rule 025 checks for a single space after the : and before the "process" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '025'
        self.solution = 'Ensure a single space exists between the : and the "process" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword:
                if re.match('^\s*\S+\s*:\s*\S+', oLine.line):
                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
                        self.add_violation(iLineNumber)


class rule_026(process_rule):
    '''Process rule 026 checks for blank lines between the end of the sensitivity list and process declarative lines.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '026'
        self.solution = 'Ensure a single blank line between the end of the sensitivity list and the next non-blank line.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        iBlankCount = 0
        iFailingLineNumber = 0
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                if oLine.isProcessBegin and oLine.isSensitivityListEnd:
                    fSkipProcess = True
                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
                    fSkipProcess = True
                if fSkipProcess:
                    if oLine.isEndProcess:
                        fSkipProcess = False
                    continue
                if fCheckForBlanks:
                    if oLine.isBlank:
                        iBlankCount += 1
                    else:
                        if not iBlankCount == 1 and not oLine.isProcessBegin:
                            self.add_violation(iFailingLineNumber)
                        fSkipProcess = True
                        fCheckForBlanks = False
                        iBlankCount = 0
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True
                    iFailingLineNumber = iLineNumber


class rule_027(process_rule):
    '''Process rule 027 checks for blank lines between the process declarative lines and the "begin" keyword.'''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '027'
        self.solution = 'Ensure a single blank line between the last non-blank line and the "begin" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        fCheckForBlanks = False
        fBlanksFound = False
        fNonBlanksFound = False
        fSkipProcess = False
        iBlankCount = 0
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideProcess:
                if oLine.isProcessBegin and oLine.isSensitivityListEnd:
                    fSkipProcess = True
                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isProcessBegin:
                    fSkipProcess = True
                if fSkipProcess:
                    if oLine.isEndProcess:
                        fSkipProcess = False
                    continue
                if fCheckForBlanks:
                    if oLine.isBlank:
                        iBlankCount += 1
                    if not oLine.isBlank and not oLine.isProcessBegin:
                        iBlankCount = 0
                    if oLine.isProcessBegin:
                        if not iBlankCount == 1:
                            self.add_violation(iLineNumber)
                        fSkipProcess = True
                        fCheckForBlanks = False
                        iBlankCount = 0
                if oLine.isSensitivityListEnd:
                    fCheckForBlanks = True

#TODOu
# Remove spaces after ( and before )
