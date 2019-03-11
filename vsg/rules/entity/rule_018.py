
from vsg.rules import keyword_alignment_rule


class rule_018(keyword_alignment_rule):
    '''
    Entity rule 018 ensures the alignment of comments in the entity.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'entity', '018')
        self.solution = 'Inconsistent alignment of comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'insideEntity'
        self.sEndGroupTrigger = 'isEndEntityDeclaration'
        self.sLineTrigger = 'hasInlineComment'
        self.phase = 6
