
from vsg.rules import keyword_alignment_rule


class rule_020(keyword_alignment_rule):
    '''
    Component rule 020 ensures the alignment of comments in a component declaration.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'component', '020')
        self.solution = 'Inconsistent alignment of comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'insideComponent'
        self.sEndGroupTrigger = 'isComponentEnd'
        self.sLineTrigger = 'hasInlineComment'
        self.phase = 6
