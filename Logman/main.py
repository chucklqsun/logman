import Logman.Utility.File as File
import Logman.Config.Mapping as Mapping
import Logman.Config.Color as Color
import re

def main():
    log_path = 'C:\\Program Files\\Apache Software Foundation\\Tomcat 8.5\\logs\\tomcat8-stderr.2019-03-13.log'
    print("Log Path:" + log_path)
    content = File.read_file(log_path)
    for ln in content:
        line = {}
        last_flt = ""
        for flt in Mapping.Fields:
            last_flt = flt["regex"]
            x = re.search(flt["regex"], ln)
            line[flt["name"]] = {}
            if x:
                line[flt["name"]]["str"] = x.group(0)
                line[flt["name"]]["color"] = flt["color"]

                # use filter to exclude unwanted log

                print(
                    line[flt["name"]]["color"] +
                    line[flt["name"]]["str"]
                    , end=''
                )
                print(" ", end='')

        # default field
        x = re.search(last_flt+"(.*)$", ln)
        if x:
            print(Color.Color.ENDC + x.group(2), end='')
        print("")

main()
