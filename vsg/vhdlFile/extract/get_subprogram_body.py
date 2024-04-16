# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.vhdlFile.extract import tokens


def get_subprogram_body(lAllObjects, oTokenMap):
    dData = {}

    dData["subprogramDeclarationSemicolon"] = oTokenMap.get_token_indexes(token.subprogram_declaration.semicolon)
    dData["subprogramBodySemicolon"] = oTokenMap.get_token_indexes(token.subprogram_body.semicolon)
    dData["procedureSpecificationKeyword"] = oTokenMap.get_token_indexes(token.procedure_specification.procedure_keyword)
    dData["functionSpecificationKeyword"] = oTokenMap.get_token_indexes(token.function_specification.function_keyword)

    lPairs = extract_pairs(dData)

    lPairs = remove_subprogram_declarations(dData, lPairs)

    lPairs = sort_pairs(lPairs)

    lReturn = create_tokens_of_interest(lPairs, lAllObjects, oTokenMap)

    return lReturn


def extract_pairs(dData):
    lStartIndexes = merge_keywords(dData)
    lEndIndexes = merge_semicolons(dData)
    return extract_inner_pairs(lStartIndexes, lEndIndexes)


def merge_keywords(dData):
    return merge_keys(dData, "procedureSpecificationKeyword", "functionSpecificationKeyword")


def merge_semicolons(dData):
    return merge_keys(dData, "subprogramDeclarationSemicolon", "subprogramBodySemicolon")


def merge_keys(dData, sKey1, sKey2):
    lReturn = []
    lReturn.extend(dData[sKey1])
    lReturn.extend(dData[sKey2])
    lReturn.sort()

    return lReturn


def extract_inner_pairs(lStartIndexes, lEndIndexes):
    lReturn = []
    while len(lStartIndexes) > 0:
        pair, lStartIndexes, lEndIndexes = extract_inner_pair(lStartIndexes, lEndIndexes)
        lReturn.append(pair)

    return lReturn


def extract_inner_pair(lStartIndexes, lEndIndexes):
    dPairs = {}
    for iStart in lStartIndexes:
        dPairs[iStart] = {}
        for iEnd in lEndIndexes:
            if iEnd - iStart > 0:
                dPairs[iStart][iEnd] = iEnd - iStart

    iMinDelta = lEndIndexes[-1]
    for iStart in dPairs:
        for iEnd in dPairs[iStart]:
            if dPairs[iStart][iEnd] < iMinDelta:
                lPair = [iStart, iEnd]
                iMinDelta = dPairs[iStart][iEnd]

    lStartIndexes.remove(lPair[0])
    lEndIndexes.remove(lPair[1])
    return lPair, lStartIndexes, lEndIndexes


def remove_subprogram_declarations(dData, lPairs):
    lReturn = []
    for pair in lPairs:
        if not pair[1] in dData["subprogramDeclarationSemicolon"]:
            lReturn.append(pair)
    return lReturn


def sort_pairs(lPairs):
    lStartIndexes = []
    for pair in lPairs:
        lStartIndexes.append(pair[0])
    lStartIndexes.sort()

    lReturn = []
    for iIndex in lStartIndexes:
        for pair in lPairs:
            if iIndex == pair[0]:
                lReturn.append(pair)

    return lReturn


def create_tokens_of_interest(lPairs, lAllTokens, oTokenMap):
    lReturn = []
    for lPair in lPairs:
        iStart = lPair[0]
        iEnd = lPair[1]
        iLine = oTokenMap.get_line_number_of_index(iStart)
        lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart : iEnd + 1]))
    return lReturn
