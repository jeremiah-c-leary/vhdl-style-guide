
from vsg import rule
from vsg import utils

import re


class rule_019(rule.rule):
    '''
    Entity rule 019 checks for the entity name on the "end entity" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '019'
        self.solution = 'Add the entity name.'
        self.phase = 1

    def _pre_analyze(self):
        self.sEntityName = ''

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEntityDeclaration:
           self.sEntityName = utils.extract_entity_identifier(oLine)[0]
        if oLine.isEndEntityDeclaration and re.match('^\s*end\s+entity', oLine.line, re.IGNORECASE):
            if not re.match('^\s*end\s+entity\s+\w+', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)
                self.dFix['violations'][iLineNumber] = self.sEntityName

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line
            iIndex = oLine.lineLower.find('entity') + len('entity')
            oLine.update_line(sLine[:iIndex] + ' ' + self.dFix['violations'][iLineNumber] + sLine[iIndex:])
