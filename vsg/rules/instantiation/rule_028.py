
from vsg import rule
from vsg import token
from vsg import violation


class rule_028(rule.Rule):
    '''
    Instantiation rule 028 checks the entity name is uppercase in direct instantiations.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    '''

    def __init__(self):
        rule.Rule.__init__(self, name='instantiation', identifier='028')
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([token.instantiated_unit.entity_name])

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            dAction = {}
            if '.' in lTokens[0].get_value():
                lTemp = lTokens[0].get_value().split('.')
                sObjectValue = lTemp[-1]
                dAction['period'] = True
            else:
                sObjectValue = lTokens[0].get_value()
                dAction['period'] = False

            if self.case == 'lower':
                if not sObjectValue.islower():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
            if self.case == 'upper':
                if not sObjectValue.isupper():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if not dAction['period']:
            if self.case == 'lower':
                lTokens[0].set_value(lTokens[0].get_value().lower())
            if self.case == 'upper':
                lTokens[0].set_value(lTokens[0].get_value().upper())
        else:
            lTemp = lTokens[0].get_value().split('.')
            if self.case == 'lower':
                lTemp[-1] = lTemp[-1].lower()
            if self.case == 'upper':
                lTemp[-1] = lTemp[-1].upper()
            lTokens[0].set_value('.'.join(lTemp))
        oViolation.set_tokens(lTokens)
