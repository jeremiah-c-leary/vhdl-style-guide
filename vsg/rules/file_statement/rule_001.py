
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.file_declaration.file_keyword)
lTokens.append(token.file_open_information.open_keyword)
lTokens.append(token.file_open_information.is_keyword)


class rule_001(token_indent):
    '''
    Constant rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'file', '001', lTokens)
