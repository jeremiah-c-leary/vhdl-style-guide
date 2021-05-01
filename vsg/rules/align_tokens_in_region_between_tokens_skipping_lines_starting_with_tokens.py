

from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region

    lSkip : token object list
       List of tokens to skip if they start a line.
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token, lSkip):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 5
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.lSkip = lSkip
        ## Stuff below is from original keyword_alignment_rule
        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')
        self.separate_generic_port_alignment = True
        self.configuration.append('separate_generic_port_alignment')
        self.include_lines_without_comments = False
        self.configuration.append('include_lines_without_comments')

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            bSkip = False
            iMaxColumn = 0
            iLeftColumn = 0
            dAnalysis = {}

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]
               iLeftColumn += oToken.length()

               if not bTokenFound and not bSkip:
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

               if isinstance(oToken, token.generic_clause.semicolon) and self.separate_generic_port_alignment:
                   add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                   for iKey in list(dAnalysis.keys()):
                       if dAnalysis[iKey]['adjust'] != 0:
                           oLineTokens = oFile.get_tokens_from_line(iKey)
                           sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                           oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                           oViolation.set_action(dAnalysis[iKey])
                           self.add_violation(oViolation)

                   dAnalysis = {}

               if isinstance(oToken, token.generic_map_aspect.close_parenthesis) and self.separate_generic_port_alignment:
                   add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                   for iKey in list(dAnalysis.keys()):
                       if dAnalysis[iKey]['adjust'] != 0:
                           oLineTokens = oFile.get_tokens_from_line(iKey)
                           sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                           oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                           oViolation.set_action(dAnalysis[iKey])
                           self.add_violation(oViolation)

                   dAnalysis = {}

               if isinstance(oToken, parser.comment):
                   iLeftColumn -= lTokens[iIndex].length()
                   if isinstance(lTokens[iIndex - 1], parser.whitespace):
                       iLeftColumn -= lTokens[iIndex - 1].length()

               if isinstance(oToken, parser.carriage_return):

                   iMaxColumn = max(iMaxColumn, iLeftColumn)
                   iLeftColumn = 0

                   iLine += 1
                   iColumn = 0
                   bTokenFound = False
                   iToken = -1

                   if bSkip:
                       bSkip = False

                   for oSkip in self.lSkip:
                       if utils.are_next_consecutive_token_types([parser.whitespace, oSkip], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([oSkip], iIndex + 1, lTokens):
                           bSkip = True
                           break

                   if bSkip:
                       continue

                   if self.comment_line_ends_group:
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
                   if self.blank_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                           add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}



            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment, self.include_lines_without_comments, iMaxColumn)


            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    sSolution = 'Move ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                    oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
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
