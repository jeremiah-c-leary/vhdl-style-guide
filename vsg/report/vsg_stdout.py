
iLineLength = 80


def print_output(dRunInfo):
    '''
    Displays results to stdout in standard VSG format.

    Parameters:
      dRunInfo (dictionary)
    '''
    print_header(dRunInfo['filename'])
    print_stats(dRunInfo)
    print_violations(dRunInfo)


def print_header(sFilename):
    '''
    Prints the header for displaying results.

    Parameters:
      sFilename (string)

    Returns: Nothing
    '''
    print('=' * iLineLength)
    print('File:  ' + sFilename)
    print('=' * iLineLength)


def print_phase_information(iPhaseNumber):
    '''
    Prints information about the analysis.
    '''
    print('Phase ' + str(iPhaseNumber) + ' of 7... Reporting')


def print_divider():
    '''
    Prints a divider that matches the column divisions in the violations.
    '''
    print('-'*28 + '+' + '-'*12 + '+' + '-'*12 + '+' + '-'*38)


def print_violation_header():
    print_divider()
    sOutputString = '  '
    sOutputString += 'Rule'.ljust(25)
    sOutputString += ' | '
    sOutputString += 'severity'.center(10)
    sOutputString += ' | '
    sOutputString += 'line(s)'.center(10)
    sOutputString += ' | '
    sOutputString += 'Solution'
    print(sOutputString)
    print_divider()


def print_stats(dRunInfo):
    '''
    Displays information about the run such as number failures.

    Parameters:

      dRunInfo : (dictionary)

    Returns: Nothing
    '''
    print('Phase ' + str(dRunInfo['stopPhase']) + ' of 7... Reporting')
    print('Total Rules Checked: ' + str(dRunInfo['num_rules_checked']))
    print('Total Violations:    ' + str(dRunInfo['total_violations']))
    for sSeverity in list(dRunInfo['severities'].keys()):
        sFormat = '  {0:<' + str(dRunInfo['maxSeverityNameLength']) + 's} : {1:5d}'
        print(sFormat.format(sSeverity, dRunInfo['severities'][sSeverity]))


def print_violations(dRunInfo):
    '''
    Displays information about each violations.

    Parameters:

      dRunInfo : (dictionary)

    Returns: Nothing
    '''
    if dRunInfo['total_violations'] > 0:
        print_violation_header()
        for dViolation in dRunInfo['violations']:
            sOutputString = '  '
            sOutputString += dViolation['rule'].ljust(25)
            sOutputString += ' | '
            sOutputString += dViolation['severity']['name'].ljust(10)
            sOutputString += ' | '
            sOutputString += dViolation['lineNumber'].rjust(10)
            sOutputString += ' | '
            sOutputString += dViolation['solution']
            print(sOutputString)
        print_divider()
        print('NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.')
