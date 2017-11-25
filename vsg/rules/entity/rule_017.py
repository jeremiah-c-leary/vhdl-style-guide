
from vsg.rules.entity import entity_rule
from vsg import line


class rule_017(entity_rule):
    '''
    Entity rule 017 ensures the alignment of the : operator for every port in the entity.
    '''

    def __init__(self):
        entity_rule.__init__(self)
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
                self._check_keyword_alignment(iStartGroupIndex, ':', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isPortDeclaration:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
