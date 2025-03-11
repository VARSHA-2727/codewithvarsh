def countVowelsConsonantsSpaces(s : str, n : int) -> List[int] :
    space=0
    for ch in s:
        if ch.lower() in "aeiou":
            vowel+=1
        elif ch.isalpha():
            consonant+=1
        else:
            ch.isspace()
            space+=1
    return[vowel,consonant,space]
