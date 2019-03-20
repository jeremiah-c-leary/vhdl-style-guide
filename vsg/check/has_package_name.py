
def has_package_name(oLine):
    '''
    Returns boolean if package name is found in line.

    Parameters:

      oLine: (line object)

    Returns: (boolean)

      True if package name exists in line.
      False if package name does not exist in line.
    '''
    lLine = oLine.lineNoComment.lower().split()
    for iIndex, sWord in enumerate(lLine):
        if sWord == 'package':
            if not lLine[iIndex + 1] == '--':
                return True
    return False
