
from vsg import parser

from vsg.rules import remove_spaces_before_token_rule


class rule_004(remove_spaces_before_token_rule):
    '''
    Whitespace rule 004 checks for spaces before semicolons
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'whitespace', '004', parser.comma)
        self.solution = 'Remove spaces before commas.'
