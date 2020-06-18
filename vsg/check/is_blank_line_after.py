from vsg import utils


def is_blank_line_after(self, oFile, iLineNumber):
    '''
    Adds a violation if the line after iLineNumber is not blank.
    This is typically used to compress lines together.

    Parameters

      self: (rule object)

      oFile: (vhdlFile object)

      iLineNumber: (integer)
    '''
    try:
        if not oFile.lines[iLineNumber + 1].isBlank:
            self.add_violation(utils.create_violation_dict(iLineNumber))
    except IndexError:
        # In case there are no more lines in the file also treat it as violation.
        # Such files are generally incorrect VHDL files, as is_blank_line_after rule can be configured only for lines,
        # that must not be the last line of correct VHDL file. However, it is better, from user perspective, to report
        # formatting violation, than raise enigmatic Python exception.
        self.add_violation(utils.create_violation_dict(iLineNumber))
