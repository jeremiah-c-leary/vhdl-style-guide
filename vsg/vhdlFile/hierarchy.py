
from vsg import token


def set_token_hierarchy_value(lTokens):
    lIfHierarchy = []
    for oToken in lTokens:
        if isinstance(oToken, token.if_statement.if_keyword):
            if len(lIfHierarchy) == 0:
                lIfHierarchy.append(0)
            oToken.set_hierarchy(lIfHierarchy[-1])
            lIfHierarchy[-1] += 1
        if isinstance(oToken, token.if_statement.elsif_keyword):
            oToken.set_hierarchy(lIfHierarchy[-1] - 1)
        if isinstance(oToken, token.if_statement.else_keyword):
            oToken.set_hierarchy(lIfHierarchy[-1] - 1)
        if isinstance(oToken, token.if_statement.semicolon):
            lIfHierarchy[-1] -= 1
            oToken.set_hierarchy(lIfHierarchy[-1])
            if lIfHierarchy[-1] == 0:
                lIfHierarchy.pop()
        if isinstance(oToken, token.case_statement.case_keyword):
            lIfHierarchy.append(0)
        if isinstance(oToken, token.case_statement.semicolon):
            try:
                if lIfHierarchy[-1] == 0:
                    lIfHierarchy.pop()
            except IndexError:
                pass
        if isinstance(oToken, token.loop_statement.loop_keyword):
            lIfHierarchy.append(0)
        if isinstance(oToken, token.loop_statement.semicolon):
            try:
                if lIfHierarchy[-1] == 0:
                    lIfHierarchy.pop()
            except IndexError:
                pass
