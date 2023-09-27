import re

TRANSLATION_MAP = {
    ord(ru): en
    for ru, en in {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }.items()
}
RE_NON_ENG_CHARS = re.compile("[^a-z0-9_]")
MANY_UNDERSCORES = re.compile("_+")


def custom_slugify(value, separator):
    """Slugify a string, to make it URL friendly."""

    return MANY_UNDERSCORES.sub(
        "_", RE_NON_ENG_CHARS.sub("_", value.lower().translate(TRANSLATION_MAP))
    ).replace("_", separator)


def on_config(config):
    config["mdx_configs"]["toc"]["slugify"] = custom_slugify
    return config
