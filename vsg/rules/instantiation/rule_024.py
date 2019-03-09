
from vsg import rule


class rule_024(rule.rule):
    '''
    Instantiation rule 024 checks for positional generic and port assignments.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '024'
        self.solution = 'Rewrite positional assignment to explicit assignment.'
        self.phase = 1
        self.fixable = False  # This requires the user to map the ports and generics

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideInstantiation:
            if ',' in oLine.lineNoComment:
                lLine = oLine.lineNoComment.split(',')
                for sString in lLine[:-1]:
                    if '=>' not in sString:
                        self.add_violation(iLineNumber)
                        break
