def askCards(types, values):
    cards = {}
    for type in types:
        for value in values:
            choice = input(f"Hai un {value} di {type}? (y/N)")
            if choice.lower() == 'y':
                if f"{value}:{type}" in cards:
                    cards[f"{value}:{type}"] += 1
                else:
                    cards[f"{value}:{type}"] = 1
    return cards

def askCard(types, values):
    card = input("Inserisci la carta (tipo:valore): ")
    if card in [f"{value}:{type}" for type in types for value in values]:
        return card