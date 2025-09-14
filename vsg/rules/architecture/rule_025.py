# -*- coding: utf-8 -*-

from vsg.rules import does_token_value_match_one_of
from vsg.token import architecture_body as token


class rule_025(does_token_value_match_one_of):
    """
    This rule checks for valid names for the architecture.
    Typical architecture names are:  RTL, EMPTY, and BEHAVE.
    This rule allows the user to restrict what can be used for an architecture name.
    Note that regular expressions are accepted in the **names** field.

    .. NOTE:: This rule is disabled by default.
       You can enable and configure the names using the following configuration.

       .. code-block:: yaml

          ---

          rule :
            architecture_025 :
              disable : False
              names :
                - rtl
                - empty
                - behave
                - my_pattern.*

    **Violation**

    .. code-block:: vhdl

       architecture some_invalid_arch_name of entity1 is

    **Fix**

    The user is required to decide which is the correct architecture name.
    """

    def __init__(self):
        super().__init__(token.identifier)

    def _get_solution(self, iLineNumber):
        return "Architecture identifier must match a name from this list: " + ", ".join(self.names)
