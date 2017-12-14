
import pprint

def debug_lines(oFile, iLineNumber, iNumberOfLines):

    for iIndex in range(0, iNumberOfLines):
        print('{0:5d} | {1:s}'.format(iLineNumber + iIndex, oFile.lines[iLineNumber + iIndex].line))


def read_file(sFilename, lLines):
    with open(sFilename) as oFile:
        for sLine in oFile:
            lLines.append(sLine.rstrip())


def print_attributes(oLine):
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(oLine.__dict__)
