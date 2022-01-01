
from vsg.rules import remove_tokens

from vsg.token import case_statement as token

lTokens = []
lTokens.append(token.end_case_label)


class rule_020(remove_tokens):
    '''
    This rule checks for labels after the **end case** keywords.
    The label should be removed.
    The preference is to have comments above the case statement.

    **Violation**

    .. code-block:: vhdl

          end case CASE_LABEL;
          end case;

    **Fix**

    .. code-block:: vhdl

          end case;
          end case;
    '''

    def __init__(self):
        remove_tokens.__init__(self, 'case', '020', lTokens)
        self.solution = 'Remove Label'
