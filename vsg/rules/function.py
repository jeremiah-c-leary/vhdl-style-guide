
from vsg import rule
import re


class function_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'function'


class rule_001(function_rule):
    '''Function rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword or oLine.isFunctionBegin or oLine.isFunctionEnd or oLine.isFunctionReturn:
                self._check_indent(oLine, iLineNumber)


class rule_002(function_rule):
    '''Function rule 002 checks there is a single space between the function keyword and the function name.'''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Ensure a single space exists between the "function" keyword and the function name.' 
        self.phase = 2

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_003(function_rule):
    '''Function rule 003 checks there is a single space between the function name and the (.'''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Ensure a single space exists between the function name and the (.' 
        self.phase = 2

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function\s+\w+\s\(', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_004(function_rule):
    '''Function rule 004 checks the "begin" keyword is lower case.'''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.' 
        self.phase = 6

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionBegin:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)


class rule_005(function_rule):
    '''Function rule 005 checks the "function" keyword is lower case.'''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Lowercase the "function" keyword.' 
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword:
                if not re.match('^\s*function', oLine.line):
                    self.add_violation(iLineNumber)


#class rule_007(function_rule):
#    '''Function rule 007 checks for a single space between the "end" and "function" keywords.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '007'
#        self.solution = 'Ensure there are only one space between the "end" and "function" keywords.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                if not re.match('^\s*\S+\s\S', oLine.line):
#                    self.add_violation(iLineNumber)
#
#
#class rule_008(function_rule):
#    '''Function rule 008 checks the "end" keyword is lowercase.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '008'
#        self.solution = 'Lowercase the "end" keyword.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                self._is_lowercase(self._get_first_word(oLine), iLineNumber)
#
#
#class rule_009(function_rule):
#    '''Function rule 009 checks the "function" keyword is lowercase on the closing of a function.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '009'
#        self.solution = 'Lowercase the "function" keyword.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                if not re.match('^\s*\w+\s+function', oLine.line):
#                    self.add_violation(iLineNumber)
#
#
#class rule_010(function_rule):
#    '''Function rule 010 checks the "begin" keyword is on it's own line.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '010'
#        self.solution = 'Place "begin" keyword on seperate line.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionBegin:
#                if not re.match('^\s*begin', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#
#
#class rule_011(function_rule):
#    '''Function rule 010 checks for a blank line after the "end function" keywords.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '011'
#        self.solution = 'Add a blank line after the "end function" keywords.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                self._is_blank_line_after(oFile, iLineNumber)
#
#
#class rule_012(function_rule):
#    '''Function rule 012 checks for the existance of the "is" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '012'
#        self.solution = 'Add "is" keyword after the closing parenthesis.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isSensitivityListEnd:
#                if not re.match('^.*\)\s*is', oLine.lineLower):
#                    self.add_violation(iLineNumber)
#
#
#class rule_013(function_rule):
#    '''Function rule 013 checks the "is" keyword is lowercase.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '013'
#        self.solution = 'Lowercase "is" keyword.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isSensitivityListEnd:
#                if re.match('^.*\)\s*is', oLine.lineLower):
#                    if not re.match('^.*\)\s*is', oLine.line):
#                      self.add_violation(iLineNumber)
#
#
#class rule_014(function_rule):
#    '''Function rule 014 checks for a single space between the ) and "is" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '014'
#        self.solution = 'Ensure only a single space exists between the ) and "is" keyword.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isSensitivityListEnd:
#                if re.match('^.*\)\s*is', oLine.lineLower):
#                    if not re.match('^.*\)\sis', oLine.lineLower):
#                      self.add_violation(iLineNumber)
#
#
#class rule_015(function_rule):
#    '''Function rule 015 checks for a blank line or a comment line above the "function" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '015'
#        self.solution = 'Add a space or a comment above the "function" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionKeyword:
#                if not oFile.lines[iLineNumber - 1].isBlank and not oFile.lines[iLineNumber - 1].isComment:
#                      self.add_violation(iLineNumber)
#
#
#class rule_016(function_rule):
#    '''Function rule 016 checks a function has a label.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '016'
#        self.solution = 'Add a label for the function.'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionKeyword:
#                if not re.match('^\s*\S+\s*:', oLine.line):
#                      self.add_violation(iLineNumber)
#
#
#class rule_017(function_rule):
#    '''Function rule 017 checks the function label is uppercase.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '017'
#        self.solution = 'Uppercase function label.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionKeyword:
#                if re.match('^\s*\S+\s*:', oLine.line):
#                    lLine = oLine.line.split(':')
#                    if not lLine[0] == lLine[0].upper():
#                        self.add_violation(iLineNumber)
#
#
#class rule_018(function_rule):
#    '''Function rule 018 checks the "end function" has a label.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '018'
#        self.solution = 'Add a label for the "end function".'
#        self.phase = 1
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                if not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
#                      self.add_violation(iLineNumber)
#
#
#class rule_019(function_rule):
#    '''Function rule 019 checks the "end function" label is uppercase.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '019'
#        self.solution = 'Uppercase the label.'
#        self.phase = 6
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                if re.match('^\s*\w+\s+\w+\s+\w+', oLine.line):
#                    self._is_uppercase(oLine.line.split()[2], iLineNumber)
#
#
#class rule_020(function_rule):
#    '''Function rule 020 checks the indentation on multiline sensitivity lists.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '020'
#        self.solution = 'Fix indentation of sensitivity list.'
#        self.phase = 5
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isSensitivityListBegin and oLine.isSensitivityListEnd:
#                continue
#            if oLine.insideSensitivityList:
#                if oLine.isSensitivityListBegin:
#                    iAlignmentColumn = oLine.line.find('(')
#                elif oLine.isSensitivityListEnd and re.match('^\s*\)', oLine.line):
#                    self._check_multiline_alignment(iAlignmentColumn, oLine, iLineNumber)
#                else:
#                    self._check_multiline_alignment(iAlignmentColumn + 1, oLine, iLineNumber)
#
#
#class rule_022(function_rule):
#    '''Function rule 022 checks for a blank line below the "begin" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '022'
#        self.solution = 'Add blank line below the "begin" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionBegin:
#                self._is_blank_line_after(oFile, iLineNumber)
#
#
#class rule_021(function_rule):
#    '''Function rule 021 checks for blank lines between the end of the sensitivity list and before the "begin" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '021'
#        self.solution = 'Remove blank lines between the end of the sensitivity list and before the "begin" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        fCheckForBlanks = False
#        fBlanksFound = False
#        fNonBlanksFound = False
#        fSkipFunction = False
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.insideFunction:
#                if oLine.isFunctionBegin and oLine.isSensitivityListEnd:
#                    fSkipFunction = True
#                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isFunctionBegin:
#                    fSkipFunction = True
#                if fSkipFunction:
#                    if oLine.isEndFunction:
#                        fSkipFunction = False
#                    continue
#                if oLine.isFunctionBegin:
#                    if fBlanksFound and not fNonBlanksFound:
#                        self.add_violation(iLineNumber)
#                    fCheckForBlanks = False
#                    fBlanksFound = False
#                    fNonBlanksFound = False
#                    fSkipFunction = True
#                if fCheckForBlanks:
#                    if oLine.isBlank:
#                        fBlanksFound = True
#                    else:
#                        fNonBlanksFound = True
#                if oLine.isSensitivityListEnd:
#                    fCheckForBlanks = True
#
#
#class rule_023(function_rule):
#    '''Function rule 023 checks for a blank line above the "end function" keywords.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '023'
#        self.solution = 'Add blank line above the "end function" keywords.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isEndFunction:
#                self._is_blank_line_before(oFile, iLineNumber)
#
#
#class rule_024(function_rule):
#    '''Function rule 024 checks for a single space after the function label and the :.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '024'
#        self.solution = 'Ensure a single space exists between function label and :.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionKeyword:
#                if re.match('^\s*\S+\s*:', oLine.line):
#                    if not re.match('^\s*\S+\s:', oLine.line):
#                        self.add_violation(iLineNumber)
#
#
#class rule_025(function_rule):
#    '''Function rule 025 checks for a single space after the : and before the "function" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '025'
#        self.solution = 'Ensure a single space exists between the : and the "function" keyword.'
#        self.phase = 2
#
#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isFunctionKeyword:
#                if re.match('^\s*\S+\s*:\s*\S+', oLine.line):
#                    if not re.match('^\s*\S+\s*:\s\S', oLine.line):
#                        self.add_violation(iLineNumber)
#
#
#class rule_026(function_rule):
#    '''Function rule 026 checks for blank lines between the end of the sensitivity list and function declarative lines.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '026'
#        self.solution = 'Ensure a single blank line between the end of the sensitivity list and the next non-blank line.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        fCheckForBlanks = False
#        fBlanksFound = False
#        fNonBlanksFound = False
#        fSkipFunction = False
#        iBlankCount = 0
#        iFailingLineNumber = 0
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.insideFunction:
#                if oLine.isFunctionBegin and oLine.isSensitivityListEnd:
#                    fSkipFunction = True
#                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isFunctionBegin:
#                    fSkipFunction = True
#                if fSkipFunction:
#                    if oLine.isEndFunction:
#                        fSkipFunction = False
#                    continue
#                if fCheckForBlanks:
#                    if oLine.isBlank:
#                        iBlankCount += 1
#                    else:
#                        if not iBlankCount == 1 and not oLine.isFunctionBegin:
#                            self.add_violation(iFailingLineNumber)
#                        fSkipFunction = True
#                        fCheckForBlanks = False
#                        iBlankCount = 0
#                if oLine.isSensitivityListEnd:
#                    fCheckForBlanks = True
#                    iFailingLineNumber = iLineNumber
#
#
#class rule_027(function_rule):
#    '''Function rule 027 checks for blank lines between the function declarative lines and the "begin" keyword.'''
#
#    def __init__(self):
#        function_rule.__init__(self)
#        self.identifier = '027'
#        self.solution = 'Ensure a single blank line between the last non-blank line and the "begin" keyword.'
#        self.phase = 3
#
#    def analyze(self, oFile):
#        fCheckForBlanks = False
#        fBlanksFound = False
#        fNonBlanksFound = False
#        fSkipFunction = False
#        iBlankCount = 0
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.insideFunction:
#                if oLine.isFunctionBegin and oLine.isSensitivityListEnd:
#                    fSkipFunction = True
#                if oLine.isSensitivityListEnd and oFile.lines[iLineNumber + 1].isFunctionBegin:
#                    fSkipFunction = True
#                if fSkipFunction:
#                    if oLine.isEndFunction:
#                        fSkipFunction = False
#                    continue
#                if fCheckForBlanks:
#                    if oLine.isBlank:
#                        iBlankCount += 1
#                    if not oLine.isBlank and not oLine.isFunctionBegin:
#                        iBlankCount = 0
#                    if oLine.isFunctionBegin:
#                        if not iBlankCount == 1:
#                            self.add_violation(iLineNumber)
#                        fSkipFunction = True
#                        fCheckForBlanks = False
#                        iBlankCount = 0
#                if oLine.isSensitivityListEnd:
#                    fCheckForBlanks = True

