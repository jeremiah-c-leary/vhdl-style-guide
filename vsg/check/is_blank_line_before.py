from vsg import utils


def is_blank_line_before(self, oFile, iLineNumber, sUnless):
    '''
    Adds a violation if the line before iLineNumber is not blank.
    This is typically used to compress lines together.

    If sUnless is given, then a violation will not occur if there is a blank line before the line with the attribute given for sUnless.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)

      sUnless: (string) (line attribute)
    '''
    if sUnless:
        if iLineNumber > 0 and not oFile.lines[iLineNumber - 1].isBlank:
            if iLineNumber > 1 and not oFile.lines[iLineNumber - 1].__dict__[sUnless]:
                self.add_violation(utils.create_violation_dict(iLineNumber))
    elif iLineNumber > 0 and not oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(utils.create_violation_dict(iLineNumber))
