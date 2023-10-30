def character_count(string_list):
    character_dicc = {}
    for string in string_list:
        for character in string:
            if not character in character_dicc:
                new_character = {character : string.count(character)}
                character_dicc.update(new_character)
            else:
                character_dicc[character] += string.count(character)
    
    return character_dicc