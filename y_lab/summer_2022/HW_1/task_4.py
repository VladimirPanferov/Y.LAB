BANANA = "banana"


def all_letters_found(word: str) -> bool:
    return word.replace("-", "") == BANANA


def bananas(s) -> set:
    result = set()    
    if len(s) < len(BANANA):
        return result
    start = 0
    finish = len(s) - 1
    while start <= finish or finish - start >= len(BANANA):
        last_index = 0
        find_word = ""
        for i in range(len(BANANA)):
            for j in range(last_index + 1, len(s)):
                if BANANA[i] == s[j]:
                    find_word = f"{find_word}{s[j]}"
                    last_index = j
                    break
                else:
                    find_word = f"{find_word}-"
        if not all_letters_found(find_word):
            start += 1
            continue
        while len(find_word) < len(s):
            find_word = f"{find_word}-"
        result.add(find_word)
        start += 1
    return result


def main():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


if __name__ == "__main__":
    main()