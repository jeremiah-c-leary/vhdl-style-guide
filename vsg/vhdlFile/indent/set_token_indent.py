
from vsg import parser
from vsg import token

from vsg.vhdlFile import utils


def set_token_indent(dIndentMap, lTokens):
    lTokenKeys, dIndents = process_indent_map(dIndentMap)

    iIndent = 0
    bLibraryFound = False
    bArchitectureFound = False
    dVars = {}
    dVars['insideConcurrentSignalAssignment'] = False

    for iToken, oToken in enumerate(lTokens):

        if isinstance(oToken, parser.whitespace):
            continue

        if isinstance(oToken, parser.blank_line):
            bLibraryFound = False
            continue

        if isinstance(oToken, parser.carriage_return):
            continue

        sUniqueId = oToken.get_unique_id(sJoin=':')

        iTokenIndent = None

        if sUniqueId in lTokenKeys:
            token_key = dIndents[sUniqueId]['token']
            after_key = dIndents[sUniqueId]['after']
            iTokenIndent = update_indent_var(iIndent, token_key)
            oToken.set_indent(iTokenIndent)
            iIndent = update_indent_var(iIndent, after_key)

        if isinstance(oToken, token.context_declaration.end_keyword):
            bLibraryFound = False
            continue

        if isinstance(oToken, token.library_clause.keyword):
            bLibraryFound = True
            continue

        if isinstance(oToken, token.use_clause.keyword):
            if not bArchitectureFound:
                oToken.set_indent(iIndent + 1)
            else:
                oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.context_reference.keyword):
            if bLibraryFound:
                oToken.set_indent(iIndent + 1)
            else:
                oToken.set_indent(iIndent)
            continue

        if isinstance(oToken, token.architecture_body.architecture_keyword):
            bLibraryFound = False
            bArchitectureFound = True
            continue

        if isinstance(oToken, token.architecture_body.semicolon):
            bArchitectureFound = False
            continue

        if isinstance(oToken, token.entity_declaration.entity_keyword):
            bLibraryFound = False
            continue

        if isinstance(oToken, token.package_body.package_keyword):
            bLibraryFound = False
            continue

        if isinstance(oToken, token.package_declaration.package_keyword):
            bLibraryFound = False
            continue

        ### Comments
        if isinstance(oToken, parser.comment):
            set_indent_of_comment(bLibraryFound, iToken, lTokens, iIndent, lTokenKeys, dIndents)
            continue

        ### Concurrent signal assignment
        if isinstance(oToken, token.concurrent_signal_assignment_statement.label_name):
            dVars['insideConcurrentSignalAssignment'] = True
            continue

        if isinstance(oToken, token.concurrent_signal_assignment_statement.postponed_keyword):
            dVars['insideConcurrentSignalAssignment'] = True
            continue

        if isinstance(oToken, token.concurrent_simple_signal_assignment.target):
            dVars['insideConcurrentSignalAssignment'] = True
            continue

        if isinstance(oToken, token.concurrent_conditional_signal_assignment.target):
            dVars['insideConcurrentSignalAssignment'] = True
            continue

        if isinstance(oToken, token.concurrent_selected_signal_assignment.with_keyword):
            dVars['insideConcurrentSignalAssignment'] = True
            continue

        if isinstance(oToken, token.concurrent_simple_signal_assignment.semicolon):
            dVars['insideConcurrentSignalAssignment'] = False
            continue

        if isinstance(oToken, token.concurrent_conditional_signal_assignment.semicolon):
            dVars['insideConcurrentSignalAssignment'] = False
            continue

        if isinstance(oToken, token.concurrent_selected_signal_assignment.semicolon):
            dVars['insideConcurrentSignalAssignment'] = False
            continue

        oToken.set_indent(iTokenIndent)


def update_indent_var(iIndent, update):
    if str(update).startswith('+'):
        return iIndent + int(update)
    if str(update).startswith('-'):
        return iIndent + int(update)
    if update == 'current':
        return iIndent
    return update


def process_indent_map(dIndentMap):
    dReturn = {}
    lTopKeys = list(dIndentMap['indent']['tokens'].keys())
    for sTopKey in lTopKeys:
        lSubKeys = list(dIndentMap['indent']['tokens'][sTopKey].keys())
        for sSubKey in lSubKeys:
            sUniqueId = sTopKey + ':' + sSubKey
            dReturn[sUniqueId] = dIndentMap['indent']['tokens'][sTopKey][sSubKey]

    lReturn = list(dReturn.keys())

    return lReturn, dReturn


def is_use_clause_use_keyword_next(iIndex, lTokens):
    iToken = utils.find_next_non_whitespace_token(iIndex, lTokens)
    if isinstance(lTokens[iToken], token.use_clause.keyword):
        return True
    if isinstance(lTokens[iToken], token.context_reference.keyword):
        return True
    return False


def set_indent_of_comment(bLibraryFound, iToken, lTokens, iIndent, lTokenKeys, dIndents):
    oToken = lTokens[iToken]
    if bLibraryFound:
        if is_use_clause_use_keyword_next(iToken + 1, lTokens):
            oToken.set_indent(iIndent + 1)
        else:
            oToken.set_indent(iIndent)
    elif oToken.is_block_comment:
        if oToken.block_comment_indent == 0:
            oToken.set_indent(0)
        else:
            oToken.set_indent(iIndent)
    else:
        iTemp = get_indent_value_of_next_token(iToken, lTokens, iIndent, lTokenKeys, dIndents)
        oToken.set_indent(iTemp)


def get_indent_value_of_next_token(iToken, lTokens, iIndent, lTokenKeys, dIndents):
    iIndex = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
    sUniqueId = lTokens[iIndex].get_unique_id(sJoin=':')
    if sUniqueId in lTokenKeys:
        token_key = dIndents[sUniqueId]['token']
        iTokenIndent = update_indent_var(iIndent, token_key)
        return iTokenIndent
    return iIndent
