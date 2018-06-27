
from vsg.rules import keyword_alignment_rule


class rule_009(keyword_alignment_rule):
    '''
    Signal rule 009 checks the colons are in the same column for all signals.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'signal', '009')
        self.solution = 'Align colon with right most colon.'
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isArchitectureBegin'
        self.sLineTrigger = 'isSignal'
