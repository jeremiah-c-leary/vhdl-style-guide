
from vsg.rules import keyword_alignment_rule


class rule_010(keyword_alignment_rule):
    '''
    Instantiation rule 010 ensures the alignment of the => operator for each generic and port in the instantiation.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'instantiation', '010')
        self.solution = 'Inconsistent alignment of "=>" in generic or port assignments of instantiation.'
        self.sKeyword = '=>'
        self.sStartGroupTrigger = 'isInstantiationDeclaration'
        self.sEndGroupTrigger = 'isInstantiationPortEnd'
        self.lLineTriggers = ['isInstantiationGenericAssignment', 'isInstantiationPortAssignment']

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.configuration_triggers += [{'name': 'separate_generic_port_alignment', 'triggers': ['isInstantiationGenericEnd']}]
