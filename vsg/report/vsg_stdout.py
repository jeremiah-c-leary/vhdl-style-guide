
iLineLength = 80


def print_output(dRunInfo):
    '''
    Displays results to stdout in standard VSG format.

    Parameters:
      dRunInfo (dictionary)
    '''
    header = print_header(dRunInfo['filename'])
    stats = print_stats(dRunInfo)
    violations = print_violations(dRunInfo)
    return header + stats + violations, None


def print_header(sFilename):
    '''
    Prints the header for displaying results.

    Parameters:
      sFilename (string)

    Returns: Nothing
    '''
    top = '=' * iLineLength + '\n'
    filename = 'File:  ' + sFilename + '\n'
    bottom = '=' * iLineLength + '\n'
    return top + filename + bottom


def print_phase_information(iPhaseNumber):
    '''
    Prints information about the analysis.
    '''
    return 'Phase ' + str(iPhaseNumber) + ' of 7... Reporting\n'


def print_divider():
    '''
    Prints a divider that matches the column divisions in the violations.
    '''
    return '-'*28 + '+' + '-'*12 + '+' + '-'*12 + '+' + '-'*38 + '\n'


def print_violation_header():
    top_divider = print_divider()
    sOutputString = '  '
    sOutputString += 'Rule'.ljust(25)
    sOutputString += ' | '
    sOutputString += 'severity'.center(10)
    sOutputString += ' | '
    sOutputString += 'line(s)'.center(10)
    sOutputString += ' | '
    sOutputString += 'Solution\n'
    bottom_divider = print_divider()
    return top_divider + sOutputString + bottom_divider


def print_stats(dRunInfo):
    '''
    Displays information about the run such as number failures.

    Parameters:

      dRunInfo : (dictionary)

    Returns: Nothing
    '''
    stats = 'Phase ' + str(dRunInfo['stopPhase']) + ' of 7... Reporting\n'
    stats += 'Total Rules Checked: ' + str(dRunInfo['num_rules_checked']) + '\n'
    stats += 'Total Violations:    ' + str(dRunInfo['total_violations']) + '\n'
    for sSeverity in list(dRunInfo['severities'].keys()):
        sFormat = '  {0:<' + str(dRunInfo['maxSeverityNameLength']) + 's} : {1:5d}'
        stats += sFormat.format(sSeverity, dRunInfo['severities'][sSeverity]) + '\n'
    return stats


def print_violations(dRunInfo):
    '''
    Displays information about each violations.

    Parameters:

      dRunInfo : (dictionary)

    Returns: Nothing
    '''
    if dRunInfo['total_violations'] > 0:
        sOutputString = print_violation_header()
        for dViolation in dRunInfo['violations']:
            sOutputString += '  '
            sOutputString += dViolation['rule'].ljust(25)
            sOutputString += ' | '
            sOutputString += dViolation['severity']['name'].ljust(10)
            sOutputString += ' | '
            sOutputString += dViolation['lineNumber'].rjust(10)
            sOutputString += ' | '
            try:
                sOutputString += dViolation['solution']
            except TypeError:
                sOutputString += 'None'
            sOutputString += '\n'
        sOutputString += print_divider()
        sOutputString += 'NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.'
        return sOutputString
    else:
        return ''
