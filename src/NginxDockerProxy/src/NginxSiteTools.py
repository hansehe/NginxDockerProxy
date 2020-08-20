import glob
import os


def GetAllNginxConfigFiles(nginxFolder = '/etc/nginx/'):
    nginxBaseFile = glob.glob(os.path.join(nginxFolder, 'nginx.conf'))
    nginxServerFiles = glob.glob(os.path.join(nginxFolder, 'conf.d', '*.conf'))
    return nginxBaseFile + nginxServerFiles


def ReplaceWithEnvironmentVariables(inputFile, outputFile, force = False):
    data = GetValidEnvironmentVariables()
    ReplaceInputVariablesInFile(inputFile, outputFile, data, force)


def ReplaceInputVariablesInFile(inputFile, outputFile, valuesDict, force = False):
    with open(inputFile, 'r') as f:
        inputStr = f.read()
    replacedStr = ReplaceInputVariables(inputStr, valuesDict, force)
    with open(outputFile, 'w') as f:
        f.write(replacedStr)


def GetValidEnvironmentVariables():
    envVariables = {}
    for key in os.environ.keys():
        envVariables[key] = os.environ[key]
    return envVariables


def ReplaceInputVariables(inputStr, valuesDict, force = False):
    index = 0
    replacedStr = inputStr
    end = len(inputStr)
    while index < end:
        startInd = inputStr[index:].find('${')
        if startInd < 0:
            break

        stopInd = startInd + inputStr[index:][startInd:].find('}')
        if stopInd < 0:
            break

        key = inputStr[index:][startInd+2:stopInd]

        value = ''
        keyMatched = False
        for valueKey in valuesDict.keys():
            if key.upper() == valueKey.upper():
                value = valuesDict[valueKey]
                keyMatched = True
                break
        
        if keyMatched or force:
            replacedStr = replacedStr.replace('${' + key + '}', value)

        index += stopInd

    return replacedStr
