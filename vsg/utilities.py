'''
This module provides functions for rules to use.
'''
import copy
import re


def copy_line(oFile, iLineNumber):
    '''
    Creates a copy of the line at iLineNumber and inserts it below iLineNumber.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))


def split_line_after_word(oFile, iLineNumber, sWord):
    '''
    Splits the line after the word given and inserts it after the current line.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sWord: (string)
    '''
    copy_line(oFile, iLineNumber)
    oLine = oFile.lines[iLineNumber]
    iIndex = oLine.line.find(sWord) + len(sWord)
    oLine.update_line(oLine.line[:iIndex])
    oLine = oFile.lines[iLineNumber + 1]
    oLine.update_line(oLine.line[iIndex:])


def split_line_before_word(oFile, iLineNumber, sWord):
    '''
    Splits the line before the word given and inserts it after the current line.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sWord: (string)
    '''
    copy_line(oFile, iLineNumber)
    oLine = oFile.lines[iLineNumber]
    iIndex = oLine.line.find(sWord)
    oLine.update_line(oLine.line[:iIndex])
    oLine = oFile.lines[iLineNumber + 1]
    oLine.update_line(oLine.line[iIndex:])


def get_word(oLine, iIndex):
    '''
    Returns a word from a line at iIndex.

    Parameters:

      oLine: (line object)

      iIndex: (integer)

    Returns: (string)
    '''
    return oLine.line.split()[iIndex]


def get_first_word(oLine):
    '''
    Returns the first word from a line at iIndex.

    Parameters:

      oLine: (line object)

    Returns: (string)
    '''
    return get_word(oLine, 0)


def change_word(oLine, sWord, sNewWord):
    '''
    Changes one word in the line to another.

    Parameters:

      oLine: (line object)

      sWord: (string)

      sNewWord: (string)
    '''
    oLine.line = re.sub(r' ' + sWord + '([\s|;|\(])', r' ' + sNewWord + r'\1', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sWord + '$', ' ' + sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + '$', sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + ' ', sNewWord + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.update_line(oLine.line)


def remove_text_after_word(sKeyword, sWord):
    '''
    Removes all text after a keyword.

    Parameters:

      sKeyword: (string)

      sWord: (string)
    '''
    if sKeyword in sWord:
        sWord = sWord[:sWord.find(sKeyword)]
    return sWord


def is_vhdl_keyword(sWord):
    '''
    Returns True if given word is a VHDL keyword.

    Returns False if given word is not a VHDL keyword.

    Parameters:

      sWord: (string)

    Returns: (boolean)
    '''
    lKeywords = []
    lKeywords.append('std_logic')
    lKeywords.append('std_logic_vector')
    lKeywords.append('integer')
    lKeywords.append('signed')
    lKeywords.append('unsigned')
    lKeywords.append('natural')
    lKeywords.append('std_ulogic')

    sWord = remove_text_after_word(')', sWord)
    sWord = remove_text_after_word(';', sWord)

    if sWord.lower() in lKeywords:
        return True
    else:
        return False


def clear_keyword_from_line(oLine, sKeyword):
    '''
    Removes a keyword from a line.

    Parameters:

      oLine: (line object)

      sKeyword: (string)
    '''
    oLine.update_line(re.sub(r'^(\s*)' + sKeyword, r'\1  ', oLine.line))
    if re.match('^\s*$', oLine.line):
        oLine.update_line('')
        oLine.isBlank = True


def search_for_and_remove_keyword(oFile, iLineNumber, sKeyword):
    '''
    Searches for a keyword on lines below the current line and removes it if discovered.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sKeyword: (string)
    '''
    iSearchIndex = iLineNumber
    while True:
        iSearchIndex += 1
        oLine = oFile.lines[iSearchIndex]
        if re.match('^\s*' + sKeyword, oLine.line, re.IGNORECASE):
            clear_keyword_from_line(oLine, sKeyword)
            remove_blank_line(oFile, iSearchIndex)
        if not oLine.isBlank:
            break


def remove_comment(sString):
    '''
    Returns a string without comments.

    Parameters:

      sString: (string)

    Returns: (string)
    '''
    if '--' in sString:
        return sString[0:sString.find('--') + len('--')]
    else:
        return sString


def remove_blank_line(oFile, iLineNumber):
    '''
    Removes a line if it is blank.

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    if oFile.lines[iLineNumber].isBlank:
        oFile.lines.pop(iLineNumber)


def reclassify_line(oFile, iLineNumber):
    '''
    Updates the following attributes on the current and next line:

       * isFunctionReturn
       * insideVariableAssignment
       * isVariableAssignmentEnd
       * isVariableAssignment
       * insideSequential
       * isSequentialEnd
       * isSequential
       * hasComment
       * hasInlineComment
       * commentColumn

    Parameters:

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    if re.match('^\s*return', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
        oFile.lines[iLineNumber].isFunctionReturn = False
        oFile.lines[iLineNumber + 1].isFunctionReturn = True
    elif re.match('^\s*\w+.*:=', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
        oFile.lines[iLineNumber + 1].insideVariableAssignment = True
        oFile.lines[iLineNumber + 1].isVariableAssignmentEnd = True
        oFile.lines[iLineNumber + 1].isVariableAssignment = True
    elif re.match('^\s*null', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
        oFile.lines[iLineNumber + 1].insideSequential = False
        oFile.lines[iLineNumber + 1].isSequentialEnd = False
        oFile.lines[iLineNumber + 1].isSequential = False
        oFile.lines[iLineNumber + 1].sequentialAlignmentColumn = None
    else:
        oFile.lines[iLineNumber + 1].insideSequential = True
        oFile.lines[iLineNumber + 1].isSequentialEnd = True
        oFile.lines[iLineNumber + 1].isSequential = True

    if not '--' in oFile.lines[iLineNumber].line:
        oFile.lines[iLineNumber].hasComment = False
        oFile.lines[iLineNumber].hasInlineComment = False
        oFile.lines[iLineNumber].commentColumn = None

    if '--' in oFile.lines[iLineNumber + 1].line:
        oFile.lines[iLineNumber + 1].hasComment = True
        oFile.lines[iLineNumber + 1].hasInlineComment = True
        oFile.lines[iLineNumber + 1].commentColumn = oFile.lines[iLineNumber + 1].line.find('--')


def remove_parenthesis_from_word(sWord):
    '''
    Removes parenthesis from words:

        Hello(there) => Hello
        Hello        => Hello

    Parameters:

      sWord: (string)

    Returns: (string)
    '''
    if '(' in sWord:
        return sWord.split('(')[0]

    return sWord
