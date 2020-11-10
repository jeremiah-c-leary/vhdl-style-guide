'''
This module provides functions for rules to use.
'''


def create_violation_dict(iLineNumber):
    '''
    Builds a minimal violation dictionary.

    Parameters:

      iLineNumber: (integer)

    Returns:  dictionary
    '''
    dReturn = {}
    dReturn['lines'] = []
    dLine = {}
    dLine['number'] = iLineNumber
    dReturn['lines'].append(dLine)
    return dReturn


def get_violation_line_number(dViolation):
    '''
    Returns a line number of a violation.

    Parameters:

      dViolation: Violation dictionary

    Returns:  integer
    '''
    return dViolation['lines'][0]['number']


def get_violating_line(oFile, dViolation):
    '''
    Returns a line from the file where a violation has occured.

    Parameters:

      oFile : (File object)

      dViolation : (Violation dictionary)

    Return: Line Object
    '''
    return oFile.lines[get_violation_line_number(dViolation)]


def get_violation_at_line_number(lViolations, iLineNumber):
    '''
    Returns a violation from a violation dictionary at the given line number.

    Parameters:

      lViolation : (List of Violation dictionaries)

      iViolation : (integer)

    Return: Violation Dictionary
    '''
    for dViolation in lViolations:
        for dLine in dViolation['lines']:
            if dLine['number'] == iLineNumber:
                return dViolation


def get_violation_solution_at_line_number(lViolations, iLineNumber):
    '''
    Returns a the solution for a violation at a given line number.

    Parameters:

      lViolation : (List of Violation dictionaries)

      iViolation : (integer)

    Return: string
    '''
    dViolation = get_violation_at_line_number(lViolations, iLineNumber)
    return dViolation['solution']
