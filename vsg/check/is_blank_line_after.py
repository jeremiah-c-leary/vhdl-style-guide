
def is_blank_line_after(self, oFile, iLineNumber):
    '''
    Adds a violation if the line after iLineNumber is not blank.
    This is typically used to compress lines together.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    if not oFile.lines[iLineNumber + 1].isBlank:
        self.add_violation(iLineNumber)
