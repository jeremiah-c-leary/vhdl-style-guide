# -*- coding: utf-8 -*-

from vsg.token import package_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import package_declarative_part, package_header


def detect(oDataStructure):
    """
    package_declaration ::=
        package identifier is
            package_header
            package_declarative_part
        end [ package ] [ package_simple_name ] ;
    """

    if oDataStructure.is_next_token("package"):
        if not oDataStructure.find_in_next_n_tokens("body", 5):
            if not oDataStructure.find_in_next_n_tokens("new", 5):
                classify(oDataStructure)
                return True
    return False


def classify(iToken, lObjects):
    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = package_header.detect(iCurrent, lObjects)

    iCurrent = package_declarative_part.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("package", token.package_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("is", token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("end", token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("package", token.end_package_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if_not(";", token.end_package_simple_name, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iToken, lObjects)

    return iCurrent
