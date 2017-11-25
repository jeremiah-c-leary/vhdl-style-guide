
from vsg.rules.entity import entity_rule

import re


class rule_005(entity_rule):
    '''
    Entity rule 005 checks the "is" keyword is on the same line as the entity keyword.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "entity" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEntityDeclaration:
                if not re.match('^.*\s\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _clear_line(self, oLine):
        oLine.update_line(re.sub(r'^(\s*)is', r'\1  ', oLine.line))
        if re.match('^\s*$', oLine.line):
            oLine.update_line('')
            oLine.isBlank = True

    def _search_for_and_remove_is_keyword(self, oFile, iLineNumber):
        iSearchIndex = iLineNumber
        while True:
            iSearchIndex += 1
            oLine = oFile.lines[iSearchIndex]
            if re.match('^\s*is', oLine.line, re.IGNORECASE):
                self._clear_line(oLine)
            if not oLine.isBlank:
                break

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*entity\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE))
            self._search_for_and_remove_is_keyword(oFile, iLineNumber)
