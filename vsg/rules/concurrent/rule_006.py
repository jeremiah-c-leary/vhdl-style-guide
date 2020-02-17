
from vsg.rules import keyword_alignment_rule


class rule_006(keyword_alignment_rule):
    '''
    Concurrent rule 006 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'concurrent', '006')
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.sKeyword = '<='
        self.sStartGroupTrigger = 'isArchitectureBegin'
        self.sEndGroupTrigger = 'isEndArchitecture'
        self.lLineTriggers = ['insideConcurrent']
