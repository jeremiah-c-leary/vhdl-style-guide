
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

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword and not fGroupFound and oLine.insideEntity:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndPortMap and oLine.insideEntity:
                lGroup.append(oLine)
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isPortDeclaration:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)
