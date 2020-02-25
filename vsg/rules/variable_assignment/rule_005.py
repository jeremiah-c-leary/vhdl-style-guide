
from vsg.rules import keyword_alignment_rule

class rule_005(keyword_alignment_rule):
    '''
    Variable assignment rule 005 ensures the alignment of the ":=" keyword over multiple lines.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'variable_assignment', '005')
        self.solution = 'Inconsistent alignment of ":=" in group of lines.'
        self.sKeyword = ':='
        self.sStartGroupTrigger = 'isProcessBegin'
        self.sEndGroupTrigger = 'isEndProcess'
        self.lLineTriggers = ['isVariableAssignment']

        self.if_control_statements_end_group = True
        self.configuration.append('if_control_statements_end_group')

        self.configuration_triggers += [{'name': 'if_control_statements_end_group', 'triggers': ['isIfKeyword',
                                                                                                 'isElseIfKeyword',
                                                                                                 'isElseKeyword',
                                                                                                 'isEndIfKeyword']}]
