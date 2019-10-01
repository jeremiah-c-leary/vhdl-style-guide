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


def change_word(oLine, sWord, sNewWord, iMax=1):
    '''
    Changes one word in the line to another.

    Parameters:

      oLine: (line object)

      sWord: (string)

      sNewWord: (string)
    '''
    sLine = oLine.line
    tLine = re.subn(r'\b' + sWord + r'\b', sNewWord, sLine, iMax, flags=re.IGNORECASE)
    sLine = tLine[0]
    if tLine[1] == 0:
        tLine = re.subn(' ' + sWord + ';', sNewWord + ';', sLine, iMax, flags=re.IGNORECASE)
        sLine = tLine[0]
    if tLine[1] == 0:
        tLine = re.subn(sWord + '$', sNewWord, sLine, iMax, flags=re.IGNORECASE)
        sLine = tLine[0]

#    tLine = re.subn(r' ' + sWord + '([\s|;|:|\(])', r' ' + sNewWord + r'\1', sLine, iMax, flags=re.IGNORECASE)
#    if tLine[1] == 0:
#    if tLine[1] == 0:
#        tLine = re.subn('^' + sWord + '$', sNewWord, sLine, iMax, flags=re.IGNORECASE)
#        sLine = tLine[0]
#    if tLine[1] == 0:
#        tLine = re.subn('^' + sWord + ' ', sNewWord + ' ', sLine, iMax, flags=re.IGNORECASE)
#        sLine = tLine[0]
#    if tLine[1] == 0:
#        tLine = re.subn('\(' + sWord + '\)', '(' + sNewWord + ')', sLine, iMax, flags=re.IGNORECASE)
#        sLine = tLine[0]
#    if tLine[1] == 0:
#        tLine = re.subn('\(' + sWord + '\s', '(' + sNewWord + ' ', sLine, iMax, flags=re.IGNORECASE)
#        sLine = tLine[0]
#    if tLine[1] == 0:
#        tLine = re.subn(sWord + ',', sNewWord + ',', sLine, iMax, flags=re.IGNORECASE)
#        sLine = tLine[0]
    sLine = tLine[0]
    oLine.update_line(sLine)


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
    lKeywords.append('event')
    lKeywords.append('is')
    lKeywords.append('end')
    lKeywords.append('entity')
    lKeywords.append('architecture')
    lKeywords.append('begin')
    lKeywords.append('process')
    lKeywords.append('downto')
    lKeywords.append('others')
    lKeywords.append('signal')
    lKeywords.append('else')
    lKeywords.append('when')
    lKeywords.append('port')
    lKeywords.append('map')
    lKeywords.append('generic')
    lKeywords.append('abs')
    lKeywords.append('library')
    lKeywords.append('postponed')
    lKeywords.append('srl')
    lKeywords.append('access')
    lKeywords.append('linkage')
    lKeywords.append('procedure')
    lKeywords.append('subtype')
    lKeywords.append('after')
    lKeywords.append('elsif')
    lKeywords.append('literal')
    lKeywords.append('then')
    lKeywords.append('alias')
    lKeywords.append('loop')
    lKeywords.append('pure')
    lKeywords.append('to')
    lKeywords.append('all')
    lKeywords.append('range')
    lKeywords.append('transport')
    lKeywords.append('and')
    lKeywords.append('exit')
    lKeywords.append('mod')
    lKeywords.append('record')
    lKeywords.append('type')
    lKeywords.append('file')
    lKeywords.append('nand')
    lKeywords.append('register')
    lKeywords.append('unaffected')
    lKeywords.append('array')
    lKeywords.append('for')
    lKeywords.append('new')
    lKeywords.append('reject')
    lKeywords.append('units')
    lKeywords.append('assert')
    lKeywords.append('function')
    lKeywords.append('next')
    lKeywords.append('rem')
    lKeywords.append('until')
    lKeywords.append('attribute')
    lKeywords.append('generate')
    lKeywords.append('nor')
    lKeywords.append('report')
    lKeywords.append('use')
    lKeywords.append('not')
    lKeywords.append('return')
    lKeywords.append('variable')
    lKeywords.append('block')
    lKeywords.append('group')
    lKeywords.append('null')
    lKeywords.append('rol')
    lKeywords.append('wait')
    lKeywords.append('body')
    lKeywords.append('guarded')
    lKeywords.append('of')
    lKeywords.append('ror')
    lKeywords.append('buffer')
    lKeywords.append('if')
    lKeywords.append('on')
    lKeywords.append('select')
    lKeywords.append('while')
    lKeywords.append('bus')
    lKeywords.append('impure')
    lKeywords.append('open')
    lKeywords.append('severity')
    lKeywords.append('with')
    lKeywords.append('case')
    lKeywords.append('in')
    lKeywords.append('or')
    lKeywords.append('shared')
    lKeywords.append('xnor')
    lKeywords.append('component')
    lKeywords.append('inertial')
    lKeywords.append('xor')
    lKeywords.append('configuration')
    lKeywords.append('inout')
    lKeywords.append('out')
    lKeywords.append('sla')
    lKeywords.append('constant')
    lKeywords.append('package')
    lKeywords.append('sll')
    lKeywords.append('disconnect')
    lKeywords.append('label')
    lKeywords.append('sra')

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

    if '--' not in oFile.lines[iLineNumber].line:
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


