
from vsg.rules import keyword_alignment_rule


class rule_018(keyword_alignment_rule):
    '''
    Entity rule 018 ensures the alignment of comments in the entity.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'entity', '018')
        self.solution = 'Inconsistent alignment of comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isEntityDeclaration'
        self.sEndGroupTrigger = 'isEndEntityDeclaration'
        self.lLineTriggers = ['hasInlineComment']
        self.phase = 6

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.rule_specific_configuration = [{'name': 'separate_generic_port_alignment', 'triggers': ['isEndGenericMap']}]
