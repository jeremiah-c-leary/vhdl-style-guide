
def print_output(dRunInfo):
    '''
    Displays results to stdout in syntastic format.

    Parameters:
      dRunInfo (dictionary)
    '''
    for dViolation in dRunInfo['violations']:
        if dViolation['severity']['type'] == 'error':
            sOutputString = 'ERROR: '
        else:
            sOutputString = 'WARNING: '
        sOutputString += dRunInfo['filename']
        sOutputString += '('
        sOutputString += str(dViolation['lineNumber'])
        sOutputString += ')'
        sOutputString += dViolation['rule']
        sOutputString += ' -- '
        sOutputString += dViolation['solution']
        print(sOutputString)
