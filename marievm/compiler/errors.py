_INVALID_TOKEN = 'Invalid token: {} on line {}'.format


class InvalidTokenError(Exception):
    lineno: int
    val: str

    def __init__(self, token):
        self.lineno = token.lineno
        self.val = token.value[0]
        super().__init__(_INVALID_TOKEN(token.value[0], token.lineno))
