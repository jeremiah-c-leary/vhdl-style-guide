
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rules import utils as rules_utils

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


class rule_002(rule.Rule):
    '''
    Ensures the alignment of the after keyword in clock processes.

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
        rule.Rule.__init__(self, 'after', '002')
        self.solution = 'Align **after** keyword.'
        self.disable = True
        self.phase = 5
        self.subphase = 2
        self.oStart = oStart
        self.oEnd = oEnd
        self.lTokens = [token.waveform_element.after_keyword]
        ## Stuff below is from original keyword_alignment_rule

        self.compact_alignment = True
        self.configuration.append('compact_alignment')
        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')


    def analyze(self, oFile):
        lPreToi = oFile.get_tokens_bounded_by(self.oStart, self.oEnd)
        lToi = []

        for oToi in lPreToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            bInsideClockDef = False
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)

                if not bInsideClockDef:
                    if detect_clock_definition(iToken, oToken, lTokens):
                        bInsideClockDef = True
                        iStartIndex = iToken
                    continue

                if isinstance(oToken, token.if_statement.semicolon) and oToken.get_hierarchy() == 0:
                    lToi.append(oToi.extract_tokens(iStartIndex, iToken))
                    bInsideClockDef = False
                    continue

        ### jcl - need to figure out how to do this better without copying
        dAnalysis = {}
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]

               if not bTokenFound:
                   for oSearch in self.lTokens:
                       if isinstance(oToken, oSearch):
                           bTokenFound = True
                           dAnalysis[iLine] = {}
                           dAnalysis[iLine]['token_column'] = iColumn
                           dAnalysis[iLine]['token_index'] = iToken
                           dAnalysis[iLine]['line_number'] = iLine
                           if isinstance(lTokens[iIndex -1], parser.whitespace):
                               dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                           else:
                               dAnalysis[iLine]['left_column'] = iColumn
                           break

                   iColumn += len(oToken.get_value())

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   iColumn = 0
                   bTokenFound = False
                   iToken = -1
                   if self.comment_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([parser.comment], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, self.solution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if self.blank_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, self.solution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, self.solution)
                    oViolation.set_action(dAnalysis[iKey])
                    self.add_violation(oViolation)

            dAnalysis = {}

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        iTokenIndex = dAction['token_index']

        if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
            iLen = len(lTokens[iTokenIndex - 1].get_value())
            lTokens[iTokenIndex - 1].set_value(' '*(iLen + dAction['adjust']))
        else:
            rules_utils.insert_whitespace(lTokens, iTokenIndex)
        oViolation.set_tokens(lTokens)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['token_column'])

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']


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
