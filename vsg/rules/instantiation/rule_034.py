
from vsg import rule
from vsg import token
from vsg import violation


class rule_034(rule.Rule):
    '''
    Checks for component or entity instantiations.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       The token types to check the case on.
    '''

    def __init__(self):
        rule.Rule.__init__(self, name='instantiation', identifier='034')
        self.phase = 1
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
