
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

    def _search_for_group(self, fGroupFound, oLine, iStartGroupIndex, iLineNumber):
        if not fGroupFound and oLine.insideEntity:
            return True, iLineNumber
        return fGroupFound, iStartGroupIndex

    def _store_lines_for_group(self, fGroupFound, oLine, lGroup):
        if fGroupFound:
            if oLine.hasComment and not oLine.isComment:
                lGroup.append(oLine)
            else:
                lGroup.append(line.line('Removed line'))

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            fGroupFound, iStartGroupIndex = self._search_for_group(fGroupFound, oLine, iStartGroupIndex, iLineNumber)
            if oLine.isEndEntityDeclaration:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '--', lGroup)
                lGroup = []
                iStartGroupIndex = None
            self._store_lines_for_group(fGroupFound, oLine, lGroup)

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
