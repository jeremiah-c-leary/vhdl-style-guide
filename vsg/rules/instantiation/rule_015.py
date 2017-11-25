
from vsg.rules.instantiation import instantiation_rule
from vsg import line


class rule_015(instantiation_rule):
    '''
    Instantiation rule 015 ensures the alignment of the => operator for every generic in the instantiation.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '015'
        self.solution = 'Inconsistent alignment of "=>" in generic assignments of instantiation.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericKeyword and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if oLine.isInstantiationGenericEnd:
                lGroup.append(oLine)
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, '=>', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isInstantiationGenericAssignment:
                    lGroup.append(oLine)
                else:
                    lGroup.append(line.line('Removed line'))

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
