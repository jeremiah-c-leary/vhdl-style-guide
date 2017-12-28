
from vsg.rules.concurrent import keyword_alignment_rule


class rule_008(keyword_alignment_rule):
    '''
    Concurrent rule 008 ensures the alignment of comments in sequential conccurent statements.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'concurrent', '008')
        self.solution = 'Inconsistent alignment of comments in group of lines.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isConcurrentBegin'
        self.sEndGroupTrigger = 'insideConcurrent'
