
from vsg import proposed_rule


class rule_028(proposed_rule.Rule):
    '''
    .. NOTE:: This rule has not been implemented yet.

    This rule checks for alignment of inline comments in the context declaration.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       context c1 is                       -- Some comment
         library ieee;                        -- Other comment
           use ieee.std_logic_1164.all;   -- Comment 3
       end context c1;  -- Comment 4

    **Fix**

    .. code-block:: vhdl

       context c1 is                    -- Some comment
         library ieee;                  -- Other comment
           use ieee.std_logic_1164.all; -- Comment 3
       end context c1;                  -- Comment 4
    '''

    def __init__(self):
        proposed_rule.Rule.__init__(self, 'context', '028')
