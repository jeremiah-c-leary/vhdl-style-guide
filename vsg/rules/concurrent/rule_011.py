
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.assignment, token.concurrent_simple_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])


class rule_011(rule.Rule):
    '''
    Checks for proper structure of concurrent assignments.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'concurrent', '011')
        self.phase = 1
        self.lTokenPairs = lTokenPairs

        self.new_line_after_assign = 'no'
        self.configuration.append('new_line_after_assign')
        self.ignore_single_line = 'yes'
        self.configuration.append('ignore_single_line')

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            if rules_utils.is_single_line(oToi) and self.ignore_single_line:
                continue

            _check_new_line_after_assign(self, oToi)

        self._sort_violations()

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction['type'] == 'new_line_after_assign':
            _fix_new_line_after_assign(oViolation)


def _check_new_line_after_assign(self, oToi):

    if self.new_line_after_assign == 'ignore':
        return

    iLine, lTokens = utils.get_toi_parameters(oToi)

    iNextToken = utils.find_next_non_whitespace_token(1, lTokens)

    iNumCarriageReturns = utils.count_carriage_returns(lTokens[:iNextToken])

    if iNumCarriageReturns == 0:
        if self.new_line_after_assign == 'yes':
            sSolution = 'Add return after assignment.'
            oViolation = _create_violation(oToi, iLine, 1, 1, 'new_line_after_assign', 'insert', sSolution)
            self.add_violation(oViolation)
    else:
        if self.new_line_after_assign == 'no':
            sSolution = 'Move code after assignment to the same line as assignment.'
            oViolation = _create_violation(oToi, iLine, 0, iNextToken, 'new_line_after_assign', 'remove', sSolution)
            self.add_violation(oViolation)


def _fix_new_line_after_assign(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    if dAction['action'] == 'insert':
        if not isinstance(lTokens[0], parser.whitespace):
            rules_utils.insert_whitespace(lTokens, 0)
        rules_utils.insert_carriage_return(lTokens, 0)
        oViolation.set_tokens(lTokens)
    elif dAction['action'] == 'remove':
        lNewTokens = []
        lNewTokens.append(lTokens[0])
        rules_utils.append_whitespace(lNewTokens)
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def _create_violation(oToi, iLine, iStartIndex, iEndIndex, sType, sAction, sSolution):
    dAction = _create_action_dictionary(sType, sAction)
    oViolation = violation.New(iLine, oToi.extract_tokens(iStartIndex, iEndIndex), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def _create_action_dictionary(sType, sAction):
    dReturn = {}
    dReturn['type'] = sType
    dReturn['action'] = sAction
    return dReturn
