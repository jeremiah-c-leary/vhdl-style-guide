
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
        if not oFile.lines[iLineNumber - 1].isBlank:
            if not oFile.lines[iLineNumber - 1].__dict__[sUnless]:
                self.add_violation(iLineNumber)
    elif not oFile.lines[iLineNumber - 1].isBlank:
        self.add_violation(iLineNumber)
