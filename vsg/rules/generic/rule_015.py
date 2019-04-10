
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_015(rule.rule):
    '''
    Generic rule 015 ensures the alignment of the := operator for every
    generic in the entity.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '015'
        self.solution = 'Inconsistent alignment of ":=" in generic \
                         declaration of entity.'
        self.phase = 5

    def _pre_analyze(self):
        self.lGroup = []
        self.fGroupFound = False
        self.iStartGroupIndex = None

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenericKeyword and not oLine.isGenericDeclaration:
            self.fGroupFound = True
            self.iStartGroupIndex = iLineNumber
        if oLine.isEndGenericMap and self.fGroupFound:
            self.lGroup.append(oLine)
            self.fGroupFound = False
            check.keyword_alignment(self, self.iStartGroupIndex, ':=', self.lGroup)
            self.lGroup = []
            self.iStartGroupIndex = None
        if self.fGroupFound:
            if oLine.isGenericDeclaration:
                self.lGroup.append(oLine)
            else:
                self.lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
