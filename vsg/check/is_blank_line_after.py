from vsg import utils


def is_blank_line_after(self, oFile, iLineNumber):
    '''
    Adds a violation if the line after iLineNumber is not blank.
    This is typically used to compress lines together.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    headroom = len(oFile.lines) - iLineNumber - 1
    if headroom > 0 and not oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(utils.create_violation_dict(iLineNumber))
