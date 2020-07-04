
from vsg import severity


def print_output(dRunInfo):
    '''
    Displays results to stdout in syntastic format.

    Parameters:
      dRunInfo (dictionary)
    '''
    for dViolation in dRunInfo['violations']:
        sOutputString = _set_violation_type(dViolation)
        sOutputString += dRunInfo['filename']
        sOutputString += '('
        sOutputString += str(dViolation['lineNumber'])
        sOutputString += ')'
        sOutputString += dViolation['rule']
        sOutputString += ' -- '
        sOutputString += dViolation['solution']
        print(sOutputString)


def _set_violation_type(dViolation):
    if dViolation['severity']['type'] == severity.error_type:
        return 'ERROR: '
    else:
        return 'WARNING: '
