

def debug_lines(oFile, iLineNumber, iNumberOfLines):  # pragma: no cover

    for iIndex in range (0, iNumberOfLines):
        print '{0:5d} | {1:s}'.format(iLineNumber + iIndex, oFile.lines[iLineNumber + iIndex].line)
