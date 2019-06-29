
from vsg.rules import keyword_alignment_rule


class rule_002(keyword_alignment_rule):
    '''
    After rule 002 ensures the alignment of the after keyword in clock processes
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'after', '002')
        self.solution = 'Inconsistent alignment of after keywords.'
        self.sKeyword = 'after'
        self.sStartGroupTrigger = 'insideClockProcess'
        self.sEndGroupTrigger = 'isEndProcess'
        self.sLineTrigger = 'hasAfterKeyword'
        self.disable = True
