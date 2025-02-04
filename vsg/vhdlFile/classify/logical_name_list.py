# -*- coding: utf-8 -*-

from vsg.token import logical_name_list as token
from vsg.vhdlFile import utils


def classify_until(lUntils, oDesignFile):
    """
    logical_name_list ::=
        logical_name { , logical_name }
    """
    while not oDesignFile.is_next_token_one_of(lUntils):
        oDesignFile.replace_next_token_with(token.logical_name)
        oDesignFile.replace_next_token_with_if(",", token.comma)
