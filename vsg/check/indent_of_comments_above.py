from vsg import utils


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
                dViolation = utils.create_violation_dict(iPreviousIndex)
                dViolation['indent'] = oFile.lines[iLineNumber].indentLevel
                self.add_violation(dViolation)
            else:
                oFile.lines[iPreviousIndex].indentLevel = oFile.lines[iLineNumber].indentLevel
