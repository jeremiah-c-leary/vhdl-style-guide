
from vsg import violation

from vsg.vhdlFile import utils
from vsg.vhdlFile.extract import tokens
from vsg.rule_group import case

from vsg import parser
from vsg import token


class consistent_token_case(case.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens: list of token type objects
       token type to apply the case check against
    '''

    def __init__(self, name, identifier, lTokens, lNames, lIgnore=None):
        case.Rule.__init__(self, name=name, identifier=identifier)
        self.subphase = 2
        self.lTokens = lTokens
        self.lNames = lNames
        self.bIncludeDeclarativePartNames = False
        self.bIncludeArchitectureBodyDeclarationsInSubprogramBody = False
        if lIgnore == None:
            self.lIgnoreTokens = []
        else:
            self.lIgnoreTokens = lIgnore
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):

        lNameTokens = get_all_name_tokens(oFile, self.lNames)
#        print(f'lNames = {lNameTokens}')
#        for iName in lNameTokens:
#            print(f'{iName} = {oFile.lAllObjects[iName].get_value()}')

        Identifiers = get_all_identifiers(oFile, self.lTokens)
#        print(f'lVariables = {Identifiers}')

        lProcessDicts = get_process_indexes(oFile)
#        print(f'lProcessDicts = {lProcessDicts}')
#
        lArchitectureDicts = get_architecture_indexes(oFile)
#        print(f'lArchitectureDicts = {lArchitectureDicts}')
#
        lSubprogramBodyDicts = get_subprogram_body_indexes(oFile)
#        print(f'lSubprogramBodyDicts = {lSubprogramBodyDicts}')

        lBlockDicts = get_block_indexes(oFile)
#        print(f'lBlockDicts = {lBlockDicts}')

        lComponentDicts = get_component_declaration_indexes(oFile)

        lAllDicts = merge_dict_lists(lArchitectureDicts, lProcessDicts)
        lAllDicts = merge_dict_lists(lAllDicts, lSubprogramBodyDicts)
        lAllDicts = merge_dict_lists(lAllDicts, lBlockDicts)
        lAllDicts = merge_dict_lists(lAllDicts, lComponentDicts)

        lAllDicts = populate_identifiers(lAllDicts, Identifiers)
        if self.bIncludeDeclarativePartNames:
            lAllDicts = populate_declarative_part_names(lAllDicts, lNameTokens)
        lAllDicts = populate_statement_part_names(lAllDicts, lNameTokens)

        lAllDicts = remove_duplicate_identifiers('architecture_body', 'subprogram_body', lAllDicts)
        lAllDicts = remove_duplicate_names('architecture_body', 'subprogram_body', lAllDicts)

        lAllDicts = remove_duplicate_identifiers('architecture_body', 'process', lAllDicts)
        lAllDicts = remove_duplicate_names('architecture_body', 'process', lAllDicts)

        lAllDicts = remove_duplicate_names('architecture_body', 'component_declaration', lAllDicts)

        lAllDicts = remove_duplicate_identifiers('process', 'subprogram_body', lAllDicts)
        lAllDicts = remove_duplicate_names('process', 'subprogram_body', lAllDicts)

        lAllDicts = remove_duplicate_identifiers('block_statement', 'subprogram_body', lAllDicts)
        lAllDicts = remove_duplicate_names('block_statement', 'subprogram_body', lAllDicts)

        lAllDicts = remove_duplicate_identifiers('block_statement', 'process', lAllDicts)
        lAllDicts = remove_duplicate_names('block_statement', 'process', lAllDicts)

        lAllDicts = add_identifiers_from_to('block_statement', 'process', lAllDicts)
        lAllDicts = add_identifiers_from_to('architecture_body', 'process', lAllDicts)

        if self.bIncludeArchitectureBodyDeclarationsInSubprogramBody:
            lAllDicts = add_identifiers_from_to('architecture_body', 'subprogram_body', lAllDicts)


#        for tmp in lAllDicts:
#            print(tmp)

        return create_tois(lAllDicts, oFile)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            sExpected = oToi.get_meta_data('expected')
            sActual = lTokens[0].get_value()
            sSolution = f'Change {sActual} to {sExpected}'
            oViolation = violation.New(iLine, oToi, sSolution)
            dAction = {}
            dAction['expected'] = sExpected
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions['expected'])
        oViolation.set_tokens(lTokens)


def add_identifiers_from_to(sType1, sType2, lAllDicts):
    lReturn = []
    for dDict in lAllDicts:
        if not dDict['type'] == sType2:
            lReturn.append(dDict)
            continue
        for dDict2 in lAllDicts:
            if dDict2['type'] == sType1:
                if dDict2['keyword'] < dDict['keyword'] < dDict2['end']:
                    dDict['identifiers'].extend(dDict2['identifiers'])
        lReturn.append(dDict)
    return lReturn


def remove_duplicate_names(sType1, sType2, lAllDicts):
    return remove_duplicate_numbers(sType1, sType2, 'names', lAllDicts)


def remove_duplicate_identifiers(sType1, sType2, lAllDicts):
    return remove_duplicate_numbers(sType1, sType2, 'identifiers', lAllDicts)


def remove_duplicate_numbers(sType1, sType2, sKey, lAllDicts):
    lReturn = []
    for dDict in lAllDicts:
        if not dDict['type'] == sType1:
            lReturn.append(dDict)
            continue
        for dDict2 in lAllDicts:
            if dDict2['type'] == sType2:
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
            if dDict['keyword'] < iIdentifier < dDict['begin']:
                lId.append(iIdentifier)
        dDict['identifiers'] = lId
        lReturn.append(dDict)
    return lReturn


def populate_statement_part_names(lAllDicts, lNames):
    lReturn = []
    for dDict in lAllDicts:
        lId = []
        for iName in lNames:
            if dDict['begin'] < iName < dDict['end']:
                lId.append(iName)
        try:
            dDict['names'].extend(lId)
        except KeyError:
            dDict['names'] = lId
        lReturn.append(dDict)
    return lReturn


def populate_declarative_part_names(lAllDicts, lNames):
    lReturn = []
    for dDict in lAllDicts:
        lId = []
        for iName in lNames:
            if dDict['keyword'] < iName < dDict['begin']:
                lId.append(iName)
        dDict['names'] = lId
        lReturn.append(dDict)
    return lReturn


def create_tois(lAllDicts, oFile):
    lReturn = []
    oTokenMap = oFile.get_token_map()
    for dDict in lAllDicts:
        for iName in dDict['names']:
            for iIdentifier in dDict['identifiers']:
                iLine = oTokenMap.get_line_number_of_index(iName)
#                print(f'--> {iLine} :: {iIdentifier} :: {iName} <' + '-'*80)
                sName = oFile.lAllObjects[iName].get_value()
                sIdentifier = oFile.lAllObjects[iIdentifier].get_value()
                if sIdentifier.lower() == sName.lower():
#                    print(f'{iName}:{iIdentifier}')
#                    print(f'{sName}:{sIdentifier}')
#                    print(dDict)
                    if not sIdentifier == sName:
#                        print(f'iLine = {iLine}')
                        oToi = tokens.New(iName, iLine, [oFile.lAllObjects[iName]])
                        oToi.set_meta_data('expected', sIdentifier)
                        lReturn.append(oToi)
#                        print('  MISMATCH')
#                    else:
#                        print('   MATCH')
                    break

    return lReturn


def merge_dict_lists(lOne, lTwo):
    lReturn = []
    lReturn.extend(lOne)
    lReturn.extend(lTwo)
    return lReturn


def get_all_name_tokens(oFile, lNames):
    lReturn = []
    oTokenMap = oFile.get_token_map()
#    oTokenMap.pretty_print()
    for oToken in lNames:
#        print(oToken)
        lReturn.extend(oTokenMap.get_token_indexes(oToken))
#    lReturn.extend(oTokenMap.get_token_indexes(parser.todo))
    lReturn.sort()
    return lReturn


def get_all_identifiers(oFile, lTokens):
    lReturn = []
    for oToken in lTokens:
        lReturn.extend(get_indexes_of_token(oFile, oToken))
    return lReturn


def get_architecture_indexes(oFile):

    lKeywords = get_all_architecture_keywords(oFile)
    lBegin = get_all_architecture_begin_keywords(oFile)
    lEnd = get_all_architecture_end_keywords(oFile)

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, 'architecture_body')

def get_process_indexes(oFile):

    lKeywords = get_all_process_keywords(oFile)
    lBegin = get_all_process_begin_keywords(oFile)
    lEnd = get_all_process_end_keywords(oFile)

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, 'process')


def get_subprogram_body_indexes(oFile):

    lKeywords = get_all_subprogram_body_is_keywords(oFile)
    lBegin = get_all_subprogram_body_begin_keywords(oFile)
    lEnd = get_all_subprogram_body_end_keywords(oFile)

    return merge_block_indexes_into_list(lKeywords, lBegin, lEnd, 'subprogram_body')


def get_block_indexes(oFile):

    lKeywords = get_all_block_keywords(oFile)
    lBegin = get_all_block_begin_keywords(oFile)
    lEnd = get_all_block_end_keywords(oFile)

    lIndexes = merge_block_indexes_into_list(lKeywords, lBegin, lEnd, 'block_statement')

    return lIndexes


def get_component_declaration_indexes(oFile):

    lKeywords = get_all_component_keywords(oFile)
    lBegin = lKeywords
    lEnd = get_all_component_end_keywords(oFile)

    return merge_three_indexes_into_list(lKeywords, lBegin, lEnd, 'component_declaration')


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
        dProc['type'] = sType
        dProc['keyword'] = lTemp[0]
        dProc['begin'] = lTemp[1]
        dProc['end'] = lTemp[2]
        lReturn.append(dProc)
    return lReturn


def get_inner_indexes(lFirst, lSecond):
    lReturn = []
    lMyFirst = lFirst.copy()
    lMySecond = lSecond.copy()
    while len(lMyFirst) > 0:
#        print(lMyFirst)
        dDelta = {}
        lTemp = []
        for iFirst in lMyFirst:
            for iSecond in lMySecond:
#                print(f'{iFirst}:{iSecond} = {iFirst - iSecond}')
                iDelta = iSecond - iFirst
                if iDelta > 0:
                    dDelta[iDelta] = [iFirst, iSecond]

#        print(dDelta)

        lKeys = list(dDelta.keys())
        lKeys.sort()
#        print(lKeys)
#        print(lKeys[0])
#        print(dDelta[lKeys[0]])
        
        lReturn.append(dDelta[lKeys[0]])
        lMyFirst.remove(dDelta[lKeys[0]][0])
        lMySecond.remove(dDelta[lKeys[0]][1])

    return lReturn

def merge_three_indexes_into_list(lFirst, lSecond, lThird, sType):
#    print(lFirst)
#    print(lSecond)
#    print(lThird)
    lReturn = []
    for i in range(0, len(lFirst)):
        dProc = {}
        dProc['type'] = sType
        dProc['keyword'] = lFirst[i]
        dProc['begin'] = lSecond[i]
        dProc['end'] = lThird[i]
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

def get_indexes_of_token(oFile, oToken):
    oTokenMap = oFile.get_token_map()
    return oTokenMap.get_token_indexes(oToken)

