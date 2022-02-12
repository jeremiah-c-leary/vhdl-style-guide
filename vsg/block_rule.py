
import string

from vsg import parser

from vsg.rule_group import structure


class Rule(structure.Rule):

    def __init__(self, name, identifier):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.fixable = False
        self.disable = True

        self.min_height = 3
        self.configuration.append('min_height')
        self.allow_indenting = True
        self.configuration.append('allow_indenting')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_consecutive_lines_starting_with_token(parser.comment, self.min_height)

    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        self.analyze(oFile)

    def set_token_indent(self, oToken):
        if self.allow_indenting:
            oToken.is_block_comment = False
        else:
            oToken.set_indent(0)
            oToken.is_block_comment = True
            oToken.block_comment_indent = 0

    def calculate_leading_whitespace(self, oToken):
        if self.allow_indenting:
            iWhitespace = self.indentSize * oToken.get_indent()
        else:
            iWhitespace = 0
        return iWhitespace

    def build_footer(self, oToken):
        iWhitespace = self.calculate_leading_whitespace(oToken)
        sFooter = '--'
        if self.footer_left is not None:
            sFooter += self.footer_left
            iFooter_left = len(self.footer_left)
        else:
            iFooter_left = 0

        if self.footer_string is None:
            sFooter += self.footer_left_repeat * (self.max_footer_column - iWhitespace - len(sFooter))
        elif self.footer_alignment == 'center':
            iLength = int((self.max_footer_column - iWhitespace - len(self.footer_string)) / 2) - iFooter_left - 2
            sFooter += self.footer_left_repeat * (iLength)
            sFooter += self.footer_string
            sFooter += self.footer_right_repeat * (self.max_footer_column - len(sFooter))
        elif self.footer_alignment == 'left':
            sFooter += self.footer_left_repeat
            sFooter += self.footer_string
            iLength = self.max_footer_column - iWhitespace - len(sFooter)
            sFooter += self.footer_right_repeat * (self.max_footer_column - len(sFooter))
        elif self.footer_alignment == 'right':
            iLength = self.max_footer_column - iWhitespace - len(sFooter) - len(self.footer_string) - 1
            sFooter += self.footer_left_repeat * (iLength)
            sFooter += self.footer_string
            sFooter += self.footer_right_repeat
        return sFooter

    def build_comment(self, oToken):
        sHeader = '--'
        sHeader += self.comment_left
        return sHeader


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
    if sComment[2] == '!':
        return False
    return True


def bare_comment(sString):
    if sString == '--':
        return True
    return False


def is_footer(sComment):
    return is_header(sComment)
