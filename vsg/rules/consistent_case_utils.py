# -*- coding: utf-8 -*-

from vsg import token
from vsg.vhdlFile.extract import tokens


def add_identifiers_from_to(sType1, sType2, lAllDicts):
    lReturn = []
    for dDict in lAllDicts:
        if not dDict["type"] == sType2:
            lReturn.append(dDict)
            continue
        for dDict2 in lAllDicts:
            if dDict2["type"] == sType1:
                if dDict2["keyword"] < dDict["keyword"] < dDict2["end"]:
                    dDict["identifiers"].extend(dDict2["identifiers"])
        lReturn.append(dDict)
    return lReturn


def add_entity_identifiers_to_architecture_body(lAllDicts):
    lReturn = []
    sType1 = "entity_declaration"
    sType2 = "architecture_body"
    for dArch in lAllDicts:
        if not type_matches(dArch, sType2):
            lReturn.append(dArch)
            continue
        for dEntity in lAllDicts:
            if type_matches(dEntity, sType1):
                if dEntity["identifier"] == dArch["identifier"]:
                    try:
                        dArch["identifiers"].extend(dEntity["identifiers"])
                    except KeyError:
                        dArch["identifiers"] = dEntity["identifiers"]

        lReturn.append(dArch)
    return lReturn


def type_matches(dDict, sType):
    if dDict["type"] == sType:
        return True
    return False


def remove_duplicate_names(sType1, sType2, lAllDicts):
    return remove_duplicate_numbers(sType1, sType2, "names", lAllDicts)


def remove_duplicate_identifiers(sType1, sType2, lAllDicts):
    return remove_duplicate_numbers(sType1, sType2, "identifiers", lAllDicts)


def remove_duplicate_numbers(sType1, sType2, sKey, lAllDicts):
    lReturn = []
    for dDict in lAllDicts:
        if not dDict["type"] == sType1:
            lReturn.append(dDict)
            continue
        for dDict2 in lAllDicts:
            if dDict2["type"] == sType2:
                for iNum in dDict2[sKey]:
                    if iNum in dDict[sKey]:
                        dDict[sKey].remove(iNum)
        lReturn.append(dDict)
    return lReturn


def populate_identifiers(lAllDicts, lIdentifiers):
    lReturn = []
    for dDict in lAllDicts:
        lId = []
        for iIdentifier in lIdentifiers:
            if dDict["keyword"] < iIdentifier < dDict["begin"]:
                lId.append(iIdentifier)
        dDict["identifiers"] = lId
        lReturn.append(dDict)
    return lReturn


def populate_statement_part_names(lAllDicts, lNames):
    lReturn = []
    for dDict in lAllDicts:
        lId = []
        for iName in lNames:
            if dDict["begin"] < iName < dDict["end"]:
                lId.append(iName)
        try:
            dDict["names"].extend(lId)
        except KeyError:
            dDict["names"] = lId
        lReturn.append(dDict)
    return lReturn


def populate_declarative_part_names(lAllDicts, lNames):
    lReturn = []
    for dDict in lAllDicts:
        lId = []
        for iName in lNames:
            if dDict["keyword"] < iName < dDict["begin"]:
                lId.append(iName)
        dDict["names"] = lId
        lReturn.append(dDict)
    return lReturn


def create_tois(lAllDicts, oFile):
    lReturn = []
    oTokenMap = oFile.get_token_map()
    for dDict in lAllDicts:
        for iName in dDict["names"]:
            try:
                for iIdentifier in dDict["identifiers"]:
                    iLine = oTokenMap.get_line_number_of_index(iName)
                    sName = oFile.lAllObjects[iName].get_value()
                    sIdentifier = oFile.lAllObjects[iIdentifier].get_value()
                    if sIdentifier.lower() == sName.lower():
                        if not sIdentifier == sName:
                            oToi = tokens.New(iName, iLine, [oFile.lAllObjects[iName]])
                            oToi.set_meta_data("expected", sIdentifier)
                            lReturn.append(oToi)
                        break
            except KeyError:
                pass

    return lReturn


