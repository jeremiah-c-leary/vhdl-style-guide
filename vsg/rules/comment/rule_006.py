
from vsg.rules import keyword_alignment_rule


class rule_006(keyword_alignment_rule):
    '''
    Comment rule 006 ensures the alignment of "--" keywords between the process sensitivity list and the process "begin" keywords.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'comment', '006')
        self.solution = 'Inconsistent alignment of comments process declaration region.'
        self.phase = 6
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isSensitivityListEnd'
        self.sEndGroupTrigger = 'isProcessBegin'
        self.sLineTrigger = 'hasInlineComment'
