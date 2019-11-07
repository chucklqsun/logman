from Logman.Config.Color import Color


class Mapping:
    Fields = [
        {
            "name": "date",
            "regex": '\d{2}-\w{3}-\d{4}',
            "color": Color.OKGREEN
        },
        {
            "name": "time",
            "regex": '\d{2}:\w{2}:\d{2}.\d{3}',
            "color": Color.OKGREEN
        },
        {
            "name": "level",
            "regex": '(INFO|DEBUG|ERROR|WARN)',
            "color": Color.FAIL
        }
    ]
