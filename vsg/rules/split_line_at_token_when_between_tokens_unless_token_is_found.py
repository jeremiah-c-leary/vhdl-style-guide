

from vsg import parser
from vsg import violation

from vsg.rule_group import structure
from vsg.rules import utils as rules_utils


class split_line_at_token_when_between_tokens_unless_token_is_found(structure.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at

    oStart : token type
       The start of the range

    oEnd : token type
       The end of the range
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd, oStop):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.oStop = oStop

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(self.lTokens, 2, self.oStart, self.oEnd, self.oStop)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
                continue
            sSolution = self.solution
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[1], parser.whitespace):
            rules_utils.insert_carriage_return(lTokens, -2)
        else:
            rules_utils.insert_carriage_return(lTokens, -1)
        oViolation.set_tokens(lTokens)
