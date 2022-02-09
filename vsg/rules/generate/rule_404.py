
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
lAlign.append(token.alias_declaration.alias_designator)

oStartToken = token.case_generate_alternative.assignment
oEndToken = token.generate_statement_body.begin_keyword

lBetweenTokens = []
lBetweenTokens.append([token.case_generate_statement.case_keyword, token.case_generate_statement.end_keyword])

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_404(align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens):
    '''
    This rule checks the identifiers for all declarations are aligned in the generate declarative part in case generate statements.

    |configuring_identifier_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable    var1 : natural;
       constant  c_period : time;

    **Fix**

    .. code-block:: vhdl

       variable var1     : natural;
       constant c_period : time;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens.__init__(self, 'generate', '404', lAlign, oStartToken, oEndToken, lBetweenTokens, lUnless)
        self.solution = 'Align identifer.'
