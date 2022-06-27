from itertools import combinations
from typing import Set


def bananas(s: str) -> Set[str]:
    result = set()    
    banana = "banana"
    for comb in combinations(enumerate(s), 6):
        find_word = ["-" for _ in range(len(s))]
        j = 0
        for idx, letter in comb:
            if letter == banana[j]:
                find_word[idx] = letter
                j += 1
            else:
                break
        if j == len(banana):
            result.add("".join(find_word))
    return result


def main() -> None:
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


if __name__ == "__main__":
    main()