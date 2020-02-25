
from vsg.rules import keyword_alignment_rule


class rule_015(keyword_alignment_rule):
    '''
    Generic rule 015 ensures the alignment of the := operator for every
    generic in the entity.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'generic', '015')
        self.solution = 'Inconsistent alignment of ":=" in generic declaration of entity.'
        self.sKeyword = ':='
        self.sStartGroupTrigger = 'isGenericKeyword'
        self.sEndGroupTrigger = 'isEndGenericMap'
        self.lLineTriggers = ['isGenericDeclaration']
