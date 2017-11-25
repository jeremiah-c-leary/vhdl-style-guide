
from vsg.rules.entity import entity_rule
from vsg import line


class rule_018(entity_rule):
    '''
    Entity rule 018 ensures the alignment of comments in the entity.
    '''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '018'
        self.solution = 'Inconsistent alignment of comments in entity.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not fGroupFound and oLine.insideEntity:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isEndEntityDeclaration:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '--', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.hasComment and not oLine.isComment:
                  lGroup.append(oLine)
                else:
                  lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
