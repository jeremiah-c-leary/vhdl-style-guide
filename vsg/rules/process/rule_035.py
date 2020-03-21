
from vsg.rules import keyword_alignment_rule


class rule_035(keyword_alignment_rule):
    '''
    Process rule 035 ensures the alignment of "--" keywords between process "begin" and "end process" keywords.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'process', '035')
        self.solution = 'Inconsistent alignment of comments within process.'
        self.phase = 6
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isProcessBegin'
        self.sEndGroupTrigger = 'isEndProcess'
        self.lLineTriggers = ['hasInlineComment']
