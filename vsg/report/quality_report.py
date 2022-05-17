
import json
import hashlib


def write(commandLineArguments, dJson):

    lReport = build_report(dJson)
    write_report_to_file(lReport, commandLineArguments)


def build_report(dJson):
    lReport = []

    iViolation = 0
    for dFile in dJson['files']:
        for dViolation in dFile['violations']:
            iViolation += 1
            dEntry = create_entry(dFile, dViolation, iViolation)
            lReport.append(dEntry)
    return lReport


def write_report_to_file(lReport, commandLineArguments):
    with open(commandLineArguments.quality_report, 'w') as oFile:
        oFile.write(json.dumps(lReport, indent=2))


def create_entry(dFile, dViolation, iViolation):
    dReturn = {}
    dReturn['description'] = build_description(dViolation)
    dReturn['fingerprint'] = build_fingerprint(dFile, dViolation, iViolation)
    dReturn['severity'] = remap_severity(dViolation['severity'])
    dReturn['location'] = build_location(dFile, dViolation)
    return dReturn


def build_description(dViolation):
    return dViolation['rule'] + ' :: ' + dViolation['solution']


def build_fingerprint(dFile, dViolation, iViolation):
    sHashString = build_description(dViolation)
    sHashString += remap_severity(dViolation['severity'])
    sHashString += dFile['file_path']
    sHashString += str(dViolation['linenumber'])
    sHashString += str(iViolation)
    sHash = hashlib.md5(sHashString.encode('utf-8')).hexdigest()
    return sHash


def build_location(dFile, dViolation):
    dReturn = {}
    dReturn['path'] = dFile['file_path']
    dReturn['lines'] = {}
    dReturn['lines']['begin'] = dViolation['linenumber']
    return dReturn


def remap_severity(sSeverity):
    if sSeverity == 'Error':
        return 'critical'
    else:
        return 'minor'
