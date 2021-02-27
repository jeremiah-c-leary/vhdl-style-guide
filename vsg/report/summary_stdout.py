def print_output(dRunInfo):
    '''
    Displays results to stdout in a compact format.

    Parameters:
      dRunInfo (dictionary)
    '''
    sOutputString = 'File: '
    sOutputString += dRunInfo['filename']

    sOutputString += ' '

    if dRunInfo['severities']['Error'] == 0:
        sOutputString += 'OK'
    else:
        sOutputString += 'ERROR'

    sOutputString += ' '

    sOutputString += '('
    sOutputString += str(dRunInfo['num_rules_checked'])
    sOutputString += ' rules checked)'

    for sSeverity in list(dRunInfo['severities'].keys()):
        sOutputString += ' ['
        sOutputString += sSeverity
        sOutputString += ': '
        sOutputString += str(dRunInfo['severities'][sSeverity])
        sOutputString += ']'
    if dRunInfo['severities']['Error'] == 0:
        return sOutputString, None
    else:
        return None, sOutputString
