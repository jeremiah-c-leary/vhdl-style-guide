
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.full_type_declaration.is_keyword, token.enumeration_type_definition.open_parenthesis])
lTokens.append([token.full_type_declaration.is_keyword, token.range_constraint.range_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.unbounded_array_definition.array_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.constrained_array_definition.array_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.record_type_definition.record_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.access_type_definition.access_keyword])
lTokens.append([token.full_type_declaration.is_keyword, token.file_type_definition.file_keyword])


class rule_007(Rule):
    '''
    This rule checks for a single space after the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       type state_machine is     (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    '''
    def __init__(self):
        Rule.__init__(self, 'type', '007', lTokens)
