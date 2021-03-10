
import sys

from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils

lIfBoundingTokens = [token.if_statement.if_keyword, token.if_statement.then_keyword]

lElsifBoundingTokens = [token.if_statement.elsif_keyword, token.if_statement.then_keyword]

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword


class rule_029(rule.Rule):
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
        rule.Rule.__init__(self, 'process', '029')
        self.solution = None
        self.phase = 1
        self.clock = 'event'
        self.configuration.append('clock')
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        aToi = oFile.get_tokens_bounded_by_token_when_between_tokens(lElsifBoundingTokens[0], lElsifBoundingTokens[1], oStart, oEnd)
        lToi = utils.combine_two_token_class_lists(lToi, aToi)
        aToi = oFile.get_tokens_bounded_by_token_when_between_tokens(lIfBoundingTokens[0], lIfBoundingTokens[1], oStart, oEnd)
        lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bEventFound = False
            iStartIndex = 0
            for iToken, oToken in enumerate(lTokens):
                if self.clock == 'edge':
                    if utils.are_next_consecutive_token_types_ignoring_whitespace([parser.tic, parser.event_keyword, token.logical_operator.and_operator, None, token.relational_operator.equal], iToken + 1, lTokens):
                        bEventFound = True
                        iStartIndex = iToken
                        sSolution = 'Change event to rising_edge/falling_edge.'
                        dAction = {}
                        dAction['convert_to'] = 'edge'
                        dAction['clock'] = oToken.get_value()
                    if bEventFound and isinstance(oToken, parser.character_literal):
                        if oToken.get_value() == "'1'":
                            dAction['edge'] = 'rising_edge'
                        else:
                            dAction['edge'] = 'falling_edge'
                        oMyToi = oToi.extract_tokens(iStartIndex, iToken)
                        oViolation = violation.New(oToi.get_line_number(), oMyToi, sSolution)
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)
                        bEventFound = False

                elif self.clock == 'event':

                    if isinstance(oToken, token.ieee.std_logic_1164.function.rising_edge):
                        sSolution = 'Change rising_edge to event format.'
                        iStartIndex = iToken
                        dAction = {}
                        dAction['convert_to'] = 'event'
                        dAction['edge'] = "'1'"
                        bEventFound = True

                    elif isinstance(oToken, token.ieee.std_logic_1164.function.falling_edge):
                        sSolution = 'Change falling_edge to event format.'
                        iStartIndex = iToken
                        dAction = {}
                        dAction['convert_to'] = 'event'
                        dAction['edge'] = "'0'"
                        bEventFound = True

                    if bEventFound and isinstance(oToken, parser.todo):
                        dAction['clock'] = oToken.get_value()

                    if bEventFound and isinstance(oToken, parser.close_parenthesis):
                        oMyToi = oToi.extract_tokens(iStartIndex, iToken)
                        oViolation = violation.New(oToi.get_line_number(), oMyToi, sSolution)
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)
                        bEventFound = False
                else:
                    sys.stderr.write('Invalid configuration option ' + self.clock)
                    exit(1)

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction['convert_to'] == 'edge':
            lTokens = []
            if dAction['edge'] == 'rising_edge':
                lTokens.append(token.ieee.std_logic_1164.function.rising_edge('rising_edge'))
            else:
                lTokens.append(token.ieee.std_logic_1164.function.falling_edge('falling_edge'))

            lTokens.append(parser.open_parenthesis())
            lTokens.append(parser.todo(dAction['clock']))
            lTokens.append(parser.close_parenthesis())
        else:
            lTokens = []
            lTokens.append(parser.todo(dAction['clock']))
            lTokens.append(parser.tic("'"))
            lTokens.append(parser.event_keyword('event'))
            lTokens.append(parser.whitespace(' '))
            lTokens.append(token.logical_operator.and_operator('and'))
            lTokens.append(parser.whitespace(' '))
            lTokens.append(parser.todo(dAction['clock']))
            lTokens.append(parser.whitespace(' '))
            lTokens.append(token.relational_operator.equal('='))
            lTokens.append(parser.whitespace(' '))
            lTokens.append(parser.character_literal(dAction['edge']))

        oViolation.set_tokens(lTokens)
