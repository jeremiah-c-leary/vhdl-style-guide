
from vsg import parser
from vsg import token

from vsg.rules import remove_carriage_returns_between_token_pairs

lTokens = []
lTokens.append([token.if_statement.if_keyword, parser.todo])
lTokens.append([token.if_statement.if_keyword, parser.open_parenthesis])
lTokens.append([token.if_statement.elsif_keyword, parser.todo])
lTokens.append([token.if_statement.elsif_keyword, parser.open_parenthesis])


class rule_035(remove_carriage_returns_between_token_pairs):
    '''
    Checks code after the **elsif** keyword are on the same line as the **elsif** keyword.
    '''

    def __init__(self):
        remove_carriage_returns_between_token_pairs.__init__(self, 'if', '035', lTokens, bInsertSpace=True)
        self.solution = 'Merge lines with **elsif** keyword and expression below.'
