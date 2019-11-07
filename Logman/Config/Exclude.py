
class Exclude:
    # timestamp will be replaced by default
    Exclude_replace_pattern = [
        # replace 1st with 2nd
        ["^\d{2}-\w{3}-\d{4} \d{2}:\w{2}:\d{2}.\d{3} (INFO|DEBUG|ERROR|WARN)", ""],
    ]

