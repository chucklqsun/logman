from Logman.Config.Mapping import Mapping
from Logman.Config.Color import Color
import re


def display_log(post_content):
    for ln in post_content:
        line = {}
        last_flt = ""
        for flt in Mapping.Fields:
            x = re.search(flt["regex"], ln)
            line[flt["name"]] = {}
            if x:
                last_flt = flt["regex"]
                line[flt["name"]]["str"] = x.group(0)
                line[flt["name"]]["color"] = flt["color"]
                print(line[flt["name"]]["color"] + line[flt["name"]]["str"], end='')
                print(" ", end='')

        # default field
        y = re.search('%s%s' % (last_flt, "(?P<rest>.*)$"), ln)
        if y:
            print(Color.ENDC + y.group('rest'))
        else:
            print(Color.ENDC + ln)
