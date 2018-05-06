'''
This module contains functions for rules to fix issues.
'''
from vsg import line
from vsg import utilities

import re


def indent(self, oLine):
    '''
    Fixes indent violations.

    Parameters:

      self: (rule object)

      oLine: (line object)
    '''
    oLine.update_line(' '*oLine.indentLevel*self.indentSize + oLine.line.lstrip())


def keyword_alignment(self, oFile):
    '''
    Aligns keywords across multiple lines.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)
    '''
    for sKey in self.dFix['violations']:
        iMaximumKeywordColumn = self.dFix['violations'][sKey]['maximumKeywordColumn']
        for iLineNumber in self.dFix['violations'][sKey]['line']:
            iKeywordColumn = self.dFix['violations'][sKey]['line'][iLineNumber]['keywordColumn']
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line[:iKeywordColumn] + ' '*(iMaximumKeywordColumn - iKeywordColumn) + oLine.line[iKeywordColumn:])


def multiline_alignment(self, oFile, iLineNumber):
    '''
    Indents successive lines of multiline statements.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    oLine = oFile.lines[iLineNumber]
    oLine.update_line(' '*self.dFix['violations'][iLineNumber]['column'] + oLine.line.lstrip())


def lower_case(self, oLine, sKeyword):
    '''
    Changes word to lowercase.

    Parameters:

      self: (rule object)

      oLine: (line object)

      sKeyword: (string)
    '''
    utilities.change_word(oLine, sKeyword, sKeyword.lower())


def upper_case(self, oLine, sKeyword):
    '''
    Changes word to lowercase.

    Parameters:

      self: (rule object)

      oLine: (line object)

      sKeyword: (string)
    '''
    if '(' in sKeyword:
        sWord = utilities.remove_parenthesis_from_word(sKeyword)
        utilities.change_word(oLine, sWord, sWord.upper())
    else:
        utilities.change_word(oLine, sKeyword, sKeyword.upper())


def upper_case_with_parenthesis(self, oLine, sKeyword):
    '''
    Changes word to lowercase.

    Parameters:

      self: (rule object)

      oLine: (line object)

      sKeyword: (string)
    '''


def enforce_one_space_after_word(self, oLine, sWord):
    '''
    Adds a space after a word.

    Parameters:

      self: (rule object)

      oLine: (line object)

      sWord: (string)
    '''
    oLine.update_line(re.sub(r'(' + sWord + ')\s*(\S)', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))


def enforce_one_space_before_word(self, oLine, sWord):
    '''
    Adds a space before word.

    Parameters:

      self: (rule object)

      oLine: (line object)

      sWord: (string)
    '''
    oLine.update_line(re.sub(r'(\S)\s*(' + sWord + ')', r'\1 \2', oLine.line, 1, flags=re.IGNORECASE))


def remove_blank_lines_above(self, oFile, iLineNumber, sUnless=None):
    '''
    This function removes blank lines above a linenumber.
    If sUnless is specified, a single blank line will be left if a line with the sUnless attribute is encountered.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sUnless: (string) (optional)
    '''
    while oFile.lines[iLineNumber - 1].isBlank:
        if sUnless:
            if oFile.lines[iLineNumber - 2].__dict__[sUnless]:
                break
        oFile.lines.pop(iLineNumber - 1)
        iLineNumber -= 1


def remove_blank_lines_below(self, oFile, iLineNumber, sUnless=None):
    '''
    This function removes blank lines below a linenumber.
    If sUnless is specified, a single blank line will be left if a line with the sUnless attribute is encountered.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sUnless: (string) (optional)
    '''
    while oFile.lines[iLineNumber + 1].isBlank:
        if sUnless:
            if oFile.lines[iLineNumber + 2].__dict__[sUnless]:
                break
        oFile.lines.pop(iLineNumber + 1)


def insert_blank_line_above(self, oFile, iLineNumber):
    '''
    This function inserts a blank line above the line specified by iLineNumber.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    oFile.lines.insert(iLineNumber, line.blank_line())


def insert_blank_line_below(self, oFile, iLineNumber):
    '''
    This function inserts a blank line below the line specified by iLineNumber.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    oFile.lines.insert(iLineNumber + 1, line.blank_line())


def replace_is_keyword(oFile, iLineNumber):
    '''
    This function removes the is keyword from a line if it starts with is.
    If the line is empty, it is replaced with a blank line.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
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
