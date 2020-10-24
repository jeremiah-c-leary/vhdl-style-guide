
from vsg.rules import remove_comments_from_end_of_lines_bounded_by_tokens

from vsg import token

oStart = token.component_instantiation_statement.instantiation_label

oEnd = token.component_instantiation_statement.semicolon


class rule_023(remove_comments_from_end_of_lines_bounded_by_tokens):
    '''
    Checks for comments after port and generic assignments.
    '''

    def __init__(self):
        remove_comments_from_end_of_lines_bounded_by_tokens.__init__(self, 'instantiation', '023', oStart, oEnd)
        self.solution = 'Remove comment.'
