

from vsg import parser
from vsg import violation

from vsg.rule_group import structure
from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class split_line_at_token_if_on_same_line_as_token_if_token_pair_are_not_on_the_same_line(structure.Rule):
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

    def __init__(self, name, identifier, oToken, oSameLineToken, lTokenPair):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oToken = oToken
        self.oSameLineToken = oSameLineToken
        self.lTokenPair = lTokenPair

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.lTokenPair[0], self.lTokenPair[1])
        lToi = extract_multi_line_statements(lToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                if isinstance(oToken, self.oSameLineToken):
                    if utils.are_next_consecutive_token_types([parser.whitespace, self.oToken], iToken + 1, lTokens) or \
                       utils.are_next_consecutive_token_types([self.oToken], iToken + 1, lTokens):
                        sSolution = self.solution
                        oViolation = violation.New(iLine, oToi, sSolution)
                        dAction = {}
                        dAction['insert_index'] = iToken + 1
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        rules_utils.insert_carriage_return(lTokens, dAction['insert_index'])
        oViolation.set_tokens(lTokens)


def extract_multi_line_statements(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        for oToken in lTokens:
            if isinstance(oToken, parser.carriage_return):
                lReturn.append(oToi)
                break
    return lReturn
