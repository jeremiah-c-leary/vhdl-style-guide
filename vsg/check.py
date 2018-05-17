'''
This module contains functions for rules to perform their checks.
'''

import re


def indent(self, oLine, iLineNumber):
    '''
    Adds a violation if the indent of the line does not match the desired level.

    Parameters

      self: (rule object)

      oLine: (line object)

      iLineNumber: (integer)

    '''
    if not oLine.isBlank:
        if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
            self.add_violation(iLineNumber)


def is_no_blank_line_after(self, oFile, iLineNumber, sUnless=None):
    '''
    Adds a violation if the line after iLineNumber is blank.
    This is typically used to compress lines together.

    If sUnless is given, then a violation will not occur if there is a blank line following the line with the attribute given for sUnless.

    Parameters

      self: (rule object)

      oLine: (line object)

      iLineNumber: (integer)

      sUnless: (string) (line attribute)
    '''
    if sUnless:
        if oFile.lines[iLineNumber + 1].isBlank:
            if not oFile.lines[iLineNumber + 2].__dict__[sUnless]:
                self.add_violation(iLineNumber)

    elif oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)


def is_no_blank_line_before(self, oFile, iLineNumber, sUnless=None):
    '''
    Adds a violation if the line before iLineNumber is blank.
    This is typically used to compress lines together.

    If sUnless is given, then a violation will not occur if there is a blank line before the line with the attribute given for sUnless.

    Parameters

      self: (rule object)

      oLine: (line object)

      iLineNumber: (integer)

      sUnless: (string) (line attribute)
    '''
    if sUnless:
        if oFile.lines[iLineNumber - 1].isBlank:
            if not oFile.lines[iLineNumber - 2].__dict__[sUnless]:
                self.add_violation(iLineNumber)
    elif oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)


def is_blank_line_after(self, oFile, iLineNumber):
    '''
    Adds a violation if the line after iLineNumber is not blank.
    This is typically used to compress lines together.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    if not oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)


def is_blank_line_before(self, oFile, iLineNumber):
    '''
    Adds a violation if the line before iLineNumber is not blank.
    This is typically used to compress lines together.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    if not oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)


def keyword_alignment(self, iLineNumber, sKeyword, lGroup):
    '''
    Checks keywords in a group of line objects are aligned in the same column.

    Parameters:

      self: (rule object)

      iLineNumber: (integer)

      sKeyword: (string)

      lGroup: (list of line objects)
    '''
    iKeywordAlignment = None
    iMaximumKeywordColumn = 0
    sViolationRange = str(iLineNumber) + '-' + str(iLineNumber + len(lGroup) - 1)
    self.dFix['violations'][sViolationRange] = {}
    self.dFix['violations'][sViolationRange]['line'] = {}

    for iIndex, oGroupLine in enumerate(lGroup):
        if sKeyword in oGroupLine.line:
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex] = {}
            self.dFix['violations'][sViolationRange]['line'][iLineNumber + iIndex]['keywordColumn'] = oGroupLine.line.find(sKeyword)

            iMaximumKeywordColumn = get_maximum_keyword_column(oGroupLine, sKeyword, iMaximumKeywordColumn)

            iKeywordAlignment = update_keyword_alignment(oGroupLine, sKeyword, iKeywordAlignment)

            if not iKeywordAlignment == oGroupLine.line.find(sKeyword):
                add_range_violation(self, sViolationRange)

    self.dFix['violations'][sViolationRange]['maximumKeywordColumn'] = iMaximumKeywordColumn


def get_maximum_keyword_column(oLine, sKeyword, iMaximumKeywordColumn):
    '''
    Return the highest column count a keyword is found.

    Parameters:

      oLine: (line object)

      sKeyword: (string)

      iMaximumKeywordColumn: (integer)

    Returns: (integer)
    '''
    if oLine.line.find(sKeyword) > iMaximumKeywordColumn:
        return oLine.line.find(sKeyword)
    return iMaximumKeywordColumn


def update_keyword_alignment(oLine, sKeyword, iKeywordAlignment):
    '''
    Returns the column where the keyword was detected.

    Parameters:

      oLine: (line object)

      sKeyword: (string)

      iKeywordAlignment: (integer)

    Returns: (integer)
    '''
    if not iKeywordAlignment:
        return oLine.line.find(sKeyword)
    return iKeywordAlignment


def add_range_violation(self, sViolationRange):
    '''
    Appends a range violation to the violation list if it does not already exist.

    Parameters:

      self: (rule object)

      sViolationRange: (string)
    '''
    if sViolationRange not in self.violations:
        self.add_violation(sViolationRange)


