
from vsg import severity


def print_output(dRunInfo):
    '''
    Displays results to stdout in syntastic format.

    Parameters:
      dRunInfo (dictionary)
    '''
    sOutputString = ''
    for dViolation in dRunInfo['violations']:
        sOutputString = _set_violation_type(dViolation)
        sOutputString += dRunInfo['filename']
        sOutputString += '('
        sOutputString += str(dViolation['lineNumber'])
        sOutputString += ')'
        sOutputString += dViolation['rule']
        sOutputString += ' -- '
        sOutputString += dViolation['solution']
        sOutputString += '\n'
    return sOutputString[:-1], None


def _set_violation_type(dViolation):
    if dViolation['severity']['type'] == severity.error_type:
        return 'ERROR: '
    elif dViolation['severity']['type'] == severity.warning_type:
        return 'WARNING: '
