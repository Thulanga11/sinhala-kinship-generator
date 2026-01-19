from core.state import RelationshipState

def evaluate(tokens):
    state = RelationshipState()

    for token in tokens:
        state.update(token)

    return state
