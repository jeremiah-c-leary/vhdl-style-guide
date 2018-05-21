
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

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if ' ' + self.sCharacter in oLine.lineNoComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'(\s+' + self.sCharacter + ')', self.sCharacter, oLine.line))
