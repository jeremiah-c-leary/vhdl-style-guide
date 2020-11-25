
from vsg.rules import separate_multiple_signal_identifiers_into_individual_statements

iAllow = 2


class rule_015(separate_multiple_signal_identifiers_into_individual_statements):
    '''
    Checks for the proper indentation at the beginning of the signal statement.
    '''

    def __init__(self):
        separate_multiple_signal_identifiers_into_individual_statements.__init__(self, 'signal', '015', iAllow)
