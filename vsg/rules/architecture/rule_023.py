
from vsg.rules import keyword_alignment_rule


class rule_023(keyword_alignment_rule):
    '''
    Architecture rule 023 ensures the alignment of comments.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'architecture', '023')
        self.solution = 'Inconsistent alignment of comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isArchitectureBegin'
        self.sLineTrigger = 'hasInlineComment'
        self.phase = 7
