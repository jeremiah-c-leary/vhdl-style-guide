
from vsg.rules.generic import generic_rule
from vsg import line

class rule_015(generic_rule):
    '''Generic rule 015 ensures the alignment of the := operator for every generic in the entity.'''

    def __init__(self):
        generic_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Inconsistent alignment of ":=" in generic declaration of entity.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword and not fGroupFound and not oLine.isGenericDeclaration:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndGenericMap and fGroupFound:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isGenericDeclaration:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
