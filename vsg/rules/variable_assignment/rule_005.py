
from vsg.rules.variable_assignment import variable_assignment_rule
from vsg import line


class rule_005(variable_assignment_rule):
    '''Variable assignment rule 005 ensures the alignment of the ":=" keyword over multiple lines.'''

    def __init__(self):
        variable_assignment_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Inconsistent alignment of ":=" in group of lines.'
        self.phase = 5

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isVariableAssignment and not fGroupFound:
                fGroupFound = True
                iStartGroupIndex = iLineNumber
            if not oLine.insideVariableAssignment and fGroupFound:
                fGroupFound = False
                self._check_keyword_alignment(iStartGroupIndex, ':=', lGroup)
                lGroup = []
                iStartGroupIndex = None
            if fGroupFound:
                if oLine.isComment:
                    lGroup.append(line.line('Removed line'))
                else:
                    lGroup.append(oLine)

    def _fix_violations(self, oFile):
        self._fix_keyword_alignment(oFile)
