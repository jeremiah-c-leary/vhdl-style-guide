
from vsg import rule

import re


class rule_019(rule.rule):
    '''
    Component rule 019 checks for comments after port and generic assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '019'
        self.solution = 'Remove comment.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideComponent and oLine.hasInlineComment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('\s*--.*', '', oLine.line))
            oLine.hasInlineComment = False
