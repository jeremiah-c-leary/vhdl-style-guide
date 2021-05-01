
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens(rule.Rule):
    '''
    Moves one token next to several possible tokens if it exists.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token type
       The token to move.

    lTokens : list of token type
       The token types to move oToken to.
       This is an ordered list with the left item containing the token furthest way from oToken.
    '''

    def __init__(self, name, identifier, oMoveToken, lAnchorTokens, oStartToken, oEndToken, bInsertWhitespace=False):
        rule.Rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 1
        self.oMoveToken = oMoveToken
        self.lAnchorTokens = lAnchorTokens
        self.oStartToken = oStartToken
        self.oEndToken = oEndToken
        self.bInsertWhitespace = bInsertWhitespace

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.oStartToken, self.oEndToken, bIncludeTillEndOfLine=True)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            if not utils.does_token_type_exist_in_list_of_tokens(self.oMoveToken, lTokens):
                continue
            dAction = {}
            bPassing = False
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                for oAnchorToken in self.lAnchorTokens:
                    if isinstance(oToken, oAnchorToken):
                        dAction['insert'] = iToken + 1
                        sAnchorToken = oToken.get_value()
                        iAnchorLine = iLine
                        if utils.are_next_consecutive_token_types([parser.whitespace, self.oMoveToken], iToken + 1, lTokens):
                            bPassing = True
                            break
                        elif isinstance(lTokens[iToken + 1], self.oMoveToken):
                            bPassing = True
                            break
                if isinstance(oToken, self.oMoveToken):
                    iAnchorLine = iLine
                    dAction['move_index'] = iToken
                    sSolution = 'Move "' + oToken.get_value() + '" on line ' + str(iLine) + ' to the right of "' + sAnchorToken + '" on line ' + str(iAnchorLine)
                if bPassing:
                    break
            else:
                oViolation = violation.New(iAnchorLine, oToi, sSolution)
                oViolation.set_action(dAction)
                oViolation.set_remap()
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        oToken = lTokens.pop(dAction['move_index'])
        rules_utils.insert_token(lTokens, dAction['insert'], oToken)
        if self.bInsertWhitespace:
            rules_utils.insert_whitespace(lTokens, dAction['insert'])
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        lTokens = utils.fix_blank_lines(lTokens)
        oViolation.set_tokens(lTokens)
