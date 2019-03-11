'''
This module contains functions for rules to perform their checks.
'''

import re


def is_uppercase(self, sString, iLineNumber):
    '''
    Checks if a string is uppercase.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)
    '''
    if not sString == sString.upper():
        self.add_violation(iLineNumber)
