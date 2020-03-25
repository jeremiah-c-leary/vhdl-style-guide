
def print_output(dRunInfo):
    '''
    Displays results to stdout in syntastic format.

    Parameters:
      dRunInfo (dictionary)
    '''
    for dViolation in dRunInfo['violations']:
        sOutputString = 'ERROR: '
        sOutputString += dRunInfo['filename']
        sOutputString += '('
        sOutputString += str(dViolation['lineNumber'])
        sOutputString += ')'
        sOutputString += dViolation['rule']
        sOutputString += ' -- '
        sOutputString += dViolation['solution']
        print(sOutputString)
