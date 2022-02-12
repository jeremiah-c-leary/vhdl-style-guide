
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
