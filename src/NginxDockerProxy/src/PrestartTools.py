from src import NginxSiteTools

def RunPrestart(nginxFiles):
    for nginxFile in nginxFiles:
        NginxSiteTools.ReplaceWithEnvironmentVariables(nginxFile, nginxFile)
        print("####################################\r\r\r\r\r\r\r\r\r##########################################")
        print("Replaced variables in {0}.".format(nginxFile))
        print("####################################\r\r\r\r\r\r\r\r\r##########################################")

