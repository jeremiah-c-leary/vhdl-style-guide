
def get_package_name(oLine):
    '''
    Returns the package name in the line.
    Parameters
      oLine: (line object)
    Returns: (string)
      Package name or empty string if package name not found.
    '''
    lLine = oLine.lineNoComment.split()
    for iIndex, sWord in enumerate(lLine):
        if sWord.lower() == 'package' and not lLine[iIndex + 1] == '--':
            return lLine[iIndex + 1].rstrip(';')
    return ''
