
from vsg.rules import keyword_alignment_rule


class rule_011(keyword_alignment_rule):
    '''
    Signal rule 011 checks the colons are in the same column for all variables.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'variable', '011')
        self.solution = 'Align colon with right most colon.'
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isProcessKeyword'
        self.sEndGroupTrigger = 'isProcessBegin'
        self.sLineTrigger = 'isVariable'
