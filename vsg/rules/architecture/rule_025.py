
from vsg.rules import is_token_value_one_of

from vsg.token import architecture_body as token


class rule_025(is_token_value_one_of):
    '''
    This rule checks for valid names for the architecture.
    Typical architecture names are:  RTL, EMPTY, and BEHAVE.
    This rule allows the user to restrict what can be used for an architecture name.

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

    **Violation**

    .. code-block:: vhdl

       architecture some_invalid_arch_name of entity1 is

    **Fix**

    The user is required to decide which is the correct architecture name.
    '''

    def __init__(self):
        is_token_value_one_of.__init__(self, 'architecture', '025', token.identifier)

    def _get_solution(self, iLineNumber):
        return 'Architecture identifier must be from this list: ' + ', '.join(self.names)