def merge_dict_lists(lOne, lTwo):
    lReturn = []
    lReturn.extend(lOne)
    lReturn.extend(lTwo)
    return lReturn


def get_all_name_tokens(oFile, lNames):
    lReturn = []
    oTokenMap = oFile.get_token_map()
    for oToken in lNames:
        lReturn.extend(oTokenMap.get_token_indexes(oToken))
    lReturn.sort()
    return lReturn


def get_all_identifiers(oFile, lTokens):
    lReturn = []
    for oToken in lTokens:
        lReturn.extend(get_indexes_of_token(oFile, oToken))
    return lReturn


def get_architecture_indexes(oFile):
    lKeywords = get_all_architecture_keywords(oFile)
    lIdentifier = get_all_architecture_entity_names(oFile)
    lBegin = get_all_architecture_begin_keywords(oFile)
    lEnd = get_all_architecture_end_keywords(oFile)

    return merge_four_indexes_into_list(lKeywords, lIdentifier, lBegin, lEnd, "architecture_body")


def get_process_indexes(oFile):
    lKeywords = get_all_process_keywords(oFile)
    lBegin = get_all_process_begin_keywords(oFile)
    lEnd = get_all_process_end_keywords(oFile)

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, "process")


def get_subprogram_body_indexes(oFile):
    lKeywords = get_all_subprogram_body_is_keywords(oFile)
    lBegin = get_all_subprogram_body_begin_keywords(oFile)
    lEnd = get_all_subprogram_body_end_keywords(oFile)

    return merge_block_indexes_into_list(lKeywords, lBegin, lEnd, "subprogram_body")


def get_block_indexes(oFile):
    lKeywords = get_all_block_keywords(oFile)
    lBegin = get_all_block_begin_keywords(oFile)
    lEnd = get_all_block_end_keywords(oFile)

    lIndexes = merge_block_indexes_into_list(lKeywords, lBegin, lEnd, "block_statement")

    return lIndexes


def get_component_declaration_indexes(oFile):
    lKeywords = get_all_component_keywords(oFile)
    lBegin = lKeywords
    lEnd = get_all_component_end_keywords(oFile)

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, "component_declaration")


def get_entity_declaration_indexes(oFile):
    lKeywords = get_all_entity_keywords(oFile)
    lIdentifiers = get_all_entity_identifiers(oFile)
    lBegin = get_all_entity_end_keywords(oFile)
    lEnd = lBegin

    return merge_four_indexes_into_list(lKeywords, lIdentifiers, lBegin, lEnd, "entity_declaration")


def get_generic_clause_indexes(oFile):
    lKeywords = get_all_generic_clause_keywords(oFile)
    lBegin = get_all_generic_clause_end_keywords(oFile)
    lEnd = lBegin

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, "generic_clause")


def get_port_clause_indexes(oFile):
    lKeywords = get_all_port_clause_keywords(oFile)
    lBegin = get_all_port_clause_end_keywords(oFile)
    lEnd = lBegin

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, "port_clause")


def merge_block_indexes_into_list(lFirst, lSecond, lThird, sType):
    lInnerIndexes = get_inner_indexes(lSecond, lThird)
    lTemps = get_inner_indexes(lFirst, lSecond)

    lCombined = []
    for lTemp in lTemps:
        for lInnerIndex in lInnerIndexes:
            if lTemp[1] == lInnerIndex[0]:
                lCombined.append([lTemp[0], lInnerIndex[0], lInnerIndex[1]])

    lReturn = []
    for lTemp in lCombined:
        dProc = {}
        dProc["type"] = sType
        dProc["keyword"] = lTemp[0]
        dProc["begin"] = lTemp[1]
        dProc["end"] = lTemp[2]
        lReturn.append(dProc)
    return lReturn


def get_inner_indexes(lFirst, lSecond):
    lReturn = []
    lMyFirst = lFirst.copy()
    lMySecond = lSecond.copy()
    while len(lMyFirst) > 0:
        dDelta = {}
        lTemp = []
        for iFirst in lMyFirst:
            for iSecond in lMySecond:
                iDelta = iSecond - iFirst
                if iDelta > 0:
                    dDelta[iDelta] = [iFirst, iSecond]

        lKeys = list(dDelta.keys())
        lKeys.sort()
        lReturn.append(dDelta[lKeys[0]])
        lMyFirst.remove(dDelta[lKeys[0]][0])
        lMySecond.remove(dDelta[lKeys[0]][1])

    return lReturn


