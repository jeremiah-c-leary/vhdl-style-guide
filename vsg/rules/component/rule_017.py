
from vsg.rules.component import component_rule
from vsg import line


class rule_017(component_rule):
    '''
    Component rule 017 ensures the alignment of the : operator for every
    port in the component.
    '''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Inconsistent alignment of ":" in port declaration of component.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.insideEntity:
                if oLine.isPortKeyword and not fGroupFound:
                    fGroupFound = True
                    iStartGroupIndex = iLineNumber
                if oLine.isEndPortMap:
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
