
from vsg import rule
from vsg import token
from vsg import violation


class formal_part_in_association_element_between_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oStart : token object type
       The beginning of the range

    oEnd : token object type
       The end of the range
    '''

    def __init__(self, name, identifier, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.fixable = False
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_association_elements_between_tokens(self.oStart, self.oEnd)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            for oToken in lTokens:
                if isinstance(oToken, token.association_element.assignment):
                    bFound = True
                    break
            if not bFound:
                sSolution = self.solution
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        return None