def merge_three_indexes_into_list(lFirst, lSecond, lThird, sType):
    lReturn = []
    for i in range(0, len(lFirst)):
        dProc = {}
        dProc["type"] = sType
        dProc["keyword"] = lFirst[i]
        dProc["begin"] = lSecond[i]
        dProc["end"] = lThird[i]
        lReturn.append(dProc)
    return lReturn


def merge_four_indexes_into_list(lFirst, lSecond, lThird, lFourth, sType):
    lReturn = []
    for i in range(0, len(lFirst)):
        dProc = {}
        dProc["type"] = sType
        dProc["keyword"] = lFirst[i]
        dProc["identifier"] = lSecond[i]
        dProc["begin"] = lThird[i]
        dProc["end"] = lFourth[i]
        lReturn.append(dProc)
    return lReturn


def get_all_process_keywords(oFile):
    return get_indexes_of_token(oFile, token.process_statement.process_keyword)


def get_all_process_begin_keywords(oFile):
    return get_indexes_of_token(oFile, token.process_statement.begin_keyword)


def get_all_process_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.process_statement.end_keyword)


def get_all_architecture_keywords(oFile):
    return get_indexes_of_token(oFile, token.architecture_body.architecture_keyword)


def get_all_architecture_entity_names(oFile):
    lReturn = []
    lIndexes = get_indexes_of_token(oFile, token.architecture_body.entity_name)
    for iIndex in lIndexes:
        lReturn.append(oFile.lAllObjects[iIndex].get_value().lower())
    return lReturn


def get_all_architecture_begin_keywords(oFile):
    return get_indexes_of_token(oFile, token.architecture_body.begin_keyword)


def get_all_architecture_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.architecture_body.end_keyword)


def get_all_subprogram_body_is_keywords(oFile):
    return get_indexes_of_token(oFile, token.subprogram_body.is_keyword)


def get_all_subprogram_body_begin_keywords(oFile):
    return get_indexes_of_token(oFile, token.subprogram_body.begin_keyword)


def get_all_subprogram_body_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.subprogram_body.end_keyword)


def get_all_block_keywords(oFile):
    return get_indexes_of_token(oFile, token.block_statement.block_keyword)


def get_all_block_begin_keywords(oFile):
    return get_indexes_of_token(oFile, token.block_statement.begin_keyword)


def get_all_block_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.block_statement.end_keyword)


def get_all_component_keywords(oFile):
    return get_indexes_of_token(oFile, token.component_declaration.component_keyword)


def get_all_component_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.component_declaration.end_keyword)


def get_all_entity_keywords(oFile):
    return get_indexes_of_token(oFile, token.entity_declaration.entity_keyword)


def get_all_entity_identifiers(oFile):
    lReturn = []
    lIndexes = get_indexes_of_token(oFile, token.entity_declaration.identifier)
    for iIndex in lIndexes:
        lReturn.append(oFile.lAllObjects[iIndex].get_value().lower())
    return lReturn


def get_all_entity_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.entity_declaration.end_keyword)


def get_all_generic_clause_keywords(oFile):
    return get_indexes_of_token(oFile, token.generic_clause.generic_keyword)


def get_all_generic_clause_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.generic_clause.semicolon)


def get_all_port_clause_keywords(oFile):
    return get_indexes_of_token(oFile, token.port_clause.port_keyword)


def get_all_port_clause_end_keywords(oFile):
    return get_indexes_of_token(oFile, token.port_clause.semicolon)


def get_indexes_of_token(oFile, oToken):
    oTokenMap = oFile.get_token_map()
    return oTokenMap.get_token_indexes(oToken)


def remove_type(sKey, lAllDicts):
    lReturn = []
    for dDict in lAllDicts:
        if dDict["type"] == sKey:
            continue
        lReturn.append(dDict)
    return lReturn
