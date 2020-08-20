

def is_object(sType, oType, oObject, lNewObjects):
    if oObject.get_value().lower() == sType:
        lNewObjects.append(oType(oObject.get_value()))
        return True
    return False


def is_current_level(dVars, sLevel):
    if current_level(dVars) == sLevel:
        return True
    return False

def pop_level(dVars):
    dVars['history'].pop()

def push_level(dVars, level):
    dVars['history'].append(level)

def current_level(dVars):
    return dVars['history'][-1]

