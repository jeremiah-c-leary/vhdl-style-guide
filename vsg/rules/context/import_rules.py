
import importlib
import os


def extract_rule_names():
    lReturn = []
    lFiles = filter(os.path.isfile, os.listdir(os.curdir))
    for sFile in lFiles:
        if sFile.startswith('rule_') and sFile.endswith('.py'):
            lReturn.append(sFile[:-3])
    return lReturn

print(extract_rule_names())
for sRule in extract_rule_names():
    importlib.import_module(sRule)

