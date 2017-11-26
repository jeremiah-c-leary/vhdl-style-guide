
from vsg.rules.entity import entity_rule
from vsg import check

import re


class rule_001(entity_rule):
    '''
    Entity rule 001 checks for spaces before the entity keyword.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
