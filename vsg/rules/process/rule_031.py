
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_031(rule.rule):
    '''Process rule 031 checks for alignment of identifiers and colons in the process declarative region.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '031'
        self.phase = 5
        self.solution = 'Align the first character of each identifier and align colons.'

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if fGroupFound:
                if oLine.isConstant or oLine.isVariable or oLine.isFileKeyword:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.blank_line())
            if oLine.isProcessBegin and fGroupFound:
                fGroupFound = False
                check.identifier_alignment(self, iStartGroupIndex, lGroup)
                check.keyword_alignment(self, iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None

    def _fix_violations(self, oFile):
        fix.identifier_alignment(self, oFile)
