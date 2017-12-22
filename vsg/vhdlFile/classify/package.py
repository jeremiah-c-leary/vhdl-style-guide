import re


def package(dVars, oLine):

    # Check package declarations
    if re.match('^\s*package', oLine.lineLower) and not oLine.insidePackage and not oLine.insidePackageBody:
        oLine.isPackageKeyword = True
        oLine.insidePackage = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 1
    if oLine.insidePackage:
        if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent and not oLine.insideTypeRecord:
            if re.match('^\s*end\s+', oLine.lineLower):
                oLine.isPackageEnd = True
                oLine.indentLevel = 0
                dVars['iCurrentIndentLevel'] = 0
