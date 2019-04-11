
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

    def _pre_analyze(self):
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword and not self.fGroupFound:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if self.fGroupFound:
            if oLine.isConstant or oLine.isVariable or oLine.isFileKeyword:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.blank_line())
        if oLine.isProcessBegin and self.fGroupFound:
            self.fGroupFound = False
            check.identifier_alignment(self, self.iStartGroupIndex, self.lGroup)
            check.keyword_alignment(self, self.iStartGroupIndex, ':', self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None

    def _fix_violations(self, oFile):
        fix.identifier_alignment(self, oFile)
