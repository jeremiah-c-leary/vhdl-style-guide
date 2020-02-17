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
        self.rule_specific_configuration = []

        self.blank_line_ends_group = True
        self.configuration.append('blank_line_ends_group')
        self.comment_line_ends_group = True
        self.configuration.append('comment_line_ends_group')

    def _check_alignment(self):
        violation = {'lines': []}

        max_keyword_column = 0
        alignment = None
        violation_found = False

        for oLine in self.lGroup:
            if self.sKeyword in oLine['line'].line:
                line = {'number': oLine['number'], 'keyword_column': oLine['line'].line.find(self.sKeyword)}
                violation['lines'].append(line)

                if line['keyword_column'] > max_keyword_column:
                    max_keyword_column = line['keyword_column']

                if alignment is None:
                    alignment = line['keyword_column']

                if not alignment == line['keyword_column']:
                    violation_found = True

        if violation_found:
            violation['max_keyword_column'] = max_keyword_column
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
            elif (oLine.isBlank and self.blank_line_ends_group) or\
                 (oLine.isComment and self.comment_line_ends_group):
                self.lGroup.append(line)
                self._check_alignment()
                self.lGroup = []
            else:
                if self.rule_specific_configuration:
                    for configuration in self.rule_specific_configuration:
                        if self.__dict__[configuration['name']]:
                            for trigger in configuration['triggers']:
                                if oLine.__dict__[trigger]:
                                    self.lGroup.append(line)
                                    self._check_alignment()
                                    self.lGroup = []
                                    break
                for trigger in self.lLineTriggers:
                    if oLine.__dict__[trigger]:
                        self.lGroup.append(line)
                        break

    def _fix_violations(self, oFile):
        for violation in self.violations:
            for line in violation['lines']:
                keyword_column = line['keyword_column']
                oLine = oFile.lines[line['number']]
                oLine.update_line(oLine.line[:keyword_column] + ' ' * (violation['max_keyword_column'] - keyword_column) + oLine.line[keyword_column:])
