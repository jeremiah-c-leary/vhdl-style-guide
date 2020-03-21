from vsg import rule


class keyword_alignment_rule(rule.rule):
    '''
    Checks for keyword alignment in consecutive statements.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    Attributes
    ----------

    sKeyword : string
       The keyword to align.

    sStartGroupTrigger: string
       The line attribute which marks the start of a group to align.

    sEndGroupTrigger: string
       The line attribute which ends the group to align.

    lLineTriggers : list of strings
       List of trigger attributes.
       If line has at least one of these attributes it will be added to the group for alignment.
    '''

    def __init__(self, name=None, identifier=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 5
        # The following is filled out by the user
        self.sKeyword = None
        self.sStartGroupTrigger = None
        self.sEndGroupTrigger = None
        self.lLineTriggers = None
        self.subphase = 2
        self.configuration_triggers = []

        self.compact_alignment = True
        self.configuration.append('compact_alignment')

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')

        self.configuration_triggers = [{'name': 'blank_line_ends_group', 'triggers': ['isBlank']},
                                       {'name': 'comment_line_ends_group', 'triggers': ['isComment']}]

    def _before_keyword_column(self, line, keyword_column):
        before_keyword_column = keyword_column - 1
        if before_keyword_column < 2:
            return 0, False

        while before_keyword_column > 0:
            if line[before_keyword_column] != ' ':
                break
            else:
                before_keyword_column -= 1

        if before_keyword_column == 0 and line[0] == ' ':
            before_keyword_column = keyword_column - 2

        return before_keyword_column, True if keyword_column - before_keyword_column == 2 else False

    def _check_alignment(self):
        violation = {'lines': []}

        max_keyword_column = 0
        max_before_keyword_column = 0  # Max column of non space character before keyword column.
        alignment = None
        violation_found = False

        one_space_gaps = []

        for oLine in self.lGroup:
            if self.sKeyword in oLine['line'].line:
                line = {'number': oLine['number'], 'keyword_column': oLine['line'].line.find(self.sKeyword)}

                if line['keyword_column'] > max_keyword_column:
                    max_keyword_column = line['keyword_column']

                before_keyword_column, one_space_gap = self._before_keyword_column(oLine['line'].line, line['keyword_column'])
                line['before_keyword_column'] = before_keyword_column
                one_space_gaps.append(one_space_gap)

                violation['lines'].append(line)

                if before_keyword_column > max_before_keyword_column:
                    max_before_keyword_column = before_keyword_column

                if alignment is None:
                    alignment = line['keyword_column']

                if not alignment == line['keyword_column']:
                    violation_found = True

        if self.compact_alignment and one_space_gaps and not any(one_space_gaps):
            violation_found = True

        if violation_found:
            violation['max_keyword_column'] = max_keyword_column
            violation['max_before_keyword_column'] = max_before_keyword_column
            self.add_violation(violation)

    def _pre_analyze(self):
        self.lGroup = []
        self.fTriggerFound = False

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sStartGroupTrigger]:
            if self.fTriggerFound:
                # We should throw an exception here, however clocked processes are classified in a way that
                # leads to exceptions for sequential rule 005.
                # raise Exception("Nested start trigger")
                pass
            else:
                self.fTriggerFound = True

        if self.fTriggerFound:
            line = {'number': iLineNumber, 'line': oLine}

            if oLine.__dict__[self.sEndGroupTrigger]:
                self.lGroup.append(line)
                self.fTriggerFound = False
                self._check_alignment()
                self.lGroup = []
            else:
                for configuration in self.configuration_triggers:
                    if self.__dict__[configuration['name']]:
                        for trigger in configuration['triggers']:
                            if oLine.__dict__[trigger]:
#                                self.lGroup.append(line)
                                self._check_alignment()
                                self.lGroup = []
                                break
                for trigger in self.lLineTriggers:
                    if oLine.__dict__[trigger]:
                        self.lGroup.append(line)
                        break

    def _fix_compact_align(self, oFile):
        for violation in self.violations:
            for line in violation['lines']:
                before_keyword_column = line['before_keyword_column']
                keyword_column = line['keyword_column']
                oLine = oFile.lines[line['number']]
                oLine.update_line(oLine.line[:before_keyword_column + 1] +
                                  ' ' * (1 + violation['max_before_keyword_column'] - before_keyword_column) +
                                  oLine.line[keyword_column:])

    def _fix_max_keyword_column(self, oFile):
        for violation in self.violations:
            for line in violation['lines']:
                keyword_column = line['keyword_column']
                oLine = oFile.lines[line['number']]
                oLine.update_line(oLine.line[:keyword_column] + ' ' * (violation['max_keyword_column'] - keyword_column) + oLine.line[keyword_column:])

    def _fix_violations(self, oFile):
        if self.compact_alignment:
            self._fix_compact_align(oFile)
        else:
            self._fix_max_keyword_column(oFile)
