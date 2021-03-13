
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

lIfBoundingTokens = [token.if_statement.if_keyword, token.if_statement.then_keyword]

lElsifBoundingTokens = [token.if_statement.elsif_keyword, token.if_statement.then_keyword]

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword


lAssignments = []
lAssignments.append(token.simple_waveform_assignment.assignment)
lAssignments.append(token.simple_force_assignment.assignment)
lAssignments.append(token.simple_release_assignment.assignment)

lEndAssignments = []
lEndAssignments.append(token.simple_waveform_assignment.semicolon)
lEndAssignments.append(token.simple_force_assignment.semicolon)
lEndAssignments.append(token.simple_release_assignment.semicolon)


class rule_003(rule.Rule):
    '''
    Checks for after keywords in waveform_elements in the reset part of a clock process.

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
        rule.Rule.__init__(self, 'after', '003')
        self.solution = None
        self.disable = True
        self.phase = 1
        self.oStart = oStart
        self.oEnd = oEnd
        self.magnitude = 1
        self.units = 'ns'
        self.configuration.extend(['magnitude', 'units'])

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.oStart, self.oEnd)

    def _analyze(self, lToi):
        lNewToi = []

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            bInsideAssignment = False
            bResetFound = False
            iStartIndex = None

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if detect_clock_definition(iToken, oToken, lTokens):
                    if bResetFound:
                        lNewToi.append(oToi.extract_tokens(iStartIndex, iToken))
                        break

                if isinstance(oToken, token.if_statement.if_keyword) and oToken.get_hierarchy() == 0:
                    iStartIndex = iToken
                    bResetFound = True

        for oToi in lNewToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            bAfterFound = False

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if not bInsideAssignment:
                    if detect_signal_assignment(oToken):
                        bInsideAssignment = True
                    continue

                if bAfterFound:
                    if detect_end_signal_assignment(oToken):
                        oNewToi = oToi.extract_tokens(iStartIndex, iToken)
                        sSolution = 'Remove *after* from signals in reset portion of a clock process'
                        oViolation = violation.New(iLine, oNewToi, sSolution)
                        self.add_violation(oViolation)
                        bInsideAssignment = False
                        bAfterFound = False

                if isinstance(oToken, token.waveform_element.after_keyword):
                    if isinstance(lTokens[iToken - 1], parser.whitespace):
                        iStartIndex = iToken - 1
                    else:
                        iStartIndex = iToken
                    bAfterFound = True

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lNewTokens = []
        lNewTokens.append(lTokens[-1])
        oViolation.set_tokens(lNewTokens)


def detect_clock_definition(iToken, oToken, lTokens):
    if isinstance(oToken, token.if_statement.if_keyword) or isinstance(oToken, token.if_statement.elsif_keyword):
        if oToken.get_hierarchy() != 0:
            return False
        if utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis, token.ieee.std_logic_1164.function.rising_edge], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([token.ieee.std_logic_1164.function.rising_edge], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis, token.ieee.std_logic_1164.function.falling_edge], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([token.ieee.std_logic_1164.function.falling_edge], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([None, parser.tic, parser.event_keyword, token.logical_operator.and_operator, None, token.relational_operator.equal], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis, None, parser.tic, parser.event_keyword, token.logical_operator.and_operator, None, token.relational_operator.equal], iToken + 1, lTokens):
            return True
    return False


def detect_signal_assignment(oToken):
    for oAssignment in lAssignments:
        if isinstance(oToken, oAssignment):
            return True
    return False


def detect_end_signal_assignment(oToken):
    for oEndAssignment in lEndAssignments:
        if isinstance(oToken, oEndAssignment):
            return True
    return False
