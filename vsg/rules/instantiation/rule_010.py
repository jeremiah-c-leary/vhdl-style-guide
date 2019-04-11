
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_010(rule.rule):
    '''
    Instantiation rule 010 ensures the alignment of the => operator for every port in the instantiation.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '010'
        self.solution = 'Inconsistent alignment of "=>" in port assignments of instantiation.'
        self.phase = 5

    def _pre_analyze(self):
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationPortKeyword and not self.fGroupFound:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if oLine.isInstantiationPortEnd and self.fGroupFound:
            self.lGroup.append(oLine)
            self.fGroupFound = False
            check.keyword_alignment(self, self.iStartGroupIndex, '=>', self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if oLine.isInstantiationPortAssignment and not oLine.isInstantiationPortKeyword:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
