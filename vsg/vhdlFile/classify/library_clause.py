# -*- coding: utf-8 -*-

from vsg.token import library_clause as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import logical_name_list


def detect(oDesignFile):
    """
    library_clause ::=
        library logic_name_list ;
    """
    if oDesignFile.is_next_token("library"):
        return classify(oDesignFile)
    return False

#    if utils.is_next_token("library", iToken, lObjects):
#        iCurrent = classify(iToken, lObjects)
#        return iCurrent
#    return iToken


def classify(oDesignFile):
    utils.assign_next_token_required("library", token.keyword, oDesignFile)

    logical_name_list.classify_until([";"], oDesignFile)

    utils.assign_next_token_required(";", token.semicolon, oDesignFile)

    return True
