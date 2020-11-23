
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.association_list.comma)

oStart = token.port_map_aspect.open_parenthesis
oEnd = token.port_map_aspect.close_parenthesis


class rule_009(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens):
    '''
    Checks multiple port assignments on the same line.
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens.__init__(self, 'port_map', '009', lTokens, oStart, oEnd)
        self.solution = 'Move multiple port assignments to their own lines.'
