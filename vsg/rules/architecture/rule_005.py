
from vsg import rule
from vsg import utils

import re


class rule_005(rule.rule):
    '''Architecture rule 005 checks if the "of" keyword is on the same line as the "architecture" keyword.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'architecture'
        self.identifier = '005'
        self.solution = 'Ensure "of" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1

    def _pre_analyze(self):
        self.ofMissing = False
        self.dViolation = {}

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword:
            self.ofMissing = False
        # Search for of statement
        if self.ofMissing and re.match('^\s*of', oLine.line, re.IGNORECASE):
            self.ofMissing = False
            self.dViolation['of_line'] = iLineNumber
            self.add_violation(self.dViolation)
        # Check architecture statement for "of"
        if oLine.isArchitectureKeyword and not re.match('^\s*architecture\s+\w+\s+of', oLine.line, re.IGNORECASE):
            self.dViolation = utils.create_violation_dict(iLineNumber)
            self.ofMissing = True

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            oLine.update_line(re.sub(r'^(\s*architecture\s+\w+\s*)', r'\1 of', oLine.line, re.IGNORECASE))
            utils.search_for_and_remove_keyword(oFile, utils.get_violation_linenumber(dViolation), 'of')
