
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_017(rule.rule):
    '''
    Entity rule 017 ensures the alignment of the : operator for every port in the entity.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'
        self.identifier = '017'
        self.solution = 'Inconsistent alignment of ":" in port declaration of entity.'
        self.phase = 5

    def _pre_analyze(self):
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortKeyword and not self.fGroupFound and oLine.insideEntity:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if oLine.isEndPortMap and oLine.insideEntity:
            self.lGroup.append(oLine)
            self.fGroupFound = False
            check.keyword_alignment(self, self.iStartGroupIndex, ':', self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if oLine.isPortDeclaration:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
