
from vsg.rules import align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)

oStartToken = token.for_generate_statement.generate_keyword
oEndToken = token.generate_statement_body.begin_keyword

lBetweenTokens = []
lBetweenTokens.append([token.for_generate_statement.for_keyword, token.for_generate_statement.end_keyword])

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_401(align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens):
    '''
    Checks the alignment of declaration identifiers in the generate declarative region.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens.__init__(self, 'generate', '401', lAlign, oStartToken, oEndToken, lBetweenTokens, lUnless)
        self.solution = 'Align colon.'
        self.subphase = 2
