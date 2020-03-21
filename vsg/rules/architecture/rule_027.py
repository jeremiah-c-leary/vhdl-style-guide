
from vsg.rules import keyword_alignment_rule


class rule_027(keyword_alignment_rule):
    '''
    Architecture rule 027 checks the alignment of inline comments in the architecture declarative part.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'architecture', '027')
        self.solution = 'Inconsistent alignment of inline comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isArchitectureKeyword'
        self.sEndGroupTrigger = 'isArchitectureBegin'
        self.lLineTriggers = ['hasInlineComment']
