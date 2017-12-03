
import copy
import re


def split_line_after_word(oFile, iLineNumber, sWord):
    oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
    oLine = oFile.lines[iLineNumber]
    iIndex = oLine.line.find(sWord) + len(sWord)
    oLine.update_line(oLine.line[:iIndex])
    oLine = oFile.lines[iLineNumber + 1]
    oLine.update_line(oLine.line[iIndex:])


def split_line_before_word(oFile, iLineNumber, sWord):
    oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
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
    oLine.line = re.sub(' ' + sWord + ' ', ' ' + sNewWord + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sWord + '$', ' ' + sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + '$', sNewWord, oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sWord + ' ', sNewWord + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sWord + ';', ' ' + sNewWord + ';', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sWord + '\(', ' ' + sNewWord + '(', oLine.line, 1, flags=re.IGNORECASE)
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

    sWord = remove_text_after_word(')', sWord)
    sWord = remove_text_after_word(';', sWord)

    if sWord.lower() in lKeywords:
        return True
    else:
        return False
