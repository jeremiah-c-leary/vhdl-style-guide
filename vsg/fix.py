
from vsg import line
from vsg import utilities

import re


def indent(self, oLine):
    '''Fixes indent violations.'''
    oLine.update_line(' '*oLine.indentLevel*self.indentSize + oLine.line.lstrip())


def keyword_alignment(self, oFile):
    for sKey in self.dFix['violations']:
        iMaximumKeywordColumn = self.dFix['violations'][sKey]['maximumKeywordColumn']
        for iLineNumber in self.dFix['violations'][sKey]['line']:
            iKeywordColumn = self.dFix['violations'][sKey]['line'][iLineNumber]['keywordColumn']
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line[:iKeywordColumn] + ' '*(iMaximumKeywordColumn - iKeywordColumn) + oLine.line[iKeywordColumn:])


def multiline_alignment(self, oFile, iLineNumber):
    oLine = oFile.lines[iLineNumber]
    oLine.update_line(' '*self.dFix['violations'][iLineNumber]['column'] + oLine.line.lstrip())


def lower_case(self, oLine, sKeyword):
    utilities.change_word(oLine, sKeyword, sKeyword.lower())


def upper_case(self, oLine, sKeyword):
    utilities.change_word(oLine, sKeyword, sKeyword.upper())


def enforce_one_space_after_word(self, oLine, sWord):
    oLine.update_line(re.sub(r'(' + sWord + ')\s*(\S)', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))


def enforce_one_space_before_word(self, oLine, sWord):
    oLine.update_line(re.sub(r'(\S)\s*(' + sWord + ')', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))


def remove_blank_lines_above(self, oFile, iLineNumber):
    while oFile.lines[iLineNumber - 1].isBlank:
        oFile.lines.pop(iLineNumber - 1)
        iLineNumber -= 1


def remove_blank_lines_below(self, oFile, iLineNumber):
    while oFile.lines[iLineNumber + 1].isBlank:
        oFile.lines.pop(iLineNumber + 1)


def insert_blank_line_above(self, oFile, iLineNumber):
    oFile.lines.insert(iLineNumber, line.blank_line())


def insert_blank_line_below(self, oFile, iLineNumber):
    oFile.lines.insert(iLineNumber + 1, line.blank_line())


def replace_is_keyword(oFile, iLineNumber):
    iSearchIndex = iLineNumber
    while True:
        iSearchIndex += 1
        oLine = oFile.lines[iSearchIndex]
        if re.match('^\s*is', oLine.line, re.IGNORECASE):
            oLine.line = re.sub(r'^(\s*)is', r'\1  ', oLine.line)
            oLine.lineLower = oLine.line.lower()
            if re.match('^\s*$', oLine.line):
                oLine.line = ''
                oLine.lineLower = ''
                oLine.isBlank = True
        if oFile.lines[iSearchIndex].isGenericKeyword or oFile.lines[iSearchIndex].isPortKeyword:
            break
