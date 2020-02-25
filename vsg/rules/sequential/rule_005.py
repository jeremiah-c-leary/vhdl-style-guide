
from vsg.rules import keyword_alignment_rule


class rule_005(keyword_alignment_rule):
    '''
    Sequential rule 005 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        keyword_alignment_rule.__init__(self, 'sequential', '005')
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
        self.sKeyword = '<='
        self.sStartGroupTrigger = 'isProcessBegin'
        self.sEndGroupTrigger = 'isEndProcess'
        self.lLineTriggers = ['insideSequential']

        self.if_control_statements_end_group = True
        self.configuration.append('if_control_statements_end_group')
        self.case_control_statements_end_group = True
        self.configuration.append('case_control_statements_end_group')

        self.rule_specific_configuration = [{'name': 'if_control_statements_end_group', 'triggers': ['isIfKeyword',
                                                                                                     'isElseIfKeyword',
                                                                                                     'isElseKeyword',
                                                                                                     'isEndIfKeyword']},
                                            {'name': 'case_control_statements_end_group', 'triggers': ['isCaseKeyword',
                                                                                                       'isCaseWhenKeyword',
                                                                                                       'isEndCaseKeyword']}]
