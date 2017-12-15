
from vsg.rules import keyword_alignment_rule


class rule_003(keyword_alignment_rule):
    '''Comment rule 003 ensures the alignment of "--" keywords between process "begin" and "end process" keywords.'''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'comment', '003')
        self.solution = 'Inconsistent alignment of comments within process.'
        self.phase = 6
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isProcessBegin'
        self.sEndGroupTrigger = 'isEndProcess'
        self.sLineTrigger = 'hasInlineComment'
