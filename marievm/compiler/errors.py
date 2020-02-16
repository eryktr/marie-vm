from typing import Any


class InvalidTokenError(Exception):
    msg = 'Invalid token: {} on line {}'.format
    lineno: int
    val: str

    def __init__(self, token):
        self.lineno = token.lineno
        self.val = token.value[0]
        super().__init__(self.msg(self.val, self.lineno))


class TooManyNewlinesError(Exception):
    msg = 'Too many newlines on line {}'.format
    lineno: int

    def __init__(self, token):
        self.lineno = token.lineno
        super().__init__(self.msg(self.lineno))


class InvalidSkipcondModeError(Exception):
    msg = 'Invalid Skipcond mode: {}'.format
    lineno: int
    mode: str

    def __init__(self, lineno: int, mode: str):
        self.lineno = lineno
        self.mode = mode
        super().__init__(self.msg(self.mode))


class InvalidSyntaxError(Exception):
    msg = 'Invalid syntax at line {}. Token: {}'.format
    lineno: int
    token: Any

    def __init__(self, lineno: int, token: Any):
        self.lineno = lineno
        self.token = token
        super().__init__(self.msg(lineno, token))

