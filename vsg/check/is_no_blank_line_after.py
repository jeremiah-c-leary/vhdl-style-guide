
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
    if sUnless:
        if oFile.lines[iLineNumber + 1].isBlank:
            if not oFile.lines[iLineNumber + 2].__dict__[sUnless]:
                self.add_violation(iLineNumber)

    elif oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)
