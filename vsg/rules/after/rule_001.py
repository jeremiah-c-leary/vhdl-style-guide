
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


class rule_001(rule.Rule):
    '''
    Checks the case for words.

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
        rule.Rule.__init__(self, 'after', '001')
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
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            bInsideClockDef = False
            bInsideAssignment = False
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if not bInsideClockDef:
                    bInsideClockDef = detect_clock_definition(iToken, oToken, lTokens)
                    continue

                if isinstance(oToken, token.if_statement.semicolon) and oToken.get_hierarchy() == 0:
                    bInsideClockDef = False
                    continue

                if not bInsideAssignment:
                    bInsideAssignment = detect_signal_assignment(oToken)
                    continue

                if bInsideAssignment:
                    if isinstance(oToken, token.waveform_element.after_keyword):
                        bInsideAssignment = False
                    if detect_end_signal_assignment(oToken):
                        oNewToi = oToi.extract_tokens(iToken, iToken)
                        sSolution = 'Add after ' + str(self.magnitude) + ' ' + self.units + ' to signal in clock process'
                        oViolation = violation.New(iLine, oNewToi, sSolution)
                        self.add_violation(oViolation)
                        bInsideAssignment = False

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lNewTokens = []
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(token.waveform_element.after_keyword('after'))
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(parser.todo(str(self.magnitude)))
        lNewTokens.append(parser.whitespace(' '))
        lNewTokens.append(parser.todo(self.units))
        lNewTokens.extend(lTokens)

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
