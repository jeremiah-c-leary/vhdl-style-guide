
import re


def indent(self, oLine, iLineNumber):
    '''Adds a violation if the indent of the line does not match the desired level.'''
    if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
        self.add_violation(iLineNumber)


def is_no_blank_line_after(self, oFile, iLineNumber):
    '''Adds a violation if the line after iLineNumber is blank.
       This is typically used to compress lines together.'''
    if oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)


def is_no_blank_line_before(self, oFile, iLineNumber):
    '''Adds a violation if the line before iLineNumber is blank.
       This is typically used to compress lines together.'''
    if oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)


def is_blank_line_after(self, oFile, iLineNumber):
    '''Adds a violation if the line after iLineNumber is not blank.
       This is typically used to compress lines together.'''
    if not oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)


def is_blank_line_before(self, oFile, iLineNumber):
    '''Adds a violation if the line before iLineNumber is not blank.
       This is typically used to compress lines together.'''
    if not oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)


def keyword_alignment(self, iStartGroupIndex, sKeyword, lGroup):
    iKeywordAlignment = None
    iMaximumKeywordColumn = 0
    sViolationRange = str(iStartGroupIndex) + '-' + str(iStartGroupIndex + len(lGroup) - 1)
    self.dFix['violations'][sViolationRange] = {}
    self.dFix['violations'][sViolationRange]['line'] = {}

    for iIndex, oGroupLine in enumerate(lGroup):
        if sKeyword in oGroupLine.line:
            self.dFix['violations'][sViolationRange]['line'][iStartGroupIndex + iIndex] = {}
            self.dFix['violations'][sViolationRange]['line'][iStartGroupIndex + iIndex]['keywordColumn'] = oGroupLine.line.find(sKeyword)

            iMaximumKeywordColumn = get_maximum_keyword_column(oGroupLine, sKeyword, iMaximumKeywordColumn)

            iKeywordAlignment = update_keyword_alignment(oGroupLine, sKeyword, iKeywordAlignment)

            if not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                add_range_violation(self, sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumKeywordColumn'] = iMaximumKeywordColumn


def get_maximum_keyword_column(oLine, sKeyword, iMaximumKeywordColumn):
    if oLine.line.find(sKeyword) > iMaximumKeywordColumn:
        return oLine.line.find(sKeyword)
    return iMaximumKeywordColumn


def update_keyword_alignment(oLine, sKeyword, iKeywordAlignment):
    if not iKeywordAlignment:
        return oLine.line.find(sKeyword)
    return iKeywordAlignment


def add_range_violation(self, sViolationRange):
        if sViolationRange not in self.violations:
            self.add_violation(sViolationRange)


def multiline_alignment(self, iColumn, oLine, iLineNumber):
    if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
        self.add_violation(iLineNumber)
        self.dFix['violations'][iLineNumber] = {}
        self.dFix['violations'][iLineNumber]['column'] = iColumn


def is_uppercase(self, sString, iLineNumber):
    if not sString == sString.upper():
        self.add_violation(iLineNumber)


def is_lowercase(self, sString, iLineNumber):
    if not sString == sString.lower():
        self.add_violation(iLineNumber)

def is_word_lowercase(oLine, sString, iLineNumber):
    if not sString == sString.lower():
        self.add_violation(iLineNumber)


def is_single_space_after(self, sString, oLine, iLineNumber):
    if not re.match('^.*\s+' + sString + '\s\S', oLine.lineLower) and \
       not re.match('^\s*' + sString + '\s\S', oLine.lineLower):
        self.add_violation(iLineNumber)


def is_single_space_before(self, sString, oLine, iLineNumber):
    if not re.match('^.*\S\s' + sString + '\s', oLine.lineLower) and \
       not re.match('^.*\S\s' + sString + '$', oLine.lineLower):
        self.add_violation(iLineNumber)
