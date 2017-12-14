
from vsg import rule
from vsg import fix

import re


class rule_005(rule.rule):
    '''
    Comment rule 005 checks consecutive comment lines above a "when" keyword
    in a case statement are aligned with the "when" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '005'
        self.solution = 'Align comment with "when" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword:
                iIndex = 0
                while iLineNumber - iIndex > 1:
                    iIndex += 1
                    iPreviousIndex = iLineNumber - iIndex
                    if not oFile.lines[iPreviousIndex].isComment:
                        break
                    else:
                        if not oFile.lines[iPreviousIndex].indentLevel == oFile.lines[iLineNumber].indentLevel:
                            self.add_violation(iPreviousIndex)
                            self.dFix['violations'][iPreviousIndex] = oFile.lines[iLineNumber].indentLevel

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oFile.lines[iLineNumber].indentLevel = self.dFix['violations'][iLineNumber]
