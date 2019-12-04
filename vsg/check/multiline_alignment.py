'''
This module contains functions for rules to perform their checks.
'''

import re


def multiline_alignment(self, iColumn, oLine, iLineNumber):
    '''
    Checks the alignment of multiline statements.

    Parameters:

      self: (rule object)

      iColumn: (integer)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not re.match('\s{' + str(iColumn) + '}\S', oLine.line):
        self.add_violation(iLineNumber)
        self.dFix['violations'][iLineNumber] = {}
        self.dFix['violations'][iLineNumber]['column'] = iColumn
