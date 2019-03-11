'''
This module contains functions for rules to perform their checks.
'''

import re


def is_lowercase(self, sString, iLineNumber):
    '''
    Checks if a string is lowercase.

    Parameters:

      self: (rule object)

      sString: (string)

      iLineNumber: (integer)
    '''
    if not sString == sString.lower():
        self.add_violation(iLineNumber)
