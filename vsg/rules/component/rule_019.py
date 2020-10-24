
from vsg.rules import remove_comments_from_end_of_lines_bounded_by_tokens

from vsg import token

oStart = token.component_declaration.component_keyword

oEnd = token.component_declaration.semicolon


class rule_019(remove_comments_from_end_of_lines_bounded_by_tokens):
    '''
    Checks for comments after port and generic assignments.
    '''

    def __init__(self):
        remove_comments_from_end_of_lines_bounded_by_tokens.__init__(self, 'component', '019', oStart, oEnd)
        self.solution = 'Remove comment.'
