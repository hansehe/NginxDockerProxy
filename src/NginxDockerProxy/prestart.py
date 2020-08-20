from src import PrestartTools
from src import NginxSiteTools

if __name__ == '__main__':
    nginxFiles = NginxSiteTools.GetAllNginxConfigFiles()
    PrestartTools.RunPrestart(nginxFiles)

