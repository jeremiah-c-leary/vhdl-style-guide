
from vsg.rules import keyword_alignment_rule


class rule_015(keyword_alignment_rule):
    '''
    Instantiation rule 015 ensures the alignment of the => operator for every generic in the instantiation.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '015'
        self.solution = 'Inconsistent alignment of "=>" in generic assignments of instantiation.'
        self.sKeyword = '=>'
        self.sStartGroupTrigger = 'isInstantiationGenericKeyword'
        self.sEndGroupTrigger = 'isInstantiationGenericEnd'
        self.sLineTrigger = 'isInstantiationGenericAssignment'
