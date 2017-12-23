
import copy
import re


def copy_line(oFile, iLineNumber):
    oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))


def split_line_after_word(oFile, iLineNumber, sWord):
    copy_line(oFile, iLineNumber)
    oLine = oFile.lines[iLineNumber]
    iIndex = oLine.line.find(sWord) + len(sWord)
    oLine.update_line(oLine.line[:iIndex])
    oLine = oFile.lines[iLineNumber + 1]
    oLine.update_line(oLine.line[iIndex:])


def split_line_before_word(oFile, iLineNumber, sWord):
    copy_line(oFile, iLineNumber)
    oLine = oFile.lines[iLineNumber]
    iIndex = oLine.line.find(sWord)
    oLine.update_line(oLine.line[:iIndex])
    oLine = oFile.lines[iLineNumber + 1]
    oLine.update_line(oLine.line[iIndex:])


def get_word(oLine, iIndex):
    return oLine.line.split()[iIndex]


def get_first_word(oLine):
    return get_word(oLine, 0)


def change_word(oLine, sWord, sNewWord):
    oLine.line = re.sub(r' ' + sWord + '([\s|;|\(])', r' ' + sNewWord + r'\1', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sWord + '$', ' ' + sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + '$', sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + ' ', sNewWord + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.lineLower = oLine.line.lower()


def remove_text_after_word(sKeyword, sWord):
    if sKeyword in sWord:
        sWord = sWord[:sWord.find(sKeyword)]
    return sWord


def is_vhdl_keyword(sWord):
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
    oLine.update_line(re.sub(r'^(\s*)' + sKeyword, r'\1  ', oLine.line))
    if re.match('^\s*$', oLine.line):
        oLine.update_line('')
        oLine.isBlank = True


def search_for_and_remove_keyword(oFile, iLineNumber, sKeyword):
    iSearchIndex = iLineNumber
    while True:
        iSearchIndex += 1
        oLine = oFile.lines[iSearchIndex]
        if re.match('^\s*' + sKeyword, oLine.line, re.IGNORECASE):
            clear_keyword_from_line(oLine, sKeyword)
            remove_blank_line(oFile, iSearchIndex)
        if not oLine.isBlank:
            break


def remove_comment(sLine):
    if '--' in sLine:
        return sLine[0:sLine.find('--') + len('--')]
    else:
        return sLine


def remove_blank_line(oFile, iLineNumber):
    if oFile.lines[iLineNumber].isBlank:
        oFile.lines.pop(iLineNumber)


def reclassify_line(oFile, iLineNumber):
    if re.match('^\s*return', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
        oFile.lines[iLineNumber].isFunctionReturn = False
        oFile.lines[iLineNumber + 1].isFunctionReturn = True
    elif re.match('^\s*\w+.*:=', oFile.lines[iLineNumber + 1].line, re.IGNORECASE):
        oFile.lines[iLineNumber + 1].insideVariableAssignment = True
        oFile.lines[iLineNumber + 1].isVariableAssignmentEnd = True
        oFile.lines[iLineNumber + 1].isVariableAssignment = True
    else:
        oFile.lines[iLineNumber + 1].insideSequential = True
        oFile.lines[iLineNumber + 1].isSequentialEnd = True
        oFile.lines[iLineNumber + 1].isSequential = True
