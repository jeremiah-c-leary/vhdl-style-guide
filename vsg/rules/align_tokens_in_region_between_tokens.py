# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import alignment
from vsg.rules import alignment_utils, utils as rules_utils
from vsg.vhdlFile import utils


class align_tokens_in_region_between_tokens(alignment.Rule):
    """
    Aligns tokens in a region.

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
    """

    def __init__(self, lTokens, left_token, right_token):
        super().__init__()
        self.lTokens = lTokens
        self.left_token = left_token
        self.right_token = right_token
        self.lUnless = []
        ## attributes below are configurable by the user

        self.compact_alignment = "yes"
        self.configuration.append("compact_alignment")
        self.blank_line_ends_group = "yes"
        self.configuration.append("blank_line_ends_group")
        self.comment_line_ends_group = "yes"
        self.configuration.append("comment_line_ends_group")
        self.separate_generic_port_alignment = "yes"
        self.configuration.append("separate_generic_port_alignment")

        self.if_control_statements_ends_group = "no"
        self.configuration.append("if_control_statements_ends_group")
        self.case_control_statements_ends_group = "no"
        self.configuration.append("case_control_statements_ends_group")
        self.loop_control_statements_ends_group = "no"
        self.configuration.append("loop_control_statements_ends_group")
        self.generate_statement_ends_group = "no"
        self.bIncludeTillBeginningOfLine = False
        self.aggregate_parens_ends_group = "no"
        self.ignore_single_line_aggregates = "no"
        self.configuration_documentation_link = "configuring_keyword_alignment_rules_link"

        self.include_type_is_keyword = "no"

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.left_token, self.right_token, bIncludeTillBeginningOfLine=self.bIncludeTillBeginningOfLine)

    def analyze(self, oFile):
        self.compact_alignment = utils.convert_yes_no_option_to_boolean(self.compact_alignment)
        self.blank_line_ends_group = utils.convert_yes_no_option_to_boolean(self.blank_line_ends_group)
        self.comment_line_ends_group = utils.convert_yes_no_option_to_boolean(self.comment_line_ends_group)
        self.if_control_statements_ends_group = utils.convert_yes_no_option_to_boolean(self.if_control_statements_ends_group)
        self.case_control_statements_ends_group = utils.convert_yes_no_option_to_boolean(self.case_control_statements_ends_group)
        self.loop_control_statements_ends_group = utils.convert_yes_no_option_to_boolean(self.loop_control_statements_ends_group)
        self.separate_generic_port_alignment = utils.convert_yes_no_option_to_boolean(self.separate_generic_port_alignment)
        self.generate_statement_ends_group = utils.convert_yes_no_option_to_boolean(self.generate_statement_ends_group)
        self.aggregate_parens_ends_group = utils.convert_yes_no_option_to_boolean(self.aggregate_parens_ends_group)
        self.ignore_single_line_aggregates = utils.convert_yes_no_option_to_boolean(self.ignore_single_line_aggregates)
        self.include_type_is_keyword = utils.convert_yes_no_option_to_boolean(self.include_type_is_keyword)

        lSearchTokens = []
        lSearchTokens.extend(self.lTokens)

        if self.include_type_is_keyword:
            lSearchTokens.append(self.is_keyword)

        lToi = self._get_tokens_of_interest(oFile)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            iColumn = 0
            bTokenFound = False
            iToken = -1
            bSkip = False
            oEndSkipToken = None
            dAnalysis = {}
            iIndex = 0

            if rules_utils.number_of_carriage_returns(lTokens) == 0:
                continue

            while iIndex < len(lTokens):
                iToken += 1
                oToken = lTokens[iIndex]

                bSkip, oEndSkipToken = alignment_utils.check_for_exclusions(oToken, bSkip, oEndSkipToken, self.lUnless)

                if not bTokenFound and not bSkip:
                    for oSearch in lSearchTokens:
                        if isinstance(oToken, oSearch):
                            bTokenFound = True
                            dAnalysis[iLine] = {}
                            dAnalysis[iLine]["token_column"] = iColumn
                            dAnalysis[iLine]["token_index"] = iToken
                            dAnalysis[iLine]["line_number"] = iLine
                            dAnalysis[iLine]["token_value"] = oToken.get_value()
                            if isinstance(lTokens[iIndex - 1], parser.whitespace):
                                dAnalysis[iLine]["left_column"] = iColumn - len(lTokens[iIndex - 1].get_value())
                            else:
                                dAnalysis[iLine]["left_column"] = iColumn
                            break

                    iColumn += alignment_utils.update_column_width(self, oToken)

                if isinstance(oToken, token.generic_clause.semicolon) and self.separate_generic_port_alignment:
                    alignment_utils.check_for_violations(self, dAnalysis, oFile)
                    dAnalysis = {}

                if isinstance(oToken, token.generic_map_aspect.close_parenthesis) and self.separate_generic_port_alignment:
                    alignment_utils.check_for_violations(self, dAnalysis, oFile)
                    dAnalysis = {}

                if alignment_utils.generate_statement_detected(self, oToken):
                    alignment_utils.check_for_violations(self, dAnalysis, oFile)
                    dAnalysis = {}

                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                    iColumn = 0
                    bTokenFound = False
                    iToken = -1
                    if self.comment_line_ends_group:
                        if utils.are_next_consecutive_token_types(
                            [parser.whitespace, parser.comment],
                            iIndex + 1,
                            lTokens,
                        ) or utils.are_next_consecutive_token_types([parser.comment], iIndex + 1, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                    if self.blank_line_ends_group:
                        if utils.are_next_consecutive_token_types([parser.blank_line], iIndex + 1, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                    if self.if_control_statements_ends_group:
                        if alignment_utils.check_for_if_keywords(iIndex + 1, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                    if alignment_utils.is_case_control_enabled(self.case_control_statements_ends_group):
                        if alignment_utils.is_case_keyword(self.case_control_statements_ends_group, iIndex, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                    if self.loop_control_statements_ends_group:
                        if alignment_utils.check_for_loop_keywords(iIndex + 1, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                elif self.ignore_single_line_aggregates and alignment_utils.is_single_line_aggregate(iIndex, lTokens):
                    iIndex = rules_utils.get_index_of_matching_close_paren(iIndex, lTokens)
                elif self.aggregate_parens_ends_group:
                    if alignment_utils.check_for_aggregate_parens(iIndex, lTokens):
                        if not self.ignore_single_line_aggregates or not alignment_utils.is_single_line_aggregate(iToken, lTokens):
                            alignment_utils.check_for_violations(self, dAnalysis, oFile)
                            dAnalysis = {}

                iIndex += 1

            alignment_utils.check_for_violations(self, dAnalysis, oFile)
            dAnalysis = {}

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        iTokenIndex = dAction["token_index"]

        if isinstance(lTokens[iTokenIndex - 1], parser.whitespace):
            iLen = len(lTokens[iTokenIndex - 1].get_value())
            lTokens[iTokenIndex - 1].set_value(" " * (iLen + dAction["adjust"]))
        else:
            rules_utils.insert_whitespace(lTokens, iTokenIndex, dAction["adjust"])
        oViolation.set_tokens(lTokens)
