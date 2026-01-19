from core.parser import parse_chain
from core.rule_engine import evaluate
from core.resolver import resolve_term

chain = "mother > elder brother > daughter"
tokens = parse_chain(chain)
state = evaluate(tokens)
term = resolve_term(state)

print(term)
