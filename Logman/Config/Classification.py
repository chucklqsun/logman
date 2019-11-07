class Classification:
    category = {
        # level 1
        "ERROR": {
            "regex": "ERROR",
            "child": {
                # level 2
                "xxxxx": {
                    "regex": "xxx123",
                    "child": {}
                }
            },
        },
        "WARN": {
            "regex": "WARN",
            "child": {},
        }
    }