def fedos_mak_split_words(text: str) -> list[str]:
    return "".join(
        map(
            lambda character: character if character.isalnum() else " ",
            text.lower()
        )   
    ).split()


def fedos_mak_count_word_frequencies(words: list[str]) -> dict[str, int]:
    return dict(
        map(
            lambda word: (word, words.count(word)),
            dict.fromkeys(words)
        )
    )


def fedos_mak_top_word(freq: dict[str, int]) -> "str | None":
    return (
        None
        if not freq
        else min(
            freq,
            key=lambda word: (-freq[word], word)
        )
    )


print(fedos_mak_top_word(fedos_mak_count_word_frequencies(fedos_mak_split_words("Привет, мир! Привет... ФП — это полезно."))))
