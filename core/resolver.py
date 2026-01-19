def resolve_term(state):
    code = generate_code(state)

    return lookup_term(code)


def generate_code(state):
    return "TERM_UNDEFINED"


def lookup_term(code):
    return code  # placeholder
