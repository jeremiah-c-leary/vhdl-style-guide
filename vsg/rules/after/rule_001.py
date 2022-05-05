
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import structure

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


class rule_001(structure.Rule):
    '''
    This rule checks for **after x** in signal assignments in clock processes.

    **Violation**

    .. code-block:: vhdl

       clk_proc : process(clock, reset) is
       begin
         if (reset = '1') then
           a <= '0';
           b <= '1';
         elsif (clock'event and clock = '1') then
           a <= d;
           b <= c;
         end if;
       end process clk_proc;

    **Fix**

    .. code-block:: vhdl

       clk_proc : process(clock, reset) is
       begin
         if (reset = '1') then
           a <= '0';
           b <= '1';
         elsif (clock'event and clock = '1') then
           a <= d after 1 ns;
           b <= c after 1 ns;
         end if;
       end process clk_proc;

    .. NOTE::  This rule has two configurable items:

       * magnitude
       * units

       The **magnitude** is the number of units.  Default is *1*.

       The **units** is a valid time unit: ms, us, ns, ps etc...  Default is *ns*.
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'after', '001')
        self.disable = True
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
           utils.are_next_consecutive_token_types_ignoring_whitespace([None, parser.tic, token.predefined_attribute.event_keyword, token.logical_operator.and_operator, None, token.relational_operator.equal], iToken + 1, lTokens) or \
           utils.are_next_consecutive_token_types_ignoring_whitespace([parser.open_parenthesis, None, parser.tic, token.predefined_attribute.event_keyword, token.logical_operator.and_operator, None, token.relational_operator.equal], iToken + 1, lTokens):
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
