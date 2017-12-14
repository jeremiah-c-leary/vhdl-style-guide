import re


def with_statement(dVars, oLine):
    if re.match('^\s*with', oLine.line, re.IGNORECASE):
        oLine.isWithKeyword = True
