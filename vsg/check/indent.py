'''
This module contains functions for rules to perform their checks.
'''

import re


def indent(self, oLine, iLineNumber):
    '''
    Adds a violation if the indent of the line does not match the desired level.

    Parameters

      self: (rule object)

      oLine: (line object)

      iLineNumber: (integer)

    '''
    if not oLine.isBlank:
        try:
            if not re.match('^\s{' + str(self.indentSize * oLine.indentLevel) + '}\S', oLine.line):
                self.add_violation(iLineNumber)
        except TypeError:
            pass
