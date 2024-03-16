# -*- coding: utf-8 -*-

from vsg.token import architecture_body as token
from vsg.vhdlFile.extract.get_tokens_bounded_by import get_tokens_bounded_by

oStart = token.is_keyword
oEnd = token.begin_keyword


def extract(lAllTokens, oTokenMap):
    return get_tokens_bounded_by(oStart, oEnd, lAllTokens, oTokenMap)
