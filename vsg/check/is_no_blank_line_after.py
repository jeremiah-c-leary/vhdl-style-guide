from vsg import utils


def is_no_blank_line_after(self, oFile, iLineNumber, sUnless=None):
    '''
    Adds a violation if the line after iLineNumber is blank.
    This is typically used to compress lines together.

    If sUnless is given, then a violation will not occur if there is a blank line following the line with the attribute given for sUnless.

    Parameters

      self: (rule object)

      oLine: (line object)

      iLineNumber: (integer)

      sUnless: (string) (line attribute)
    '''
    headroom = len(oFile.lines) - iLineNumber - 1
    if sUnless:
        if headroom > 0 and oFile.lines[iLineNumber + 1].isBlank:
            if headroom > 1 and not oFile.lines[iLineNumber + 2].__dict__[sUnless]:
                self.add_violation(utils.create_violation_dict(iLineNumber))

    elif headroom > 0 and oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(utils.create_violation_dict(iLineNumber))
