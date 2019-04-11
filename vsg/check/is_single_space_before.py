'''
This module contains functions for rules to perform their checks.
'''

import re


def is_single_space_before(self, sString, oLine, iLineNumber):
    '''
    Checks if a single space exists before the string given.
    The string is considered a whole word.
    Parameters:
      self: (rule object)
      sString: (string)
      oLine: (line object)
      iLineNumber: (integer)
    '''
    if not sString.lower() in oLine.lineLower:
        return
    if not re.match('^.*\S\s' + sString + '\s', oLine.lineNoComment.lower()) and \
       not re.match('^.*\S\s' + sString + '$', oLine.lineNoComment.lower()) and \
       not re.match('^.*\S\s' + sString + '\'', oLine.lineNoComment.lower()):
        self.add_violation(iLineNumber)
