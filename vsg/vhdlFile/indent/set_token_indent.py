
from vsg import parser
from vsg import token


def set_token_indent(dIndentMap, lTokens):

    lTokenKeys, dIndents = process_indent_map(dIndentMap)

    iIndent = 0
    bLibraryFound = False
    bArchitectureFound = False
    dVars = {}
    dVars['insideConcurrentSignalAssignment'] = False

    for oToken in lTokens:

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
            if bLibraryFound:
                oToken.set_indent(iIndent + 1)
            else:
                oToken.set_indent(iIndent)
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
