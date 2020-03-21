
from vsg.rules import keyword_alignment_rule


class rule_017(keyword_alignment_rule):
    '''
    Entity rule 017 ensures the alignment of the colon for each generic and port in the entity declaration.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'entity', '017')
        self.solution = 'Inconsistent alignment of ":" in generic or port declaration of entity.'
        self.sKeyword = ':'
        self.sStartGroupTrigger = 'isEntityDeclaration'
        self.sEndGroupTrigger = 'isEndEntityDeclaration'
        self.lLineTriggers = ['isGenericDeclaration', 'isPortDeclaration']

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.configuration_triggers += [{'name': 'separate_generic_port_alignment', 'triggers': ['isEndGenericMap']}]
