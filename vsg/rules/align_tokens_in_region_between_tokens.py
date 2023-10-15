
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import alignment_utils
from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class align_tokens_in_region_between_tokens(alignment.Rule):
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
    '''

    def __init__(self, name, identifier, lTokens, left_token, right_token, bIndexes=False):
        alignment.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.bIndexes = bIndexes
        ## Stuff below is from original keyword_alignment_rule

        self.compact_alignment = 'yes'
        self.configuration.append('compact_alignment')
        self.blank_line_ends_group = 'yes'
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = 'yes'
        self.configuration.append('comment_line_ends_group')
        self.separate_generic_port_alignment = 'yes'
        self.configuration.append('separate_generic_port_alignment')

        self.generate_statement_ends_group = 'no'
        self.bIncludeTillBeginningOfLine = False
        self.configuration_documentation_link = 'configuring_keyword_alignment_rules_link'

    def analyze(self, oFile):
        self.compact_alignment = utils.convert_yes_no_option_to_boolean(self.compact_alignment)
        self.blank_line_ends_group = utils.convert_yes_no_option_to_boolean(self.blank_line_ends_group)
        self.comment_line_ends_group = utils.convert_yes_no_option_to_boolean(self.comment_line_ends_group)
        self.separate_generic_port_alignment = utils.convert_yes_no_option_to_boolean(self.separate_generic_port_alignment)
        self.generate_statement_ends_group = utils.convert_yes_no_option_to_boolean(self.generate_statement_ends_group)

        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token, bIncludeTillBeginningOfLine=self.bIncludeTillBeginningOfLine)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            dAnalysis = {}

            if rules_utils.number_of_carriage_returns(lTokens) == 0:
                continue

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
                           dAnalysis[iLine]['token_value'] = oToken.get_value()
                           if isinstance(lTokens[iIndex -1], parser.whitespace):
                               dAnalysis[iLine]['left_column'] = iColumn - len(lTokens[iIndex - 1].get_value())
                           else:
                               dAnalysis[iLine]['left_column'] = iColumn
                           break

                   iColumn += alignment_utils.update_column_width(self, oToken)

               if isinstance(oToken, token.generic_clause.semicolon) and self.separate_generic_port_alignment:
                   alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                   for iKey in list(dAnalysis.keys()):
                       if dAnalysis[iKey]['adjust'] != 0:
                           oLineTokens = oFile.get_tokens_from_line(iKey)
                           sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                           oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                           oViolation.set_action(dAnalysis[iKey])
                           self.add_violation(oViolation)

                   dAnalysis = {}

               if isinstance(oToken, token.generic_map_aspect.close_parenthesis) and self.separate_generic_port_alignment:
                   alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                   for iKey in list(dAnalysis.keys()):
                       if dAnalysis[iKey]['adjust'] != 0:
                           oLineTokens = oFile.get_tokens_from_line(iKey)
                           sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                           oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                           oViolation.set_action(dAnalysis[iKey])
                           self.add_violation(oViolation)

                   dAnalysis = {}

               if generate_statement_detected(self, oToken):
                   alignment_utils.add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)
                   for iKey in list(dAnalysis.keys()):
                       if dAnalysis[iKey]['adjust'] != 0:
                           oLineTokens = oFile.get_tokens_from_line(iKey)
                           sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                           oViolation = violation.New(oLineTokens.get_line_number(), oLineTokens, sSolution)
                           oViolation.set_action(dAnalysis[iKey])
                           self.add_violation(oViolation)

                   dAnalysis = {}

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


def generate_statement_detected(self, oToken):
    if not self.generate_statement_ends_group:
        return False
    if generate_label_detected(oToken):
        return True
    if generate_semicolon_detected(oToken):
        return True
    if case_generate_alternative_detected(oToken):
        return True
    return False


def generate_label_detected(oToken):
    if isinstance(oToken, token.if_generate_statement.generate_label):
        return True
    if isinstance(oToken, token.for_generate_statement.generate_label):
        return True
    return False


def generate_semicolon_detected(oToken):
    if isinstance(oToken, token.if_generate_statement.semicolon):
        return True
    if isinstance(oToken, token.for_generate_statement.semicolon):
        return True
    if isinstance(oToken, token.case_generate_statement.semicolon):
        return True
    return False


def case_generate_alternative_detected(oToken):
    if isinstance(oToken, token.case_generate_alternative.when_keyword):
        return True
    return False
