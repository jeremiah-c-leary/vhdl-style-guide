
def is_lowercase(self, sString, iLineNumber):
    '''
    Checks if a string is lowercase.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)
    '''
    if not sString == sString.lower():
        self.add_violation(iLineNumber)
        return False

    return True
