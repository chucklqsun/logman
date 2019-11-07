import Logman.Utility.File as File
import Logman.Engine.ExcludeMe as ExcludeMe
import Logman.Engine.DisplayMe as DisplayMe
from Logman.GlobalConfig import GlobalConfig
from Logman.Engine.Report import Report
import os


def main():
    GlobalConfig.app_path = os.path.dirname(os.path.realpath(__file__))

    log_path = os.path.join(GlobalConfig.app_path, 'output', 'tomcat8-stderr.2019-03-13.log')
    print("Log Path:" + log_path)
    ori_content = File.read_file(log_path)

    # use pre-define level to exclude log
    pre_content = ExcludeMe.pre_exclude_log(ori_content)

    # use exclude file to hide log
    post_content = ExcludeMe.post_exclude_log(pre_content)
    # display new log
    DisplayMe.display_log(post_content)

    # export exclude file via post_content
    ExcludeMe.output_new_exclude_file(post_content)

    # export post_content as report
    # todo: use classification for report
    Report.output_report(post_content)


# Everything from here
main()
