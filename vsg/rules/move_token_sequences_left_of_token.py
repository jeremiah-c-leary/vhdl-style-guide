
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class move_token_sequences_left_of_token(rule.Rule):
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
    '''

    def __init__(self, name, identifier, lSequences, oLeftToken):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lSequences = lSequences
        self.oLeftToken = oLeftToken

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        lPrevious = []
        for lSequence in self.lSequences:
            if not lSequence[0] in lPrevious:
                aToi = oFile.get_tokens_bounded_by(lSequence[0], self.oLeftToken, bIncludeTillBeginningOfLine=True)
                lToi = utils.combine_two_token_class_lists(lToi, aToi)
            lPrevious.append(lSequence[0])
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for iToken, oToken in enumerate(lTokens):
                for lSequence in self.lSequences:
                    bFound = False
                    if isinstance(oToken, lSequence[0]):
                        if utils.are_next_consecutive_token_types(lSequence, iToken, lTokens):
                            bFound = True
                            break
                        if utils.are_next_consecutive_token_types(lSequence[:-1], iToken, lTokens):
                            dAction = {}
                            dAction['num_tokens'] = len(lSequence) - 1
                        elif utils.are_next_consecutive_token_types(lSequence[:-2], iToken, lTokens):
                            dAction = {}
                            dAction['num_tokens'] = len(lSequence) - 2

                if bFound:
                    break
            else:
                sSolution = self.solution
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action(dAction)
                oViolation.set_remap()
                oViolation.fix_blank_lines = True
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        bInsertBlankLine = False
        if isinstance(lTokens[0], parser.whitespace):
            lTokens = lTokens[1:]
            bInsertBlankLine = True
        lMoveTokens = lTokens[0:dAction['num_tokens']]
        lTokens = lTokens[dAction['num_tokens']:]
        lTokens = lTokens[:-1] + lMoveTokens + [parser.whitespace(' ')] + [lTokens[-1]]
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        if bInsertBlankLine:
            rules_utils.insert_blank_line(lTokens, 0)
        oViolation.set_tokens(lTokens)
