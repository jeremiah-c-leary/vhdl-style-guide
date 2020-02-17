
from vsg.rules import keyword_alignment_rule


class rule_026(keyword_alignment_rule):
    '''
    Architecture rule 026 checks the colons are in the same column for all declarations
    in the architecture declarative part.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'architecture', '026')
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isArchitectureBegin'
        self.lLineTriggers = ['isConstant', 'isSignal', 'insideFile']
        self.solution = 'Align colon with right most colon.'
