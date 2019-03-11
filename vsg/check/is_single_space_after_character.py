'''
This module contains functions for rules to perform their checks.
'''

import re


def is_single_space_after_character(self, sCharacter, oLine, iLineNumber):
    '''
    Checks if a single space exists after a series of characters.
    NOTE:  The characters will match partial words.

    Parameters:

      self: (rule object)

      sCharacter: (string)

      oLine: (line object)

      iLineNumber: (integer)
    '''
    if not sCharacter.lower() in oLine.lineLower:
        return
    if not re.match('^.*' + sCharacter.lower() + '\s*--', oLine.lineNoComment):
        if re.match('^.*' + sCharacter.lower() + '$', oLine.lineNoComment):
            return
        if not re.match('^.*' + sCharacter.lower() + '\s\S', oLine.lineLower):
            self.add_violation(iLineNumber)
