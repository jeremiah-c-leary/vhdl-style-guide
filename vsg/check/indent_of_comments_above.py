
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
