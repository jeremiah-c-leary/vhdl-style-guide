
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils

lTokens = []
lTokens.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)

oLeftToken = token.architecture_body.begin_keyword

oRightToken = token.architecture_body.end_keyword

lStart = []
lStart.append(token.concurrent_selected_signal_assignment.target)
lStart.append(token.concurrent_conditional_signal_assignment.target)
lStart.append(token.concurrent_simple_signal_assignment.target)

lEnd = []
lEnd.append(token.concurrent_selected_signal_assignment.semicolon)
lEnd.append(token.concurrent_conditional_signal_assignment.semicolon)
lEnd.append(token.concurrent_simple_signal_assignment.semicolon)


class rule_008(alignment.Rule):
    '''
    This rule checks the alignment of inline comments in consecutive concurrent statements.
    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0';     -- Write enable
       rd_en <= '1';   -- Read enable
       data  <= (others => '0'); -- Write data

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0';             -- Write enable
       rd_en <= '1';             -- Read enable
       data  <= (others => '0'); -- Write data
    '''

    def __init__(self):
        alignment.Rule.__init__(self, 'concurrent', '008')
        self.subphase = 3
        self.lTokens = lTokens
        self.left_token = oLeftToken
        self.right_token = oRightToken
        self.lSkip = lSkip
        self.lStart = lStart
        self.lEnd = lEnd
        ## Stuff below is from original keyword_alignment_rule
        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')
        self.include_lines_without_comments = False
        self.configuration.append('include_lines_without_comments')

    def analyze(self, oFile):

        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            dAnalysis = {}
            iColumn = 0
            iToken = -1
            iLeftColumn = 0
            bStartFound = False
            bEndFound = False

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]
#               print(f'{oToken} | {oToken.get_value()}')

               if bStartFound:
                   if isinstance(oToken, parser.carriage_return):
                       if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([parser.comment], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)
                           dAnalysis = {}
                           bStartFound = False
                           bEndFound = False

                           iLine += 1
                           iLeftColumn = 0
                           iColumn = 0
                           iToken = -1
                           continue

                   elif isinstance(oToken, parser.comment):
#                       print(f'--> Comment Found     | {iLine} | {iColumn}')
                       dAnalysis[iLine] = {}
                       dAnalysis[iLine]['token_column'] = iColumn
                       dAnalysis[iLine]['token_index'] = iToken
                       dAnalysis[iLine]['line_number'] = iLine
                       if isinstance(lTokens[iIndex -1], parser.whitespace):
                           dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                       else:
                           dAnalysis[iLine]['left_column'] = iColumn

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   iLeftColumn = 0
                   iColumn = 0
                   iToken = -1
               else:
                   iLeftColumn += oToken.length()
                   iColumn += oToken.length()

               if bEndFound:
                   for oStartToken in self.lStart:
                       if isinstance(oToken, oStartToken):
                           bStartFound = False
                           bEndFound = False
                           break
                   else:
                       if not isinstance(oToken, parser.whitespace) and \
                          not isinstance(oToken, parser.comment) and \
                          not isinstance(oToken, parser.carriage_return):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)
                           dAnalysis = {}
                           bStartFound = False
                           bEndFound = False
                           continue

               if bStartFound:
                   for oEndToken in self.lEnd:
                       if isinstance(oToken, oEndToken):
#                           print(f'--> End Token Found   | {iLine} | {iColumn}')
                           bEndFound = True
                           break
               else:
                   for oStartToken in self.lStart:
                       if isinstance(oToken, oStartToken):
#                           print(f'--> Start Token Found | {iLine} | {iColumn} | {oToken}')
                           bStartFound = True
                           break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        iTokenIndex = dAction['token_index']

        if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
            iLen = len(lTokens[iTokenIndex - 1].get_value())
            lTokens[iTokenIndex - 1].set_value(' '*(iLen + dAction['adjust']))
        else:
            rules_utils.insert_whitespace(lTokens, iTokenIndex, dAction['adjust'])
        oViolation.set_tokens(lTokens)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment, include_lines_without_comments=False, iMaxColumn=0):
    iMaxLeftColumn = 0
    iMaxTokenColumn = 0
    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['left_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['token_column'])

    if include_lines_without_comments:
        iMaxTokenColumn = max(iMaxTokenColumn, iMaxColumn)

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['token_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['token_column']
