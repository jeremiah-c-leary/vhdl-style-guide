
def starts_with(self, sString, iLineNumber, sPattern):
    '''
    Checks if a string starts with pattern.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)

      sPattern: (string)
    '''
    if not sString.startswith(sPattern):
        self.add_violation(iLineNumber)
