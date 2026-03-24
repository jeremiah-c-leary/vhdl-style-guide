# -*- coding: utf-8 -*-

import math
import string

from vsg import exceptions, parser
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils

HEADER_FIELDS = [
    "header_left",
    "header_left_repeat",
    "header_string",
    "header_right_repeat",
    "header_alignment",
    "max_header_column",
]

BODY_FIELDS = [
    "comment_left",
]

FOOTER_FIELDS = [
    "footer_left",
    "footer_left_repeat",
    "footer_string",
    "footer_right_repeat",
    "footer_alignment",
    "max_footer_column",
]

ALL_STYLE_FIELDS = HEADER_FIELDS + BODY_FIELDS + FOOTER_FIELDS

RULE_FIELD_MAP = {
    "block_comment_001": HEADER_FIELDS,
    "block_comment_002": BODY_FIELDS,
    "block_comment_003": FOOTER_FIELDS,
}


class Rule(structure.Rule):
    def __init__(self):
        super().__init__()
        self.fixable = False
        self.disable = True

        self.min_height = 3
        self.configuration.append("min_height")
        self.allow_indenting = "yes"
        self.configuration.append("allow_indenting")
        self.configuration_documentation_link = "configuring_block_comments_link"

        # Shared block comment style attributes.
        # Concrete rules expose only their own configuration keys, but the base
        # class owns the full style set so it can validate the family counts
        # and select one consistent style for the entire block.
        self.header_left = None
        self.header_left_repeat = "-"
        self.header_string = None
        self.header_right_repeat = None
        self.header_alignment = "center"
        self.max_header_column = 120

        self.comment_left = None

        self.footer_left = None
        self.footer_left_repeat = "-"
        self.footer_string = None
        self.footer_right_repeat = None
        self.footer_alignment = "center"
        self.max_footer_column = 120

        self._block_comment_style_count = 1

    def configure(self, oConfig):
        lReturn = super().configure(oConfig)
        self._synchronize_block_comment_style_attributes(oConfig)
        self._block_comment_style_count = self._validate_and_get_style_count()
        return lReturn

    def analyze(self, oFile):
        self.allow_indenting = utils.convert_yes_no_option_to_boolean(self.allow_indenting)
        super().analyze(oFile)

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_consecutive_lines_starting_with_token(parser.comment, self.min_height)
        lReturn = []
        for oToi in lToi:
            iLeft, iLines, iRight = adjust_for_code_tags(oToi)
            if iLines >= self.min_height:
                lReturn.append(oToi.extract_tokens(iLeft, iRight))
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            if not first_comment_is_a_header(oToi):
                continue

            self.analyze_comments(oToi)

    def fix(self, oFile, dFixOnly=None):
        """
        Applies fixes for any rule violations.
        """
        super().fix(oFile, dFixOnly)

    def set_token_indent(self, oToken):
        oToken.is_block_comment = True
        if not self.allow_indenting:
            oToken.set_indent(0)
            oToken.block_comment_indent = 0

    def calculate_leading_whitespace(self, oToken):
        if self.allow_indenting:
            iWhitespace = self.indent_size * oToken.get_indent()
        else:
            iWhitespace = 0
        return iWhitespace

    def get_style_count(self):
        return self._block_comment_style_count

    def get_style(self, iIndex):
        if iIndex < 0 or iIndex >= self.get_style_count():
            raise IndexError("Style index out of range: {0}".format(iIndex))

        dStyle = {}
        for sField in ALL_STYLE_FIELDS:
            dStyle[sField] = get_style_value_at_index(getattr(self, sField), iIndex)
        return dStyle

    def get_styles(self):
        return [self.get_style(iIndex) for iIndex in range(self.get_style_count())]

    def build_header(self, oToken, dStyle=None):
        if dStyle is None:
            dStyle = self.get_style(0)

        iWhitespace = self.calculate_leading_whitespace(oToken)

        sHeader = "--"

        sHeaderLeft = dStyle["header_left"]
        sHeaderLeftRepeat = dStyle["header_left_repeat"] or ""
        sHeaderString = dStyle["header_string"]
        sHeaderRightRepeat = dStyle["header_right_repeat"] or ""
        sHeaderAlignment = dStyle["header_alignment"]
        iMaxHeaderColumn = dStyle["max_header_column"]

        if sHeaderLeft is not None:
            sHeader += sHeaderLeft
            iHeaderLeft = len(sHeaderLeft)
        else:
            iHeaderLeft = 0

        if sHeaderString is None:
            sHeader += sHeaderLeftRepeat * (iMaxHeaderColumn - iWhitespace - len(sHeader))
        elif sHeaderAlignment == "center":
            iLeft = math.floor((iMaxHeaderColumn - iWhitespace - len(sHeaderString)) / 2) - iHeaderLeft - 2
            sLeft = sHeaderLeftRepeat * iLeft
            iRight = iMaxHeaderColumn - iWhitespace - 2 - iHeaderLeft - len(sHeaderString) - iLeft
            sRight = sHeaderRightRepeat * iRight
            sHeader += sLeft + sHeaderString + sRight
        elif sHeaderAlignment == "left":
            sHeader += sHeaderLeftRepeat
            sHeader += sHeaderString
            iLength = iMaxHeaderColumn - iWhitespace - len(sHeader)
            sHeader += sHeaderRightRepeat * iLength
        elif sHeaderAlignment == "right":
            iLength = iMaxHeaderColumn - iWhitespace - len(sHeader) - len(sHeaderString) - 1
            sHeader += sHeaderLeftRepeat * iLength
            sHeader += sHeaderString
            sHeader += sHeaderRightRepeat

        return sHeader

    def build_footer(self, oToken, dStyle=None):
        if dStyle is None:
            dStyle = self.get_style(0)

        iWhitespace = self.calculate_leading_whitespace(oToken)
        sFooter = "--"

        sFooterLeft = dStyle["footer_left"]
        sFooterLeftRepeat = dStyle["footer_left_repeat"] or ""
        sFooterString = dStyle["footer_string"]
        sFooterRightRepeat = dStyle["footer_right_repeat"] or ""
        sFooterAlignment = dStyle["footer_alignment"]
        iMaxFooterColumn = dStyle["max_footer_column"]

        if sFooterLeft is not None:
            sFooter += sFooterLeft
            iFooterLeft = len(sFooterLeft)
        else:
            iFooterLeft = 0

        if sFooterString is None:
            sFooter += sFooterLeftRepeat * (iMaxFooterColumn - iWhitespace - len(sFooter))
        elif sFooterAlignment == "center":
            iLength = int((iMaxFooterColumn - iWhitespace - len(sFooterString)) / 2) - iFooterLeft - 2
            sFooter += sFooterLeftRepeat * iLength
            sFooter += sFooterString
            sFooter += sFooterRightRepeat * (iMaxFooterColumn - iWhitespace - len(sFooter))
        elif sFooterAlignment == "left":
            sFooter += sFooterLeftRepeat
            sFooter += sFooterString
            sFooter += sFooterRightRepeat * (iMaxFooterColumn - iWhitespace - len(sFooter))
        elif sFooterAlignment == "right":
            iLength = iMaxFooterColumn - iWhitespace - len(sFooter) - len(sFooterString) - 1
            sFooter += sFooterLeftRepeat * iLength
            sFooter += sFooterString
            sFooter += sFooterRightRepeat

        return sFooter

    def build_comment(self, oToken=None, dStyle=None):
        if dStyle is None:
            dStyle = self.get_style(0)

        sComment = "--"
        if dStyle["comment_left"] is not None:
            sComment += dStyle["comment_left"]
        return sComment

    def matching_style_indexes(self, oToi):
        lComments = get_comment_tokens(oToi)
        if len(lComments) < 2:
            return []

        lMatches = []

        for iStyleIndex in range(self.get_style_count()):
            dStyle = self.get_style(iStyleIndex)

            if not self.header_matches(lComments[0], dStyle):
                continue

            bMiddleMatches = True
            for oToken in lComments[1:-1]:
                if not self.middle_matches(oToken, dStyle):
                    bMiddleMatches = False
                    break

            if not bMiddleMatches:
                continue

            if not self.footer_matches(lComments[-1], dStyle):
                continue

            lMatches.append(iStyleIndex)

        return lMatches

    def select_style_index(self, oToi):
        lMatches = self.matching_style_indexes(oToi)
        if lMatches:
            return lMatches[0]

        iBestIndex = 0
        iBestScore = -1

        for iStyleIndex in range(self.get_style_count()):
            dStyle = self.get_style(iStyleIndex)
            iScore = self.style_score(oToi, dStyle)
            if iScore > iBestScore:
                iBestScore = iScore
                iBestIndex = iStyleIndex

        return iBestIndex

    def style_score(self, oToi, dStyle):
        lComments = get_comment_tokens(oToi)
        if len(lComments) < 2:
            return -1

        iScore = 0

        if self.header_matches(lComments[0], dStyle):
            iScore += 1

        for oToken in lComments[1:-1]:
            if self.middle_matches(oToken, dStyle):
                iScore += 1

        if self.footer_matches(lComments[-1], dStyle):
            iScore += 1

        return iScore

    def header_matches(self, oToken, dStyle):
        sComment = oToken.get_value()

        try:
            if not is_header(sComment):
                return False
        except IndexError:
            return False

        return sComment == self.build_header(oToken, dStyle)

    def middle_matches(self, oToken, dStyle):
        if dStyle["comment_left"] is None:
            return True
        return oToken.get_value().startswith(self.build_comment(oToken, dStyle))

    def footer_matches(self, oToken, dStyle):
        sComment = oToken.get_value()
        if not is_footer(sComment):
            return False
        return sComment == self.build_footer(oToken, dStyle)

    def _synchronize_block_comment_style_attributes(self, oConfig):
        try:
            dRuleConfig = oConfig.dConfig["rule"]
        except (AttributeError, KeyError, TypeError):
            return

        for sRuleName, lFields in RULE_FIELD_MAP.items():
            try:
                dSource = dRuleConfig[sRuleName]
            except KeyError:
                continue

            for sField in lFields:
                if sField in dSource:
                    setattr(self, sField, dSource[sField])

    def _validate_and_get_style_count(self):
        dCounts = {
            "header": self._get_family_style_count(HEADER_FIELDS, "header"),
            "body": self._get_family_style_count(BODY_FIELDS, "body"),
            "footer": self._get_family_style_count(FOOTER_FIELDS, "footer"),
        }

        lUniqueCounts = sorted(set(dCounts.values()))
        if len(lUniqueCounts) != 1:
            raise exceptions.ConfigurationError(
                "Block comment style count mismatch: header={0}, body={1}, footer={2}. "
                "All three block_comment rules must define the same number of styles.".format(
                    dCounts["header"], dCounts["body"], dCounts["footer"]
                )
            )

        return lUniqueCounts[0]

    def _get_family_style_count(self, lFields, sFamilyName):
        iStyleCount = 1

        for sField in lFields:
            iLength = get_style_value_length(getattr(self, sField))
            if iLength != 1:
                if iStyleCount == 1:
                    iStyleCount = iLength
                elif iLength != iStyleCount:
                    raise exceptions.ConfigurationError(
                        "Block comment {0} configuration mismatch: field '{1}' has {2} entries, "
                        "expected 1 or {3}.".format(sFamilyName, sField, iLength, iStyleCount)
                    )

        return iStyleCount


