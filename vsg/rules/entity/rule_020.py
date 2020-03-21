
from vsg.rules import keyword_alignment_rule


class rule_020(keyword_alignment_rule):
    '''
    Entity rule 020 ensures the alignment of inline comments in the entity.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'entity', '020')
        self.solution = 'Inconsistent alignment of inline comments.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isEntityDeclaration'
        self.sEndGroupTrigger = 'isEndEntityDeclaration'
        self.lLineTriggers = ['hasInlineComment']
        self.phase = 6

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.configuration_triggers += [{'name': 'separate_generic_port_alignment', 'triggers': ['isEndGenericMap']}]
