def parse_chain(chain: str):
    parts = [p.strip().lower() for p in chain.split(">")]
    tokens = []

    for p in parts:
        tokens.append({
            "type": "UNKNOWN",
            "gender": "unknown"
        })

    return tokens
