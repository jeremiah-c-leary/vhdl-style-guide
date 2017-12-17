
from vsg import rule
from vsg import utilities

import re


class rule_005(rule.rule):
    '''
    Entity rule 005 checks the "is" keyword is on the same line as the
    entity keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "entity" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration and not re.match('^.*\s\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*entity\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE))
            utilities.search_for_and_remove_keyword(oFile, iLineNumber, 'is')
