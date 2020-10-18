
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

from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.simple_variable_assignment.assignment)
lAlign.append(token.conditional_variable_assignment.assignment)
lAlign.append(token.selected_variable_assignment.assignment)

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword

lUnless = []


class rule_005(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'variable_assignment', '005', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align identifer.'
        self.if_control_statements_ends_group = True
        self.case_control_statements_ends_group = True
