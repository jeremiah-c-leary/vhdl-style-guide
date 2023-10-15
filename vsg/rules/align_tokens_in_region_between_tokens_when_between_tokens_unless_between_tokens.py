

from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rules import alignment_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens(alignment.Rule):
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

    lUnless : token object pairs list
       A list of pairs of tokens in which to exclude alignment
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token, lBetween, lUnless):
        alignment.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.lBetween = lBetween[0]
        self.lUnless = lUnless
        ## attributes below are configurable by the user

        self.compact_alignment = 'yes'
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = 'yes'
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = 'yes'
        self.configuration.append('comment_line_ends_group')

        self.if_control_statements_ends_group = 'no'
        self.configuration.append('if_control_statements_ends_group')
        self.case_control_statements_ends_group = 'no'
        self.configuration.append('case_control_statements_ends_group')


    def analyze(self, oFile):
        self.compact_alignment = utils.convert_yes_no_option_to_boolean(self.compact_alignment)
        self.blank_line_ends_group = utils.convert_yes_no_option_to_boolean(self.blank_line_ends_group)
        self.comment_line_ends_group = utils.convert_yes_no_option_to_boolean(self.comment_line_ends_group)
        self.if_control_statements_ends_group = utils.convert_yes_no_option_to_boolean(self.if_control_statements_ends_group)
        self.case_control_statements_ends_group = utils.convert_yes_no_option_to_boolean(self.case_control_statements_ends_group)

        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = oFile.get_tokens_bounded_by_token_when_between_tokens(self.left_token, self.right_token, self.lBetween[0], self.lBetween[1])
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            bSkip = False
            oEndSkipToken = None
            dAnalysis = {}

            for iIndex in range(0, len(lTokens)):
               iToken += 1
               oToken = lTokens[iIndex]

               bSkip, oEndSkipToken = alignment_utils.check_for_exclusions(oToken, bSkip, oEndSkipToken, self.lUnless)

               if not bTokenFound and not bSkip:
                   for oSearch in self.lTokens:
                       if isinstance(oToken, oSearch):
                           bTokenFound = True
                           dAnalysis[iLine] = {}
                           dAnalysis[iLine]['token_column'] = iColumn
                           dAnalysis[iLine]['token_index'] = iToken
                           dAnalysis[iLine]['line_number'] = iLine
                           dAnalysis[iLine]['token_value'] = oToken.get_value()
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
                           alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}
                   if self.blank_line_ends_group:
                       if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                           alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if self.if_control_statements_ends_group:
                       if alignment_utils.check_for_if_keywords(iIndex + 1, lTokens):
                           alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}

                   if self.case_control_statements_ends_group:
                       if alignment_utils.check_for_case_keywords(iIndex + 1, lTokens):
                           alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

                           for iKey in list(dAnalysis.keys()):
                               if dAnalysis[iKey]['adjust'] != 0:
                                   oLineTokens = oFile.get_tokens_from_line(iKey)
                                   sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                                   oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                                   oViolation.set_action(dAnalysis[iKey])
                                   self.add_violation(oViolation)

                           dAnalysis = {}



            alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)


            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oFile.get_tokens_from_line(iKey)
                    sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
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
