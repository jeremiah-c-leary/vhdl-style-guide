
from vsg.rules import align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)

oStartToken = token.for_generate_statement.generate_keyword
oEndToken = token.generate_statement_body.begin_keyword

lBetweenTokens = []
lBetweenTokens.append([token.for_generate_statement.for_keyword, token.for_generate_statement.end_keyword])

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_400(align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens):
    '''
    Checks the alignment of declaration identifiers in the generate declarative region.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens.__init__(self, 'generate', '400', lAlign, oStartToken, oEndToken, lBetweenTokens, lUnless)
        self.solution = 'Align identifer.'
