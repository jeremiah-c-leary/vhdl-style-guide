import re


def entity(self, dVars, oLine):

    # Check for entity
    if re.match('^\s*entity', oLine.lineLower):
        self.hasEntity = True
        oLine.isEntityDeclaration = True
        dVars['iCurrentIndentLevel'] = 1
        oLine.indentLevel = 0
        oLine.insideEntity = True
    # Check for the end of the entity
    if re.match('^\s*end', oLine.lineLower) and not oLine.insidePortMap and not oLine.insideGenericMap and oLine.insideEntity:
        oLine.isEndEntityDeclaration = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 0
