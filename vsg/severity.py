

class error():

    def __init__(self, name):
        self.name = name
        self.type = 'error'
        self.count = 0


class warning():

    def __init__(self, name):
        self.name = name
        self.type = 'warning'
        self.count = 0


class create_list():

    def __init__(self, dConfiguration):
        self.iMaxNameLength = 0
        self.lSeverities = _add_built_in_severities(self)
        _update_severities_from_configuration(self, dConfiguration)
        self.clear_severity_counts()

    def add_severity(self, oSeverity):
        self.lSeverities.append(oSeverity)

    def get_severity_named(self, sName):
        for oSeverity in self.lSeverities:
            if sName == oSeverity.name:
                return oSeverity
        return None

    def get_severities(self):
        return self.lSeverities

    def clear_severity_counts(self):
        for oSeverity in self.lSeverities:
            oSeverity.count = 0


def _add_built_in_severities(self):
    '''
    Creates the built in severity types.

    Parameters: (None)

    Returns: (list of severity objects)
    '''
    lReturn = []
    lReturn.append(set_error_severity)
    lReturn.append(set_warning_severity)
    self.iMaxNameLength = max(self.iMaxNameLength, len('Warning'))
    return lReturn


def _extract_severities_from_configuration(dConfiguration):
    '''
    Creates a list of severities from a configuration.

    Parameters:

        dConfiguration: (Configuration dictionary)

    Returns: (list of severity objects)
    '''
    lReturn = []
    if 'severity' in dConfiguration:
        for sKey in list(dConfiguration['severity']):
            if dConfiguration['severity'][sKey]['type'] == 'error':
                lReturn.append(error(sKey))
            elif dConfiguration['severity'][sKey]['type'] == 'warning':
                lReturn.append(warning(sKey))
    return lReturn


def _update_severities_from_configuration(self, dConfiguration):
    '''
    Adds user defined severities to the build in severities.

    Parameters:

        dConfiguration: (Configuration dictionary)

    Returns: (Nothing)
    '''
    lUserSeverities = _extract_severities_from_configuration(dConfiguration)
    for oSeverity in lUserSeverities:
        self.add_severity(oSeverity)
        self.iMaxNameLength = max(self.iMaxNameLength, len(oSeverity.name))


set_error_severity = error('Error')
set_warning_severity = warning('Warning')
