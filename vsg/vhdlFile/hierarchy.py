
from vsg import token


def set_token_hierarchy_value(lTokens):
    lIfHierarchy = []
    for oToken in lTokens:
        check_if_statement(oToken, lIfHierarchy)
        check_case_statement(oToken, lIfHierarchy)
        check_loop_statement(oToken, lIfHierarchy)


def check_case_statement(oToken, lIfHierarchy):
    check_for_hierarchy_nesting(oToken, lIfHierarchy, token.case_statement.case_keyword, token.case_statement.semicolon)


def check_loop_statement(oToken, lIfHierarchy):
    check_for_hierarchy_nesting(oToken, lIfHierarchy, token.loop_statement.loop_keyword, token.loop_statement.semicolon)


def check_for_hierarchy_nesting(oToken, lIfHierarchy, oStartToken, oEndToken):
    if tokens_match(oToken, oStartToken):
        insert_hierarchy_index(lIfHierarchy)
    elif tokens_match(oToken, oEndToken):
        remove_hierarchy_index(lIfHierarchy)


def insert_hierarchy_index(lIfHierarchy):
    lIfHierarchy.append(0)


def remove_hierarchy_index(lIfHierarchy):
    if len(lIfHierarchy) > 0 and lIfHierarchy[-1] == 0:
            lIfHierarchy.pop()


def check_if_statement(oToken, lIfHierarchy):
    set_if_keyword_hierarchy(oToken, lIfHierarchy)
    set_elsif_keyword_hierarchy(oToken, lIfHierarchy)
    set_else_keyword_hierarchy(oToken, lIfHierarchy)
    set_if_semicolon_hierarchy(oToken, lIfHierarchy)


def set_if_keyword_hierarchy(oToken, lIfHierarchy):
    if tokens_match(oToken, token.if_statement.if_keyword):
        if len(lIfHierarchy) == 0:
            lIfHierarchy.append(0)
        oToken.set_hierarchy(lIfHierarchy[-1])
        lIfHierarchy[-1] += 1


def set_elsif_keyword_hierarchy(oToken, lIfHierarchy):
    if tokens_match(oToken, token.if_statement.elsif_keyword):
        oToken.set_hierarchy(lIfHierarchy[-1] - 1)


def set_else_keyword_hierarchy(oToken, lIfHierarchy):
    if tokens_match(oToken, token.if_statement.else_keyword):
        oToken.set_hierarchy(lIfHierarchy[-1] - 1)


def set_if_semicolon_hierarchy(oToken, lIfHierarchy):
    if tokens_match(oToken, token.if_statement.semicolon):
        lIfHierarchy[-1] -= 1
        oToken.set_hierarchy(lIfHierarchy[-1])
        if lIfHierarchy[-1] == 0:
            lIfHierarchy.pop()


def tokens_match(oToken1, oToken2):
    if isinstance(oToken1, oToken2):
        return True
    return False
