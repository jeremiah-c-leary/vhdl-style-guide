
from vsg import rule
from vsg import check
from vsg import fix

import re


class rule_009(rule.rule):
    '''
    If rule 009 checks the alignment of multiline boolean expressions.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '009'
        self.solution = 'Align with space after ( in first line of boolean expression.'
        self.phase = 5

    def analyze(self, oFile):
        fCheckAlignment = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isIfKeyword and oLine.isThenKeyword:
                continue
            if oLine.isElseIfKeyword and oLine.isThenKeyword:
                continue
            if oLine.isIfKeyword:
                if re.match('^\s+if\s\(', oLine.lineLower):
                    iAlignmentColumn = oLine.lineLower.find('(')
                    fCheckAlignment = True
                continue  # pragma: no cover
            if oLine.isElseIfKeyword:
                if re.match('^\s+elsif\s\(', oLine.lineLower):
                    iAlignmentColumn = oLine.lineLower.find('(')
                    fCheckAlignment = True
                continue  # pragma: no cover
            if oLine.insideIf and fCheckAlignment:
                check.multiline_alignment(self, iAlignmentColumn + 1, oLine, iLineNumber)
            if oLine.isThenKeyword:
                fCheckAlignment = False

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            fix.multiline_alignment(self, oFile, iLineNumber)
