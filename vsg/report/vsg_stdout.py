
iLineLength = 80


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
    print('-'*28 + '+' + '-'*12 + '+' + '-'*38)

def print_violation_header():
    print_divider()
    sOutputString = '  '
    sOutputString += 'Violation'.ljust(25)
    sOutputString += ' | '
    sOutputString += 'line(s)'.center(10)
    sOutputString += ' | '
    sOutputString += 'Solution'
    print(sOutputString)
    print_divider()


def print_output(dRunInfo):
    '''
    Displays results to stdout in standard VSG format.

    Parameters:
      dRunInfo (dictionary)
    '''
    print_header(dRunInfo['filename'])
    print('Phase ' + str(dRunInfo['stopPhase']) + ' of 7... Reporting')
    print('Total Rules Checked: ' + str(dRunInfo['num_rules_checked']))
    print('Total Violations:    ' + str(dRunInfo['total_violations']))
    if dRunInfo['total_violations'] > 0:
        print_violation_header()
        for dViolation in dRunInfo['violations']:
            sOutputString = '  '
            sOutputString += dViolation['rule'].ljust(25)
            sOutputString += ' | '
            sOutputString += dViolation['lineNumber'].rjust(10)
            sOutputString += ' | '
            sOutputString += dViolation['solution']
            print(sOutputString)
        print_divider()