def strip_semicolon_from_word(sWord):
    '''
    Removes trailing semicolon from a word:

        case;   => case
        entity; => entity

    Parameters:

      sWord: (string)

    Returns: (string)
    '''
    if ';' == sWord[-1]:
        return sWord[0:-1]

    return sWord


def is_port_mode(sWord):
    '''
    Returns True if given word is a valid port mode.

    Returns False if given word is not a valid port mode.

    Parameters:

      sWord: (string)

    Returns: (boolean)
    '''
    lKeywords = []
    lKeywords.append('in')
    lKeywords.append('out')
    lKeywords.append('inout')
    lKeywords.append('buffer')
    lKeywords.append('linkage')

    if sWord.lower() in lKeywords:
        return True
    else:
        return False


def end_of_line_index(oLine):
    '''
    Finds the end of the code on a line ignoring comments.
    Returns the index of the last code character.

    Parameters:

      oLine: (line object)

    Returns: (integer)
    '''

    sLine = remove_comment(oLine.line).replace('--', '')
    for iIndex, sChar in enumerate(sLine[::-1]):
        if not sChar == ' ':
            return len(sLine) - iIndex


def remove_closing_parenthesis_and_semicolon(oLine):
    '''
    Parameters:

      oLine: (line object)

    Returns: (line object)
    '''
    return re.sub(r'\)(\s*);', r' \1 ', oLine)


def extract_non_keywords(sString):
    '''
    Returns a keyword list with the following removed:
       :'s
       commas
       semicolons
       vhdl keywords
       double quotes
       numbers
       ticks
       comments

    Parameters:

       sString: (string)

    Returns: (list of strings)
    '''
    lReturn = []
    sMyString = remove_comment(sString).replace('--', ' ')
    sMyString = sMyString.replace(':', ' ')
    sMyString = sMyString.replace(',', ' ')
    sMyString = sMyString.replace('\'', ' ')
    sMyString = sMyString.replace('(', ' ')
    sMyString = sMyString.replace(')', ' ')
    sMyString = sMyString.replace(';', ' ')
    sMyString = sMyString.replace('=', ' ')
    sMyString = sMyString.replace('>', ' ')
    sMyString = sMyString.replace('<', ' ')
    sMyString = sMyString.replace('&', ' ')
    sMyString = sMyString.replace('*', ' ')
    sMyString = sMyString.replace('-', ' ')
    sMyString = sMyString.replace('+', ' ')
    sMyString = sMyString.replace('/', ' ')
    sMyString = re.sub('x"\S+"', ' ', sMyString)
    sMyString = re.sub('X"\S+"', ' ', sMyString)

    for sWord in sMyString.split():
        if re.match('[0-9]+', sWord):
            continue
        if not is_vhdl_keyword(sWord):
            lReturn.append(sWord)

    return lReturn


def extract_class_identifier_list(sClass, oLine):
    '''
    Returns a list of signals in a signal declaration.

    Parameters:

       sClass: (class according to the VHDL standard)

       oLine: (line object)

    Returns: (list of strings)
    '''
    if sClass not in ['constant', 'variable', 'signal', 'file']:
        raise Exception("sClass must be one of: constant, variable, signal, file")

    sLine = oLine.line.replace(';', '')
    sLine = sLine.split(':')[0]
    sLine = sLine.replace(',', ' ').split()
    if sLine[0].lower() == sClass:
        sLine = sLine[1:]

    return sLine


def extract_type_name(oLine):
    '''
    Returns the name of a type in a type declaration.

    Parameters:

       oLine: (line object)

    Returns: (string)
    '''
    sLine = oLine.line.split(':')[0]
    return sLine.split()[1]


def remove_comment_attributes_from_line(oLine):
    '''
    Sets all comment attributes on a line to indicate no comment is present.

    Parameters:
    
        oLine: (line object)
    '''
    oLine.isComment = False
    oLine.hasComment = False
    oLine.hasInlineComment = False
    oLine.commentColumn = None
