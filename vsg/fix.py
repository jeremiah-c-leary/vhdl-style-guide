
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
    oLine.line = re.sub(' ' + sKeyword + ' ', ' ' + sKeyword.lower() + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + '$', ' ' + sKeyword.lower(), oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sKeyword + '$', sKeyword.lower(), oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sKeyword + ' ', sKeyword.lower() + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + ';', ' ' + sKeyword.lower() + ';', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + '\(', ' ' + sKeyword.lower() + '(', oLine.line, 1, flags=re.IGNORECASE)
    oLine.lineLower = oLine.line.lower()

def upper_case(self, oLine, sKeyword):
    oLine.line = re.sub(' ' + sKeyword + ' ', ' ' + sKeyword.upper() + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + '$', ' ' + sKeyword.upper(), oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sKeyword + '$', sKeyword.upper(), oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub('^' + sKeyword + ' ', sKeyword.upper() + ' ', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + ';', ' ' + sKeyword.upper() + ';', oLine.line, 1, flags=re.IGNORECASE)
    oLine.line = re.sub(' ' + sKeyword + '\(', ' ' + sKeyword.upper() + '(', oLine.line, 1, flags=re.IGNORECASE)
    oLine.lineLower = oLine.line.lower()
