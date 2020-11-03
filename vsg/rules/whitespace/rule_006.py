
from vsg import parser

from vsg.rules import remove_spaces_before_token_rule


class rule_006(remove_spaces_before_token_rule):
    '''
    Checks for spaces before close parenthesis
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'whitespace', '006', parser.close_parenthesis, bIgnoreIfLineStart=True)
        self.solution = 'Remove spaces before close ).'