def multiline_alignment(self, iColumn, oLine, iLineNumber):
    '''
    Checks the alignment of multiline statements.

    Parameters:

      self: (rule object)

      iColumn: (integer)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
        self.add_violation(iLineNumber)
        self.dFix['violations'][iLineNumber] = {}
        self.dFix['violations'][iLineNumber]['column'] = iColumn


def is_uppercase(self, sString, iLineNumber):
    '''
    Checks if a string is uppercase.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)
    '''
    if not sString == sString.upper():
        self.add_violation(iLineNumber)


def is_lowercase(self, sString, iLineNumber):
    '''
    Checks if a string is lowercase.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)
    '''
    if not sString == sString.lower():
        self.add_violation(iLineNumber)


def is_single_space_after(self, sString, oLine, iLineNumber):
    '''
    Checks if a single space is after the string given.
    The string is considered a whole word.
    Allowances are made for end of line and semicolons.

    Parameters:

      self: (rule object)

      sString: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not sString.lower() in oLine.lineLower:
        return
    if re.match('^.*' + sString + ';', oLine.lineLower):
        return
    if re.match('^.*' + sString + '$', oLine.lineLower):
        return
    if not re.match('^.*\s+' + sString + '\s\S', oLine.lineLower) and \
       not re.match('^\s*' + sString + '\s\S', oLine.lineLower) and \
       not re.match('^.*\S\s' + sString + '\'', oLine.lineLower):
        self.add_violation(iLineNumber)


def is_single_space_before(self, sString, oLine, iLineNumber):
    '''
    Checks if a single space exists before the string given.
    The string is considered a whole word.

    Parameters:

      self: (rule object)

      sString: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not sString.lower() in oLine.lineLower:
        return
    if not re.match('^.*\S\s' + sString + '\s', oLine.lineNoComment.lower()) and \
       not re.match('^.*\S\s' + sString + '$', oLine.lineNoComment.lower()) and \
       not re.match('^.*\S\s' + sString + '\'', oLine.lineNoComment.lower()):
        self.add_violation(iLineNumber)


def is_single_space_after_character(self, sCharacter, oLine, iLineNumber):
    '''
    Checks if a single space exists after a series of characters.
    NOTE:  The characters will match partial words.

    Parameters:

      self: (rule object)

      sCharacter: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not sCharacter.lower() in oLine.lineLower:
        return
    if not re.match('^.*' + sCharacter.lower() + '\s*--', oLine.lineNoComment):
        if re.match('^.*' + sCharacter.lower() + '$', oLine.lineNoComment):
            return
        if not re.match('^.*' + sCharacter.lower() + '\s\S', oLine.lineLower):
            self.add_violation(iLineNumber)


def is_single_space_before_character(self, sCharacter, oLine, iLineNumber):
    '''
    Checks if a single space exists before a series of characters.
    NOTE:  The characters will match partial words.

    Parameters:

      self: (rule object)

      sCharacter: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    iIndex = oLine.line.find(sCharacter) + len(sCharacter)
    if not re.match('^.*\s' + sCharacter.lower(), oLine.lineNoComment[:iIndex]):
        self.add_violation(iLineNumber)


def indent_of_comments_above(self, oFile, iLineNumber):
    '''
    Checks the indent level of consecutive comment lines above the line number given.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    iIndex = 0
    while iLineNumber - iIndex > 1:
        iIndex += 1
        iPreviousIndex = iLineNumber - iIndex
        if not oFile.lines[iPreviousIndex].isComment:
            break
        else:
            if not oFile.lines[iPreviousIndex].line.index('--') == oFile.lines[iLineNumber].indentLevel * self.indentSize:
                self.add_violation(iPreviousIndex)
                self.dFix['violations'][iPreviousIndex] = oFile.lines[iLineNumber].indentLevel
            else:
                oFile.lines[iPreviousIndex].indentLevel = oFile.lines[iLineNumber].indentLevel


def has_package_name(oLine):
    '''
    Returns boolean if package name is found in line.

    Parameters:

      oLine: (line object)

    Returns: (boolean)

      True if package name exists in line.
      False if package name does not exist in line.
    '''
    lLine = oLine.lineNoComment.lower().split()
    for iIndex, sWord in enumerate(lLine):
        if sWord == 'package':
            if not lLine[iIndex + 1] == '--':
                return True
    return False


def get_package_name(oLine):
    '''
    Returns the package name in the line.

    Parameters

      oLine: (line object)

    Returns: (string)

      Package name or empty string if package name not found.
    '''
    lLine = oLine.lineNoComment.split()
    for iIndex, sWord in enumerate(lLine):
        if sWord.lower() == 'package' and not lLine[iIndex + 1] == '--':
            return lLine[iIndex + 1].rstrip(';')
    return ''
