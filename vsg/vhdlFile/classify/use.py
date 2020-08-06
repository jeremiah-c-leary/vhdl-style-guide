
import re


def use(dVars, lTokens, lObjects, oLine):

    '''
    Classifies library declarations.

    use identifier ;

    Sets the following line attributes:

      * isLibraryUse

    Modifies the following variables:

      * bInsideUse
    '''

    ## This will be depricated when the object method is done for libraries
    if not oLine.insideEntity and not oLine.insideArchitecture and not oLine.insidePackage and not oLine.insidePackageBody:
        check_use_keyword(oLine)


def check_use_keyword(oLine):
    if re.match('^\s*use', oLine.lineLower):
        oLine.isLibraryUse = True
        oLine.indentLevel = 1
