
from vsg.rules import keyword_alignment_rule


class rule_033(keyword_alignment_rule):
    '''
    Process rule 033 checks the colons are in the same column for all declarations
    in the process declarative part.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'process', '033')
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isProcessKeyword'
        self.sEndGroupTrigger = 'isProcessBegin'
        self.lLineTriggers = ['isConstant', 'isVariable', 'insideFile']
        self.solution = 'Align colon with right most colon.'
