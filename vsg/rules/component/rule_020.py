
from vsg.rules import keyword_alignment_rule


class rule_020(keyword_alignment_rule):
    '''
    Component rule 020 ensures the alignment of inline comments in a component declaration.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'component', '020')
        self.solution = 'Inconsistent alignment of comments in a component declaration.'
        self.sKeyword = '--'
        self.sStartGroupTrigger = 'isComponentDeclaration'
        self.sEndGroupTrigger = 'isComponentEnd'
        self.lLineTriggers = ['hasInlineComment']
        self.phase = 6

        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')

        self.configuration_triggers += [{'name': 'separate_generic_port_alignment', 'triggers': ['isEndGenericMap']}]
