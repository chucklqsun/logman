from Logman.Utility.File import write_file
from Logman.GlobalConfig import GlobalConfig
import os


class Report:

    @staticmethod
    def output_report(post_content):
        post_content = "".join(post_content)
        write_file(post_content, os.path.join(GlobalConfig.app_path, "output", "report.txt"))
