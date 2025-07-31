def red(text: str) -> str:
    return f"\033[31m{text}\033[0m"


def green(text: str) -> str:
    return f"\033[32m{text}\033[0m"


def yellow(text: str) -> str:
    return f"\033[33m{text}\033[0m"


def blue(text: str) -> str:
    return f"\033[34m{text}\033[0m"


def magenta(text: str) -> str:
    return f"\033[35m{text}\033[0m"


def cyan(text: str) -> str:
    return f"\033[36m{text}\033[0m"


def white(text: str) -> str:
    return f"\033[37m{text}\033[0m"


def black(text: str) -> str:
    return f"\033[30m{text}\033[0m"


def bright_red(text: str) -> str:
    return f"\033[91m{text}\033[0m"


def bright_green(text: str) -> str:
    return f"\033[92m{text}\033[0m"


def bright_yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"


def bright_blue(text: str) -> str:
    return f"\033[94m{text}\033[0m"


def bright_magenta(text: str) -> str:
    return f"\033[95m{text}\033[0m"


def bright_cyan(text: str) -> str:
    return f"\033[96m{text}\033[0m"


def bright_white(text: str) -> str:
    return f"\033[97m{text}\033[0m"


def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def italic(text: str) -> str:
    return f"\033[3m{text}\033[0m"


def underline(text: str) -> str:
    return f"\033[4m{text}\033[0m"


def strikethrough(text: str) -> str:
    return f"\033[9m{text}\033[0m"


def bg_red(text: str) -> str:
    return f"\033[41m{text}\033[0m"


def bg_green(text: str) -> str:
    return f"\033[42m{text}\033[0m"


def bg_yellow(text: str) -> str:
    return f"\033[43m{text}\033[0m"


def bg_blue(text: str) -> str:
    return f"\033[44m{text}\033[0m"


def bg_magenta(text: str) -> str:
    return f"\033[45m{text}\033[0m"


def bg_cyan(text: str) -> str:
    return f"\033[46m{text}\033[0m"


def bg_white(text: str) -> str:
    return f"\033[47m{text}\033[0m"


def bg_black(text: str) -> str:
    return f"\033[40m{text}\033[0m"
