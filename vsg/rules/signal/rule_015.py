
from vsg.rules import separate_multiple_signal_identifiers_into_individual_statements

iAllow = 2


class rule_015(separate_multiple_signal_identifiers_into_individual_statements):
    '''
    This rule checks for multiple signal names defined in a single signal declaration.
    By default, this rule will only flag more than two signal declarations.

    Refer to `Configuring Number of Signals in Signal Declaration <configuring_number_of_signals_in_signal_declaration.html>`_ for information on changing the default.

    **Violation**

    .. code-block:: vhdl

       signal sig1, sig2
         sig3, sig4,
         sig5
         : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal sig1 : std_logic;
       signal sig2 : std_logic;
       signal sig3 : std_logic;
       signal sig4 : std_logic;
       signal sig5 : std_logic;
    '''

    def __init__(self):
        separate_multiple_signal_identifiers_into_individual_statements.__init__(self, 'signal', '015', iAllow)
