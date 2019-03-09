
from vsg import rule

import re


class rule_023(rule.rule):
    '''
    Instantiation rule 023 checks for comments after port and generic assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '023'
        self.solution = 'Remove comment.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideInstantiation and oLine.hasComment:
            if oLine.isInstantiationPortAssignment or oLine.isInstantiationGenericAssignment:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('\s*--.*', '', oLine.line))
            oLine.hasComment = False
            oLine.hasInlineComment = False
