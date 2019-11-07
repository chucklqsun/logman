import Logman.Config.Color as c
Fields = [
    {
        "name": "date",
        "regex": '\d{2}-\w{3}-\d{4}',
        "color": c.Color.OKGREEN
    },
    {
        "name": "time",
        "regex": '\d{2}:\w{2}:\d{2}.\d{3}',
        "color": c.Color.OKGREEN
    },
    {
        "name": "level",
        "regex": '(INFO|DEBUG|ERROR)',
        "color": c.Color.FAIL
    }
]
