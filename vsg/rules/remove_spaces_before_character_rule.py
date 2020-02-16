
from vsg import rule

import re


class remove_spaces_before_character_rule(rule.rule):
    '''
    This class removes spaces before a given character.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sCharacter : string
       The character to start removing spaces before.
    '''

    def __init__(self, name=None, identifier=None, sCharacter=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 2
        self.sCharacter = sCharacter
        self.solution = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if ' ' + self.sCharacter in oLine.lineNoComment:
            self.add_violation({'lineNumber': iLineNumber})

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = oFile.lines[dViolation['lineNumber']]
            oLine.update_line(re.sub(r'(\s+' + self.sCharacter + ')', self.sCharacter, oLine.line))
