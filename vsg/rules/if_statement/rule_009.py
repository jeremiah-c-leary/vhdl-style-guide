
from vsg.rules.if_statement import if_rule

import re


class rule_009(if_rule):
    '''If rule 009 checks the alignment of multiline boolean expressions.'''

    def __init__(self):
        if_rule.__init__(self)
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
                continue #  pragma: no cover
            if oLine.isElseIfKeyword:
                if re.match('^\s+elsif\s\(', oLine.lineLower):
                    iAlignmentColumn = oLine.lineLower.find('(')
                    fCheckAlignment = True
                continue #  pragma: no cover
            if oLine.insideIf and fCheckAlignment:
                self._check_multiline_alignment(iAlignmentColumn + 1, oLine, iLineNumber)
            if oLine.isThenKeyword:
                fCheckAlignment = False

    def _fix_violations(self, oFile):
        for iLineNumber in self.dFix['violations']:
            self._fix_multiline_alignment(oFile, iLineNumber)
