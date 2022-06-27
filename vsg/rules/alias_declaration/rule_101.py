
from vsg.rules.whitespace_before_token_if_on_same_line_as_token import Rule

from vsg.token import alias_declaration as token


class rule_101(Rule):
    '''
    This rule checks for a single space before the **is** keyword if the : is present.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       alias alias_designator : subtype_indication     is name;
       alias alias_designator   is name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator : subtype_indication is name;
       alias alias_designator   is name;
    '''
    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '101')
        self.oFirstToken = token.is_keyword
        self.oExceptToken = token.colon
