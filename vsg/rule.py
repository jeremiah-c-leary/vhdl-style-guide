
from vsg import line
import re
import copy

class rule():

    def __init__(self, name=None, identifier=None):
        self.name = name
        self.identifier = identifier
        self.solution = None
        self.violations = []
        self.indentSize = 2
        self.phase = None
        self.disable = False
        self.fixable = True
        self.dFix = {}
        self.dFix['violations'] = {}

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

        self._configure_global_rule_attributes(dConfiguration)
        self._configure_rule_attributes(dConfiguration)

    def report_violations(self, iLineNumber):
        if iLineNumber in self.violations:
            
            print ('  ' + (self.name + '_' + self.identifier).ljust(25) + ' | ' + str(iLineNumber).rjust(10) + ' | ' + self.solution)
            return 1
        else:
            for sViolation in self.violations:
                if str(sViolation).startswith(str(iLineNumber) + '-'):
                    print ('  ' + (self.name + '_' + self.identifier).ljust(25) + ' | ' + sViolation.rjust(10) + ' | ' + self.solution)
                    return 1
            return 0

    def fix(self, oFile):
        self.analyze(oFile)
        self._fix_violations(oFile)
        self._clear_violations()

    def _fix_violations(self, oFile):
        return

    def add_violation(self, lineNumber):
        self.violations.append(lineNumber)

    def _clear_violations(self):
        self.violations = []
        self.dFix = {}
        self.dFix['violations'] = {}

    def _fix_indent(self, oLine):
        '''Fixes indent violations.'''
        oLine.update_line(' '*oLine.indentLevel*self.indentSize + oLine.line.lstrip())

    def _check_multiline_alignment(self, iColumn, oLine, iLineNumber):
        if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
            self.add_violation(iLineNumber)
            self.dFix['violations'][iLineNumber] = {}
            self.dFix['violations'][iLineNumber]['column'] = iColumn

    def _fix_multiline_alignment(self, oFile, iLineNumber):
        oLine = oFile.lines[iLineNumber]
        oLine.update_line(' '*self.dFix['violations'][iLineNumber]['column'] + oLine.line.lstrip())

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
        iMaximumKeywordColumn = 0

        sViolationRange = str(iStartGroupIndex) + '-' + str(iStartGroupIndex + len(lGroup) - 1)
        self.dFix['violations'][sViolationRange] = {}
        self.dFix['violations'][sViolationRange]['line'] = {}
        for iIndex, oGroupLine in enumerate(lGroup):
            if sKeyword in oGroupLine.line:
                self.dFix['violations'][sViolationRange]['line'][iStartGroupIndex + iIndex] = {}
    
                self.dFix['violations'][sViolationRange]['line'][iStartGroupIndex + iIndex]['keywordColumn'] = oGroupLine.line.find(sKeyword)
                if oGroupLine.line.find(sKeyword) > iMaximumKeywordColumn:
                    iMaximumKeywordColumn = oGroupLine.line.find(sKeyword)
       
                if not iKeywordAlignment:
                    iKeywordAlignment = oGroupLine.line.find(sKeyword)
                elif not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                    if not sViolationRange in self.violations:
                        self.add_violation(sViolationRange)
                    
        self.dFix['violations'][sViolationRange]['maximumKeywordColumn'] = iMaximumKeywordColumn

    def _fix_keyword_alignment(self, oFile):
        for sKey in self.dFix['violations']:
            iMaximumKeywordColumn = self.dFix['violations'][sKey]['maximumKeywordColumn']
            for iLineNumber in self.dFix['violations'][sKey]['line']:
                iKeywordColumn = self.dFix['violations'][sKey]['line'][iLineNumber]['keywordColumn']
                oLine = oFile.lines[iLineNumber]
                oLine.update_line(oLine.line[:iKeywordColumn] + ' '*(iMaximumKeywordColumn - iKeywordColumn) + oLine.line[iKeywordColumn:])

    def _lower_case(self, oLine, sKeyword):
        oLine.line = re.sub(' ' + sKeyword + ' ', ' ' + sKeyword.lower() + ' ', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + '$', ' ' + sKeyword.lower(), oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub('^' + sKeyword + '$', sKeyword.lower(), oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub('^' + sKeyword + ' ', sKeyword.lower() + ' ', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + ';', ' ' + sKeyword.lower() + ';', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + '\(', ' ' + sKeyword.lower() + '(', oLine.line, 1, flags=re.IGNORECASE)
        oLine.lineLower = oLine.line.lower()
    
    def _upper_case(self, oLine, sKeyword):
        oLine.line = re.sub(' ' + sKeyword + ' ', ' ' + sKeyword.upper() + ' ', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + '$', ' ' + sKeyword.upper(), oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub('^' + sKeyword + '$', sKeyword.upper(), oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub('^' + sKeyword + ' ', sKeyword.upper() + ' ', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + ';', ' ' + sKeyword.upper() + ';', oLine.line, 1, flags=re.IGNORECASE)
        oLine.line = re.sub(' ' + sKeyword + '\(', ' ' + sKeyword.upper() + '(', oLine.line, 1, flags=re.IGNORECASE)
        oLine.lineLower = oLine.line.lower()
    
    def _enforce_one_space_after_word(self, oLine, sWord):
        oLine.update_line(re.sub(r'(' + sWord + ')\s*(\S)', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))

    def _enforce_one_space_before_word(self, oLine, sWord):
        oLine.update_line(re.sub(r'(\S)\s*(' + sWord + ')', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))

    def _remove_blank_lines_above(self, oFile, iLineNumber):
        while oFile.lines[iLineNumber - 1].isBlank:
            oFile.lines.pop(iLineNumber - 1)
            iLineNumber -= 1

    def _remove_blank_lines_below(self, oFile, iLineNumber):
        while oFile.lines[iLineNumber + 1].isBlank:
            oFile.lines.pop(iLineNumber + 1)

    def _insert_blank_line_above(self, oFile, iLineNumber):
        oFile.lines.insert(iLineNumber, line.blank_line())

    def _insert_blank_line_below(self, oFile, iLineNumber):
        oFile.lines.insert(iLineNumber + 1, line.blank_line())

    def _split_line_after_word(self, oFile, iLineNumber, sWord):
            oFile.lines.insert(iLineNumber + 1,copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.line.find(sWord) + len(sWord)
            oLine.update_line(oLine.line[:iIndex])
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line(oLine.line[iIndex:])

    def _split_line_before_word(self, oFile, iLineNumber, sWord):
            oFile.lines.insert(iLineNumber + 1,copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.line.find(sWord)
            oLine.update_line(oLine.line[:iIndex])
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line(oLine.line[iIndex:])

    def _configure_global_rule_attributes(self, dConfiguration):
        try:
            for sAttributeName in dConfiguration['rule']['global']:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule']['global'][sAttributeName]
        except KeyError:
            pass

    def _configure_rule_attributes(self, dConfiguration):
        try:
            for sAttributeName in dConfiguration['rule'][self.name + '_' + self.identifier]:
                if sAttributeName in self.__dict__:
                    self.__dict__[sAttributeName] = dConfiguration['rule'][self.name + '_' + self.identifier][sAttributeName]
        except KeyError:
            pass
