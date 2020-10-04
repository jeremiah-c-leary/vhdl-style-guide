
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_generate_alternative.when_keyword)


class rule_016(token_indent):
    '''
    Generate rule 016 checks the indent of the when keywords in case generate statements.
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '016', lTokens)
