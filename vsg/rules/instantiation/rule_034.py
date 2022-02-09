
from vsg import token
from vsg import violation
from vsg.rule_group import structure


class rule_034(structure.Rule):
    '''
    This rule checks for component versus direct instantiations.

    |configuring_type_of_instantiations_link|

    component instantiation
    ^^^^^^^^^^^^^^^^^^^^^^^

    .. NOTE:: This is the default configuration

    **Violation**

    .. code-block:: vhdl

       U_FIFO : entity fifo_dsn.FIFO(RTL)


    entity instantiation
    ^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       U_FIFO : component FIFO

       U_FIFO : FIFO
    '''

    def __init__(self):
        structure.Rule.__init__(self, name='instantiation', identifier='034')
        self.method = 'component'
        self.configuration.append('method')
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        if self.method == 'component':
            return oFile.get_tokens_matching_in_range_bounded_by_tokens([token.instantiated_unit.entity_keyword], token.component_instantiation_statement.instantiation_label, token.component_instantiation_statement.semicolon)
        else:
            return oFile.get_tokens_matching_in_range_bounded_by_tokens([token.instantiated_unit.component_name], token.component_instantiation_statement.instantiation_label, token.component_instantiation_statement.semicolon)

    def _analyze(self, lToi):
        for oToi in lToi:
            if self.method == 'component':
                sSolution = 'Change to component instantiation'
            else:
                sSolution = 'Change to entity instantiation'
            self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
