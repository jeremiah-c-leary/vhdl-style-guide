
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
