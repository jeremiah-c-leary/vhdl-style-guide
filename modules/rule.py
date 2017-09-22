
import re

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2

    def report_violations(self,filename):
        if len(self.violations) > 0:
            print (self.name + '_' + self.identifier + ':  ' + self.solution + '...FAILED')
            for violation in self.violations:
                print '    ' + str(violation)
            return 1
        else:
            return 0
#            print (self.name + '_' + self.identifier + ':  ' + self.solution + '...PASSED')


    def add_violation(self, lineNumber):
        self.violations.append(lineNumber)

    def _isLowercase(self, sString):
        if sString == sString.lower():
            return True
        else:
            return False

    def _check_indent(self, oLine, iLineNumber):
        '''Adds a violation if the indent of the line does not match the desired level.'''
        if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
            self.add_violation(iLineNumber)

    def _is_no_blank_line_after(self, oFile, iLineNumber): 
        '''Adds a violation if the line after iLineNumber is blank.
           This is typically used to compress lines together.'''
        if oFile.lines[iLineNumber + 1].isBlank:
            self.add_violation(iLineNumber)

    def _is_no_blank_line_before(self, oFile, iLineNumber):
        '''Adds a violation if the line before iLineNumber is blank.
           This is typically used to compress lines together.'''
        if oFile.lines[iLineNumber - 1].isBlank:
            self.add_violation(iLineNumber)

    def _is_blank_line_after(self, oFile, iLineNumber): 
        '''Adds a violation if the line after iLineNumber is not blank.
           This is typically used to compress lines together.'''
        if not oFile.lines[iLineNumber + 1].isBlank:
            self.add_violation(iLineNumber)

    def _is_blank_line_before(self, oFile, iLineNumber):
        '''Adds a violation if the line before iLineNumber is not blank.
           This is typically used to compress lines together.'''
        if not oFile.lines[iLineNumber - 1].isBlank:
            self.add_violation(iLineNumber)

    def _check_multiline_alignment(self, iColumn, oLine, iLineNumber):
        if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
            self.add_violation(iLineNumber)

    def _is_uppercase(self, sString, iLineNumber):
        if not sString == sString.upper():
            self.add_violation(iLineNumber)

    def _is_lowercase(self, sString, iLineNumber):
        if not sString == sString.lower():
            self.add_violation(iLineNumber)

    def _get_word(self, oLine, iIndex):
        return oLine.line.split()[iIndex]

    def _get_first_word(self, oLine):
        return self._get_word(oLine, 0)

    def _is_single_space_after(self, sString, oLine, iLineNumber):
        if not re.match('^.*\s+' + sString + '\s\S', oLine.lineLower):
            self.add_violation(iLineNumber)

    def _is_single_space_before(self, sString, oLine, iLineNumber):
        if not re.match('^.*\S\s' + sString + '\s', oLine.lineLower) and \
           not re.match('^.*\S\s' + sString + '$', oLine.lineLower):
            self.add_violation(iLineNumber)

    def _check_keyword_alignment(self, iStartGroupIndex, sKeyword, lGroup):
        iKeywordAlignment = None
        for oGroupLine in lGroup:
            if sKeyword in oGroupLine.line:
                if not iKeywordAlignment:
                    iKeywordAlignment = oGroupLine.line.find(sKeyword)
                elif not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                    self.add_violation(str(iStartGroupIndex) + '-' + str(iStartGroupIndex + len(lGroup) - 1))
                    break

