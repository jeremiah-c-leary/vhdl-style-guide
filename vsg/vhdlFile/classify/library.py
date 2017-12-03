import re


def library(oLine):

    if not oLine.insideEntity and not oLine.insideArchitecture and not oLine.insidePackage and not oLine.insidePackageBody:
        # Check for library lines
        if re.match('^\s*library', oLine.lineLower):
            oLine.isLibrary = True
            oLine.indentLevel = 0
        # Check for library use lines
        if re.match('^\s*use', oLine.lineLower):
            oLine.isLibraryUse = True
            oLine.indentLevel = 1
