import unittest
import os

from src import NginxSiteTools

class TestNginxSiteTools(unittest.TestCase):

    def test_ReplaceInputVariablesInFile(self):
        valuesDict = {
            'MQTT__WSPATH': '/mqtt',
            'MQTT__SCHEME': 'https',
            'MQTT__HOSTNAME': 'rabbit_host',
            'MQTT__WSPORT': '15675'
        }
        inputFile = 'tests/nginx.dev.conf'
        outputFile = 'tests/nginx.test.conf'
        os.environ['MQTT__WSPORT'] = valuesDict['MQTT__WSPORT']
        NginxSiteTools.ReplaceWithEnvironmentVariables(inputFile, outputFile, False)
        with open(outputFile, 'r') as f:
            replacedStr = f.read()
        self.assertTrue('15675' in replacedStr)
        self.assertTrue('${MQTT__WSPATH}' in replacedStr)
        NginxSiteTools.ReplaceInputVariablesInFile(inputFile, outputFile, valuesDict, True)
        with open(outputFile, 'r') as f:
            replacedStr = f.read()
        self.assertTrue('rabbit_host' in replacedStr)

    def test_ReplaceInputVariables(self):
        testStr = "some stuff { ${REPLACEMENT_VALUE} other stuff and more ${REPLACEMENT_VALUE_2}  }"
        valuesDict = {'REPLACEMENT_VALUE': 'first_value', 'REPLACEMENT_VALUE_2': 'second_value'}
        shouldBeStr = "some stuff { first_value other stuff and more second_value  }"
        replacedStr = NginxSiteTools.ReplaceInputVariables(testStr, valuesDict, True)
        self.assertEqual(replacedStr, shouldBeStr)


if __name__ == '__main__':
    unittest.main()