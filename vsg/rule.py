
import re

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2
        self.phase = None
        self.disable = False

    def configure(self, dConfiguration):
        '''Configures attributes on rules using a dictionary of the following form:

            dConfiguration['rule'] = {}
            dConfiguration['rule']['xyz_001'] = {}
            dConfiguration['rule']['xyz_001']['disable'] = True
            dConfiguration['rule']['xyz_001']['solution'] = 'This is the new solution'
            dConfiguration['rule']['xyz_002'] = {}
            dConfiguration['rule']['xyz_002']['disable'] = False
            dConfiguration['rule']['global'] = {}
            dConfiguration['rule']['global']['indentSize'] = 4

          The rule:global dictionary will apply to all rules.
          Individual rule attributes can be modified with [self.name_self.identifier].
        '''

        try:
            for sAttributeName in dConfiguration['rule']['global']:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule']['global'][sAttributeName]
        except KeyError:
            pass

        try:
            for sAttributeName in dConfiguration['rule'][self.name + '_' + self.identifier]:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule'][self.name + '_' + self.identifier][sAttributeName]
        except KeyError:
            pass

    def report_violations(self, iLineNumber):
        if len(self.violations) > 0:
            if iLineNumber in self.violations:
                
                print ('  ' + (self.name + '_' + self.identifier).ljust(25) + ' | ' + str(iLineNumber).rjust(10) + ' | ' + self.solution)
                return 1
            elif not isinstance(self.violations[0], int):
                for sViolation in self.violations:
                    if sViolation.startswith(str(iLineNumber) + '-'):
                        print ('  ' + (self.name + '_' + self.identifier).ljust(25) + ' | ' + sViolation.rjust(10) + ' | ' + self.solution)
                return 1
            else:
                return 0
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

