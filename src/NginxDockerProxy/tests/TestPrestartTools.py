import unittest
import os

from src import PrestartTools

class TestPrestartTools(unittest.TestCase):

    def test_RunPrestart(self):
        with open('tests/nginx.dev.conf', 'r') as f:
            replacedStr = f.read()
        with open('tests/nginx.dev.prestart.conf', 'w') as f:
            f.write(replacedStr)

        nginxFiles = ['tests/nginx.dev.prestart.conf']
        PrestartTools.RunPrestart(nginxFiles)
        with open(nginxFiles[0], 'r') as f:
            replacedStr = f.read()
        self.assertTrue(not('${RABBIT_HOSTNAME}' in replacedStr))

    def test_RunPrestartWithSsl(self):
        with open('tests/nginx.dev.conf', 'r') as f:
            replacedStr = f.read()
        with open('tests/nginx.dev.prestart.conf', 'w') as f:
            f.write(replacedStr)

        nginxFiles = ['tests/nginx.dev.prestart.conf']
        PrestartTools.RunPrestart(nginxFiles)
        with open(nginxFiles[0], 'r') as f:
            replacedStr = f.read()
        self.assertTrue(not('${RABBIT_HOSTNAME}' in replacedStr))


if __name__ == '__main__':
    unittest.main()