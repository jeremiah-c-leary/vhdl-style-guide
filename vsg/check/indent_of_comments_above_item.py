from vsg import utils
from vsg import parser


def indent_of_comments_above_item(self, oFile, iLine, iIndentLevel):
    '''
    Checks the indent level of consecutive comment lines above the line number given.

    Parameters:

      self: (rule object)

      oFile: (vhdlFile object)

      iLine: (integer)
    '''
    for iIndex in range(iLine - 1, 0, -1):
        oLine = oFile.lines[iIndex] 
 
        if oLine.begins_with_token(parser.comment, True):
            if oLine.get_indent_value() != len(iIndentLevel * self.indentSize * ' '):
                dViolation = utils.create_violation_dict(iIndex)
                dViolation['indent'] = iIndentLevel
                self.add_violation(dViolation)
            else:
                oLine.indentLevel = iIndentLevel
        else:
            break
