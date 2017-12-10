import re


def library(oLine):

    if not oLine.insideEntity and not oLine.insideArchitecture and not oLine.insidePackage and not oLine.insidePackageBody:
        check_library_keyword(oLine)
        check_use_keyword(oLine)


def check_library_keyword(oLine):
    if re.match('^\s*library', oLine.lineLower):
        oLine.isLibrary = True
        oLine.indentLevel = 0


def check_use_keyword(oLine):
    if re.match('^\s*use', oLine.lineLower):
        oLine.isLibraryUse = True
        oLine.indentLevel = 1
