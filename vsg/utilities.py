
import copy

def split_line_after_word(self, oFile, iLineNumber, sWord):
        oFile.lines.insert(iLineNumber + 1,copy.deepcopy(oFile.lines[iLineNumber]))
        oLine = oFile.lines[iLineNumber]
        iIndex = oLine.line.find(sWord) + len(sWord)
        oLine.update_line(oLine.line[:iIndex])
        oLine = oFile.lines[iLineNumber + 1]
        oLine.update_line(oLine.line[iIndex:])

def split_line_before_word(self, oFile, iLineNumber, sWord):
        oFile.lines.insert(iLineNumber + 1,copy.deepcopy(oFile.lines[iLineNumber]))
        oLine = oFile.lines[iLineNumber]
        iIndex = oLine.line.find(sWord)
        oLine.update_line(oLine.line[:iIndex])
        oLine = oFile.lines[iLineNumber + 1]
        oLine.update_line(oLine.line[iIndex:])

def get_word(oLine, iIndex):
    return oLine.line.split()[iIndex]

def get_first_word(oLine):
    return get_word(oLine, 0)