def get_style_value_length(oValue):
    if isinstance(oValue, (list, tuple)):
        return len(oValue)
    return 1


def get_style_value_at_index(oValue, iIndex):
    if isinstance(oValue, (list, tuple)):
        return oValue[iIndex]
    return oValue


def get_comment_tokens(oToi):
    return [oToken for oToken in oToi.get_tokens() if isinstance(oToken, parser.comment)]


def is_header(sComment):
    if bare_comment(sComment):
        return False
    if not third_character_is_alphanumeric(sComment):
        return False
    return fourth_character_is_alphanumeric(sComment)


def fourth_character_is_alphanumeric(sComment):
    try:
        if sComment[3] not in string.punctuation:
            return False
    except IndexError:
        return True
    return True


def third_character_is_alphanumeric(sComment):
    if sComment[2] not in string.punctuation:
        return False
    if sComment[2] == "!":
        return False
    return True


def bare_comment(sString):
    if sString == "--":
        return True
    return False


def is_footer(sComment):
    return is_header(sComment)


def first_comment_is_a_header(oToi):
    oToken = oToi.get_first_token_matching(parser.comment)
    if is_header(oToken.get_value()):
        return True
    return False


def adjust_for_code_tags(oToi):
    lTokens = oToi.get_tokens()
    iLeft, iLines, iRight = extract_initial_indexes_from_token_list(lTokens)
    iLeft, iLines = adjust_indexes_for_code_tags_at_beginning_of_block_comment(lTokens, iLeft, iLines)
    iRight, iLines = adjust_indexes_for_code_tags_at_end_of_block_comment(lTokens, iRight, iLines)
    return iLeft, iLines, iRight


def extract_initial_indexes_from_token_list(lTokens):
    iLines = utils.count_carriage_returns(lTokens) + 1
    iLeft = 0
    iRight = len(lTokens)
    return iLeft, iLines, iRight


def adjust_indexes_for_code_tags_at_beginning_of_block_comment(lTokens, iLeft, iLines):
    if code_tag_detected(lTokens[0]):
        iLeft = 2
        iLines -= 1
    if code_tag_detected(lTokens[1]):
        iLeft = 3
        iLines -= 1
    return iLeft, iLines


def adjust_indexes_for_code_tags_at_end_of_block_comment(lTokens, iRight, iLines):
    if code_tag_detected(lTokens[-1]):
        if rules_utils.token_is_whitespace(lTokens[-2]):
            iRight = len(lTokens) - 4
        else:
            iRight = len(lTokens) - 3
        iLines -= 1
    return iRight, iLines


def code_tag_detected(oToken):
    if "vsg_on" in oToken.get_value() or "vsg_off" in oToken.get_value():
        return True
    return False
