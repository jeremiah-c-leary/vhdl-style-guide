
from vsg.rules import keyword_alignment_rule


class rule_029(keyword_alignment_rule):
    '''
    Instantiation rule 029 ensures the alignment of inline comments in an instantiation.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'instantiation', '029')
        self.solution = 'Inconsistent alignment of comments in instantiation.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isInstantiationDeclaration'
        self.sEndGroupTrigger = 'isInstantiationPortEnd'
        self.lLineTriggers = ['hasInlineComment']

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.configuration_triggers += [{'name': 'separate_generic_port_alignment', 'triggers': ['isInstantiationGenericEnd']}]
