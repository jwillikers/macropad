import time

from adafruit_macropad import MacroPad

# Prerequisites
#
# Firefox
# Disable the browser.translations.automaticallyPopup option in about:config
# Install the https://www.greasespot.net/[GreaseMonkey] extension in Firefox
# Install the SUPER MIND CONTROL II X Turbo user script for MusicBrainz
# https://github.com/jesus2099/konami-command/raw/master/mb_SUPER-MIND-CONTROL-II-X-TURBO.user.js
# Install the Guess Unicode Punctuation user script for MusicBrainz
#
# The clipse clipboard manager in the Sway desktop is necessary since I use it to manage the contents of the clipboard.
# It's bound to the keyboard shortcut Super+I
#
# Requires fcitx5 for the input of Unicode characters.
# sudo rpm-ostree install fcitx5-autostart
# sudo systemctl reboot
#
# This script is used on an Adafruit MacroPad using CircuitPython.
# It requires the MacroPad library plus all of its dependencies to be copied over to the lib directory on the MacroPad.

# Usage
#
# Configure the constants below as necessary for the works of the series you want to add.
# Set the volume start and end values, which are inclusive, accordingly.
# Save the updated script to the MacroPad in the code.py file.
# Copy the name for the first volume in the original language.
# This copied text will be used as the title and immediately followed by the index value.
# Open a browser window and focus on it.
# Click the desired key to create the series.
# Always test with 1 or 2 works in the series before doing more.
#

# Key Legend
#
# Keys are numbered in the order of left to right, top to bottom.
# The first key, #0, is the one in the top left which resides below the OLED screen.
#
# 0 - Create a series of MusicBrainz works along with their associated translated works
# 1 - Create a series of MusicBrain release groups
# 2 -
# 3 - Create a series of BookBrainz works along with their associated translated works
# 4 -
# 5 -
# 6 -
# 7 -
# 8 -
# 9 - Test snippet
# 10 -
# 11 -
#
# Rotary Encoder -
#

VOLUME_START = 2
VOLUME_END = 14

# Convert the indices to a string.
RANGE = [str(i) for i in range(VOLUME_START, VOLUME_END + 1)]

# RANGE = [
#     "1",
#     "1.1",
#     "1.2",
#     "1.3",
#     "2",
#     "3",
#     "4",
#     "5",
#     "6",
#     "7",
#     "8",
#     "9",
#     "10",
#     "11",
#     "12",
#     "13",
# ]

SUBTITLES = {
    "2": {
        0: {
            "title": "",
            "sort": "",
        },
        1: {
            "title": "",
        },
        3: {
            "title": "",
        }
    },
    "3": {
        0: {
            "title": "",
            "sort": "",
        },
        1: {
            "title": "",
        },
        3: {
            "title": "",
        }
    },
    "4": {
        0: {
            "title": "",
            "sort": "",
        },
        1: {
            "title": "",
        },
        3: {
            "title": "",
        }
    },
    "5": {
        0: {
            "title": "",
            "sort": "",
        },
        1: {
            "title": "",
        },
        3: {
            "title": "",
        }
    },
}

ORIGINAL_TITLE = {
    "text": "とんでもスキルで異世界放浪メシ |index| |subtitle|",
    "sort": "とんでも スキル で い せかい ほうろう メシ |index| |subtitle|",  # Or GUESS
    "language": "Japanese",
}

ORIGINAL_WORK_DISAMBIGUATION_COMMENT = "light novel"
TRANSLATED_WORK_DISAMBIGUATION_COMMENT = "light novel, English"

ORIGINAL_LANGUAGE = "Japanese"
TRANSLATED_LANGUAGE = "English"

ORIGINAL_WORK_ALIASES = [
    # The first alias must always be the title for the translated works
    # Remember to use the appropriate Unicode characters!
    #
    # Apostrophe:: ’
    # Dash:: ‐
    # Ellipsis:: …
    # Multiplication Sign:: ×
    # Quotation Marks:: “”
    #
    {
        "text": "Campfire Cooking in Another World With My Absurd Skill, Volume |index|: |subtitle|",
        "sort": "COPY",  # Or GUESS
        "language": "English",
        "primary": True,
    },
    {
        "text": "Campfire Cooking in Another World With My Absurd Skill, Volume |index|",
        "sort": "COPY",  # Or GUESS
        "language": "English",
        "primary": False,
    },
    {
        "text": "Tondemo Skill de Isekai Hourou Meshi |index| |subtitle|",
        "sort": "COPY",
        "language": "Japanese",
        "primary": False,
    },
]

TRANSLATED_WORK_ALIASES = [
    {
        "text": "Campfire Cooking in Another World With My Absurd Skill, Volume |index|",
        "sort": "COPY",  # Or GUESS
        "language": "English",
        "primary": False,
    },
]

MUSICBRAINZ_WORK_TYPE = "Prose"

MUSICBRAINZ_WRITER = ""
MUSICBRAINZ_ORIGINAL_WRITER_CREDITED_AS = None
MUSICBRAINZ_TRANSLATED_WRITER_CREDITED_AS = ""
MUSICBRAINZ_ORIGINAL_WORK_SERIES = ""
MUSICBRAINZ_TRANSLATED_WORK_SERIES = ""
MUSICBRAINZ_TRANSLATOR = ""

BOOKBRAINZ_WORK_TYPE = "manga" # Novel or manga

BOOKBRAINZ_ORIGINAL_WORK_SERIES = "5e867fc1-8134-41d7-a78a-3a37a4ef5ddb"
BOOKBRAINZ_ORIGINAL_WORK_SECOND_SERIES = "2770aac1-2e00-4e87-b101-3a1223c0c0bc"
BOOKBRAINZ_WORK_SECOND_SERIES_OFFSET = 41
BOOKBRAINZ_TRANSLATED_WORK_SERIES = "6deef979-9550-499f-b7f3-e72e0a48b8ec"
BOOKBRAINZ_TRANSLATED_WORK_SECOND_SERIES = "fcaca2f0-4702-4a84-b458-59235df33945"
BOOKBRAINZ_WRITER = "cfae7528-a044-43f3-966d-3c9165907e1a"
BOOKBRAINZ_ILLUSTRATOR = "cfae7528-a044-43f3-966d-3c9165907e1a"
BOOKBRAINZ_TRANSLATOR = "33eac350-7750-46f5-9c0b-f4759f60540f"
BOOKBRAINZ_ADAPTER = None
BOOKBRAINZ_LETTERER = "e1e850a9-dc4e-42eb-9110-92fbe64e6a8b"

TRANSLATED_EDITIONS = {
    # "1": "xxxx",
    # "2": "",
}

IDENTIFIERS = {
    # "1": ["", ""],
    # "2": ["", ""],
    # "3": ["", ""],
    # "4": ["", ""],
    # "5": ["", ""],
    # "6": ["", ""],
    # "7": ["", ""],
    # "8": ["", ""],
    # "9": ["", ""],
    # "10": ["", ""],
    # "11": ["", ""],
    # "12": ["", ""],
    # "13": ["", ""],
    # "14": ["", ""],
    # "15": ["", ""],
    # "16": ["", ""],
    # "17": ["", ""],
}

ORIGINAL_BOOKBRAINZ_WORK_IDENTIFIERS = {
}
TRANSLATED_BOOKBRAINZ_WORK_IDENTIFIERS = {
}

# Use the following snippet to format the items in a MusicBrainz series so that they can be copied and pasted here.
# http get --headers [Accept "application/json"]  $"https://musicbrainz.org/ws/2/series/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx?inc=work-rels" | get relations | select attribute-values.number work.id | rename number id | each {|w| $"    \"($w.number)\": \"https://beta.musicbrainz.org/work/($w.id)\"," } | print --raw
ORIGINAL_MUSICBRAINZ_WORK_IDENTIFIERS = {
}

# http get --headers [Accept "application/json"]  $"https://musicbrainz.org/ws/2/series/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx?inc=work-rels" | get relations | select attribute-values.number work.id | rename number id | each {|w| $"    \"($w.number)\": \"https://beta.musicbrainz.org/work/($w.id)\"," } | print --raw
TRANSLATED_MUSICBRAINZ_WORK_IDENTIFIERS = {
}

ORIGINAL_BOOKBRAINZ_WORK = {
    "title": ORIGINAL_TITLE,
    "type": BOOKBRAINZ_WORK_TYPE,
    "language": ORIGINAL_LANGUAGE,
    "disambiguation": ORIGINAL_WORK_DISAMBIGUATION_COMMENT,
    "aliases": ORIGINAL_WORK_ALIASES,
    "series": BOOKBRAINZ_ORIGINAL_WORK_SERIES,
    "second_series": BOOKBRAINZ_ORIGINAL_WORK_SECOND_SERIES,
    "second_series_offset": BOOKBRAINZ_WORK_SECOND_SERIES_OFFSET,
    "relationships": [
        {
            "role": "writer",
            "id": BOOKBRAINZ_WRITER,
        },
        {
            "role": "illustrator",
            "id": BOOKBRAINZ_ILLUSTRATOR,
        },
    ],
}

TRANSLATED_BOOKBRAINZ_WORK = {
    "title": ORIGINAL_WORK_ALIASES[0],
    "type": BOOKBRAINZ_WORK_TYPE,
    "language": TRANSLATED_LANGUAGE,
    "disambiguation": TRANSLATED_WORK_DISAMBIGUATION_COMMENT,
    "aliases": TRANSLATED_WORK_ALIASES,
    "series": BOOKBRAINZ_TRANSLATED_WORK_SERIES,
    "second_series": BOOKBRAINZ_TRANSLATED_WORK_SECOND_SERIES,
    "second_series_offset": BOOKBRAINZ_WORK_SECOND_SERIES_OFFSET,
    "relationships": [
        {
            "role": "provided story for",
            "id": BOOKBRAINZ_WRITER,
        },
        {
            "role": "illustrator",
            "id": BOOKBRAINZ_ILLUSTRATOR,
        },
        {
            "role": "translator",
            "id": BOOKBRAINZ_TRANSLATOR,
        },
        {
            "role": "adapter",
            "id": BOOKBRAINZ_ADAPTER,
        },
        {
            "role": "letterer",
            "id": BOOKBRAINZ_LETTERER,
        },
        # {
        #     "role": "letterer",
        #     "id": "d52c8c63-9e03-47b5-b6fa-10b2abec6131", # Madeleine Jose
        # },
        {
            "role": "translation",
            "id": "PASTE_FROM_CLIPBOARD",
        },
    ],
}

TAGS = ["fiction", "light novel"]

ORIGINAL_MUSICBRAINZ_WORK = {
    "title": ORIGINAL_TITLE,
    "type": MUSICBRAINZ_WORK_TYPE,
    "language": ORIGINAL_LANGUAGE,
    "disambiguation": ORIGINAL_WORK_DISAMBIGUATION_COMMENT,
    "aliases": ORIGINAL_WORK_ALIASES,
    "series": MUSICBRAINZ_ORIGINAL_WORK_SERIES,
    "artists": [
        {
            "id": MUSICBRAINZ_WRITER,
            "role": "Writer",
            "credited_as": MUSICBRAINZ_ORIGINAL_WRITER_CREDITED_AS,
        },
    ],
    "tags": TAGS,
}

TRANSLATED_MUSICBRAINZ_WORK = {
    "title": ORIGINAL_WORK_ALIASES[0],
    "type": MUSICBRAINZ_WORK_TYPE,
    "language": TRANSLATED_LANGUAGE,
    "disambiguation": TRANSLATED_WORK_DISAMBIGUATION_COMMENT,
    "aliases": TRANSLATED_WORK_ALIASES,
    "series": MUSICBRAINZ_TRANSLATED_WORK_SERIES,
    "artists": [
        {
            "id": MUSICBRAINZ_WRITER,
            "role": "Writer",
            "credited_as": MUSICBRAINZ_TRANSLATED_WRITER_CREDITED_AS,
        },
        {
            "id": MUSICBRAINZ_TRANSLATOR,
            "role": "Translator",
        },
    ],
    "tags": TAGS,
}

MUSICBRAINZ_RELEASE_GROUP = {
    "name": ORIGINAL_WORK_ALIASES[0]["text"],
    "disambiguation": "light novel, English, unabridged",
    "primary_type": "Other",
    "secondary_type": "Audiobook",
    "series": "",
    "credits": [
        {
            "id": MUSICBRAINZ_WRITER,
            "credited_as": "Such and such",
            "join_phrase": " read by ",
        },
        {
            "id": "",
        },
    ],
    "tags": ["light novel", "unabridged"]
}

MUSICBRAINZ_RELEASE_GROUP_LINKS = {
    "1": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "2": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "3": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "4": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "5": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "6": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "7": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "8": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "9": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
    "10": [
        {
            "url": "",
            "type": "discography entry",
        },
    ],
}

# Constants which don't usually need to be changed
MUSICBRAINZ_CREATE_WORK_URL = "https://beta.musicbrainz.org/work/create"
MUSICBRAINZ_CREATE_RELEASE_GROUP_URL = "https://beta.musicbrainz.org/release-group/create"
BOOKBRAINZ_CREATE_WORK_URL = "https://bookbrainz.org/work/create"


def next_tab(macropad):
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.PAGE_DOWN)
    time.sleep(2)


# todo Yank this to a buffer instead of using the system clipboard
def paste(macropad):
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.V)


def get_unicode_hex(char):
    """
    Returns the four-character hex code of a Unicode character.
    """
    code_point = ord(char)
    hex_code = hex(code_point)[2:].upper()  # Remove "0x" prefix and convert to uppercase
    while len(hex_code) < 4:
        hex_code = "0" + hex_code
    return hex_code


# This only works for Linux
def type_unicode_character(macropad, character):
    time.sleep(0.1)
    # Enter Unicode input mode
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.SHIFT, macropad.Keycode.U)
    time.sleep(0.1)
    macropad.keyboard_layout.write(get_unicode_hex(character))
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.1)


# An implementation of the write method for the macropad that supports Unicode characters.
def write(macropad, string):
    for character in string:
        if ord(character) < 128:
            macropad.keyboard_layout.write(character)
        else:
            type_unicode_character(macropad, character)


def clipboard_select(macropad, index):
    # Super+I is the keyboard shortcut for my clipboard manager
    macropad.keyboard.send(macropad.Keycode.GUI, macropad.Keycode.I)
    time.sleep(3)
    for _ in range(index):
        macropad.keyboard.send(macropad.Keycode.DOWN_ARROW)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(1)


def copy_browser_url(macropad):
    # todo Yank this to a buffer somehow?

    # Vimium
    # macropad.keyboard.send(macropad.Keycode.Y)
    # time.sleep(0.1)
    # macropad.keyboard.send(macropad.Keycode.Y)
    # time.sleep(0.3)

    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.C)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ESCAPE)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ESCAPE)
    time.sleep(0.1)


def tab(macropad, times=1):
    for _ in range(times):
        macropad.keyboard.send(macropad.Keycode.TAB)


def new_browser_tab(macropad, url):
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.T)
    time.sleep(0.1)
    write(macropad, url)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    # Wait for the page to load
    time.sleep(10)


def bookbrainz_set_title(macropad, index, title):
    subtitle = ""
    if "subtitle" in title and title["subtitle"]:
        subtitle = title["subtitle"]
    if "text" in title and title["text"]:
        write(macropad, title["text"].replace("|index|", f"{index}").replace("|subtitle|", subtitle))
    else:
        paste(macropad)
        time.sleep(0.1)
        write(macropad, f"{index}")
    time.sleep(0.05)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(1)
    if title["sort"] == "COPY":
        tab(macropad, 2)
        time.sleep(0.5)
        macropad.keyboard.send(macropad.Keycode.SPACE)
        time.sleep(2)
        macropad.keyboard.send(macropad.Keycode.TAB)
    elif title["sort"] == "GUESS":
        macropad.keyboard.send(macropad.Keycode.TAB)
        time.sleep(0.5)
        macropad.keyboard.send(macropad.Keycode.SPACE)
        time.sleep(2)
        tab(macropad, 2)
    else:
        sort_subtitle = ""
        if "sort_subtitle" in title and title["sort_subtitle"]:
            sort_subtitle = title["sort_subtitle"]
        write(macropad, title["sort"].replace("|index|", f"{index}").replace("|subtitle|", sort_subtitle))
        time.sleep(2)
        tab(macropad, 3)
    time.sleep(0.2)
    write(macropad, title["language"])
    time.sleep(0.2)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.5)


def bookbrainz_add_aliases(macropad, aliases):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    for index, alias in enumerate(aliases):
        write(macropad, alias["text"])
        time.sleep(0.5)
        macropad.keyboard.send(macropad.Keycode.TAB)
        time.sleep(0.5)
        if alias["sort"] == "COPY":
            tab(macropad, 2)
            time.sleep(0.5)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.5)
            macropad.keyboard.send(macropad.Keycode.TAB)
        elif alias["sort"] == "GUESS":
            macropad.keyboard.send(macropad.Keycode.TAB)
            time.sleep(0.5)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.5)
            tab(macropad, 2)
        else:
            write(macropad, alias["sort"])
            time.sleep(0.5)
            tab(macropad, 3)
        time.sleep(0.5)
        write(macropad, alias["language"])
        time.sleep(0.2)
        macropad.keyboard.send(macropad.Keycode.ENTER)
        time.sleep(0.2)
        macropad.keyboard.send(macropad.Keycode.TAB)
        if alias["primary"]:
            time.sleep(0.2)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.2)
        tab(macropad, 2)
        time.sleep(0.2)
        if index >= len(aliases) - 1:
            macropad.keyboard.send(macropad.Keycode.TAB)
            time.sleep(0.2)
        macropad.keyboard.send(macropad.Keycode.SPACE)
        time.sleep(0.6)


def bookbrainz_add_identifiers(macropad, identifiers):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.75)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.25)
    for index, identifier in enumerate(identifiers):
        write(macropad, identifier)
        time.sleep(1.25)
        tab(macropad, 4)
        time.sleep(0.25)
        if index < len(identifiers) - 1:
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.5)
        else:
            macropad.keyboard.send(macropad.Keycode.ESCAPE)
            time.sleep(1.25)


def bookbrainz_set_work_type(macropad, work_type):
    write(macropad, work_type)
    time.sleep(0.2)
    if work_type == "Novel":
        macropad.keyboard.send(macropad.Keycode.DOWN_ARROW)
        time.sleep(0.2)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.2)


def bookbrainz_add_series(macropad, series, index):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.25)
    write(macropad, series)
    time.sleep(4)
    tab(macropad, 3)
    time.sleep(0.25)
    write(macropad, "is part of")
    time.sleep(0.25)
    tab(macropad, 2)
    time.sleep(0.25)
    write(macropad, f"{index}")
    time.sleep(0.25)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(1)


BOOKBRAINZ_RELATIONSHIP_VERB = {
    "adapter": "adapted",
    "edition": "contains",
    "illustrator": "illustrated",
    "letterer": "lettered",
    "provided story for": "provided story for",
    "revisor": "revised",
    "translation": "is a translation of",
    "translator": "translated",
    "writer": "wrote",
}


def bookbrainz_add_relationship(macropad, relationship):
    if "id" not in relationship or not relationship["id"] or "role" not in relationship or not relationship["role"]:
        return
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.25)
    if relationship["id"] == "PASTE_FROM_CLIPBOARD":
        paste(macropad)
    else:
        write(macropad, relationship["id"])
    time.sleep(4)
    tab(macropad, 3)
    write(macropad, BOOKBRAINZ_RELATIONSHIP_VERB[relationship["role"].lower()])
    time.sleep(0.25)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(1)


# original_work = {
#     "title": {
#         # "text": "",
#         "sort": ORIGINAL_WORK_TITLE_SORT,
#         "language": ORIGINAL_LANGUAGE,
#     },
#     "type": "",
#     "language": "",
#     "disambiguation": ORIGINAL_WORK_DISAMBIGUATION_COMMENT,
#     "aliases": original_aliases,
#     "identifiers": original_identifiers,
#     "series": BOOKBRAINZ_ORIGINAL_WORK_SERIES,
#     "relationships": [
#         {
#             "writer": BOOKBRAINZ_WRITER,
#             "illustrator": BOOKBRAINZ_ILLUSTRATOR,
#         }
#     ],
# }
def bookbrainz_create_work(macropad, work, index):
    new_browser_tab(macropad, BOOKBRAINZ_CREATE_WORK_URL)
    tab(macropad, 11)
    time.sleep(1)
    bookbrainz_set_title(macropad, index, work["title"])
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    if "disambiguation" in work and work["disambiguation"]:
        write(macropad, work["disambiguation"])
        time.sleep(0.25)
    macropad.keyboard.send(macropad.Keycode.TAB)

    if "aliases" in work and work["aliases"]:
        aliases = []
        for a in work["aliases"]:
            subtitle = ""
            if "subtitle" in a and a["subtitle"]:
                subtitle = a["subtitle"]
            sort_subtitle = ""
            if "sort_subtitle" in a and a["sort_subtitle"]:
                sort_subtitle = a["sort_subtitle"]
            aliases.append(
                {
                    "text": a["text"].replace("|index|", f"{index}").replace("|subtitle|", subtitle),
                    "sort": a["sort"].replace("|index|", f"{index}").replace("|subtitle|", sort_subtitle),
                    "language": a["language"],
                    "primary": a["primary"],
                }
            )
        bookbrainz_add_aliases(macropad, aliases)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.2)

    if "identifiers" in work and work["identifiers"]:
        bookbrainz_add_identifiers(macropad, work["identifiers"])
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.2)

    bookbrainz_set_work_type(macropad, work["type"])
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.2)
    write(macropad, work["language"])
    time.sleep(0.2)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.2)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.2)
    if "series" in work and work["series"]:
        bookbrainz_add_series(macropad, work["series"], index)
    if "second_series" in work and work["second_series"]:
        if "second_series_offset" in work and work["second_series_offset"]:
            bookbrainz_add_series(macropad, work["second_series"], str(int(index) + work["second_series_offset"]))
        else:
            bookbrainz_add_series(macropad, work["second_series"], index)
    if "relationships" in work:
        for relationship in work["relationships"]:
            if relationship:
                bookbrainz_add_relationship(macropad, relationship)

    # Submit the work
    tab(macropad, 5)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ENTER)

    # Wait for the original work to be created
    time.sleep(20)


def musicbrainz_add_series(macropad, series, index):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.2)
    write(macropad, "Series")
    macropad.keyboard.send(macropad.Keycode.TAB)
    write(macropad, "has parts / part of")
    time.sleep(0.25)
    tab(macropad, 2)
    write(macropad, series)
    time.sleep(1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    write(macropad, f"{index}")
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.2)


def musicbrainz_add_translation_of_relationship(macropad, original_work_id):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.2)
    write(macropad, "Work")
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    write(macropad, "later versions / version of")
    time.sleep(0.25)
    tab(macropad, 2)
    time.sleep(0.1)
    if original_work_id == "PASTE_FROM_CLIPBOARD":
        paste(macropad)
    else:
        write(macropad, original_work_id)
    time.sleep(1)
    tab(macropad, 2)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.2)
    tab(macropad, 2)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.2)
    tab(macropad, 2)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.2)


def musicbrainz_add_artist(macropad, artist):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(0.75)
    write(macropad, "Artist")
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    write(macropad, artist["role"])
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    write(macropad, artist["id"])
    time.sleep(1)
    if "credited_as" in artist and artist["credited_as"]:
        macropad.keyboard.send(macropad.Keycode.TAB)
        time.sleep(0.1)
        write(macropad, artist["credited_as"])
        time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(0.2)


def musicbrainz_add_identifiers(macropad, identifiers):
    for identifier in identifiers:
        write(macropad, identifier)
        time.sleep(0.4)
        macropad.keyboard.send(macropad.Keycode.ENTER)
        time.sleep(0.4)


# This is done after the work is created
def musicbrainz_add_aliases(macropad, aliases, index=None):
    for alias_index, alias in enumerate(aliases):
        macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
        time.sleep(0.1)
        macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.RIGHT_ARROW)
        time.sleep(0.2)
        write(macropad, "/add-alias")
        time.sleep(0.2)
        macropad.keyboard.send(macropad.Keycode.ESCAPE)
        time.sleep(0.1)
        macropad.keyboard.send(macropad.Keycode.ENTER)
        time.sleep(12)

        # Add the alias
        macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.A)
        macropad.keyboard.send(macropad.Keycode.BACKSPACE)
        time.sleep(0.1)

        if alias["text"] == "PASTE_FROM_CLIPBOARD":
            paste(macropad)
            if index:
                write(macropad, f"{index}")
        else:
            write(macropad, alias["text"])

        tab(macropad, 3)

        if alias["sort"] == "PASTE_FROM_CLIPBOARD":
            paste(macropad)
            if index:
                write(macropad, f"{index}")
            tab(macropad, 3)
        elif alias["sort"] == "COPY":
            tab(macropad, 2)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.1)
            tab(macropad, 3)
        elif alias["sort"] == "GUESS":
            tab(macropad, 1)
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.1)
            tab(macropad, 1)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.1)
            tab(macropad, 3)
        else:
            write(macropad, alias["sort"])
            tab(macropad, 3)

        # Reset the language list to the beginning as a precaution.
        macropad.keyboard.send(macropad.Keycode.A)
        macropad.keyboard.send(macropad.Keycode.TAB)
        macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.TAB)
        write(macropad, alias["language"])
        time.sleep(0.1)
        macropad.keyboard.send(macropad.Keycode.TAB)
        if alias["primary"]:
            macropad.keyboard.send(macropad.Keycode.SPACE)
        tab(macropad, 2)
        write(macropad, "Work name")
        macropad.keyboard.send(macropad.Keycode.TAB)
        macropad.keyboard.send(macropad.Keycode.ENTER)
        time.sleep(12)

        if alias_index < len(aliases) - 1:
            # Remove the /aliases part at the end of the URL in the URL bar
            macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.RIGHT_ARROW)
            time.sleep(0.1)
            for _ in range(8):
                macropad.keyboard.send(macropad.Keycode.BACKSPACE)


# This is done after a work has been created
# def musicbrainz_add_tags(macropad, tags, index=None):
#     macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
#     time.sleep(0.1)
#     macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.RIGHT_ARROW)
#     time.sleep(0.2)
#     write(macropad, "/tags")
#     time.sleep(0.2)
#     macropad.keyboard.send(macropad.Keycode.ESCAPE)
#     time.sleep(0.1)
#     macropad.keyboard.send(macropad.Keycode.ENTER)
#     time.sleep(12)
#     for alias_index, alias in enumerate(aliases):
#         # Add the alias
#         macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.A)
#         macropad.keyboard.send(macropad.Keycode.BACKSPACE)
#         time.sleep(0.1)

#         if alias["text"] == "PASTE_FROM_CLIPBOARD":
#             paste(macropad)
#             if index:
#                 write(macropad, f"{index}")
#         else:
#             write(macropad, alias["text"])

#         tab(macropad, 5)
#         macropad.keyboard.send(macropad.Keycode.SPACE)
#         time.sleep(0.1)
#         tab(macropad, 3)
#         # Reset the language list to the beginning as a precaution.
#         macropad.keyboard.send(macropad.Keycode.A)
#         macropad.keyboard.send(macropad.Keycode.TAB)
#         macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.TAB)
#         write(macropad, alias["language"])
#         time.sleep(0.1)
#         macropad.keyboard.send(macropad.Keycode.TAB)
#         if alias["primary"]:
#             macropad.keyboard.send(macropad.Keycode.SPACE)
#         tab(macropad, 2)
#         write(macropad, "Work name")
#         macropad.keyboard.send(macropad.Keycode.TAB)
#         macropad.keyboard.send(macropad.Keycode.ENTER)
#         time.sleep(12)

#         if alias_index < len(aliases) - 1:
#             # Remove the /aliases part at the end of the URL in the URL bar
#             macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
#             time.sleep(0.1)
#             macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.RIGHT_ARROW)
#             time.sleep(0.1)
#             for _ in range(8):
#                 macropad.keyboard.send(macropad.Keycode.BACKSPACE)


def musicbrainz_create_work(macropad, work, index):
    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.T)
    write(macropad, MUSICBRAINZ_CREATE_WORK_URL)
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(15)
    # I use the a user script which automatically focuses on the first input box in MusicBrainz.
    subtitle = ""
    if "subtitle" in work["title"] and work["title"]["subtitle"]:
        subtitle = work["title"]["subtitle"]
    if "text" in work["title"] and work["title"]["text"]:
        write(macropad, work["title"]["text"].replace("|index|", f"{index}").replace("|subtitle|", subtitle))
    else:
        macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.V)
        write(macropad, f"{index}")
    time.sleep(0.1)
    tab(macropad, 3)
    if "disambiguation" in work and work["disambiguation"]:
        write(macropad, work["disambiguation"])
    time.sleep(0.1)
    tab(macropad, 2)
    write(macropad, work["type"])
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    write(macropad, work["language"])
    time.sleep(0.1)
    tab(macropad, 10)

    if "artists" in work:
        for artist in work["artists"]:
            musicbrainz_add_artist(macropad, artist)

    if "series" in work and work["series"]:
        musicbrainz_add_series(macropad, work["series"], index)

    if "translation_of" in work and work["translation_of"]:
        musicbrainz_add_translation_of_relationship(macropad, work["translation_of"])

    macropad.keyboard.send(macropad.Keycode.TAB)
    if "identifiers" in work and work["identifiers"]:
        musicbrainz_add_identifiers(macropad, work["identifiers"])

    # Submit by just hitting enter here, thanks to the MusicBrainz user script
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(18)

    # After the work is created, add the aliases
    if "aliases" in work and work["aliases"]:
        aliases = []
        for a in work["aliases"]:
            subtitle = ""
            if "subtitle" in a and a["subtitle"]:
                subtitle = a["subtitle"]
            sort_subtitle = ""
            if "sort_subtitle" in a and a["sort_subtitle"]:
                sort_subtitle = a["sort_subtitle"]
            aliases.append(
                {
                    "text": a["text"].replace("|index|", f"{index}").replace("|subtitle|", subtitle),
                    "sort": a["sort"].replace("|index|", f"{index}").replace("|subtitle|", sort_subtitle),
                    "language": a["language"],
                    "primary": a["primary"],
                }
            )
        musicbrainz_add_aliases(macropad, aliases, index)


# Set the Artist credit for a MusicBrainz Release Group
def musicbrainz_set_artist_credit(macropad, credits):
    macropad.keyboard.send(macropad.Keycode.SPACE)
    time.sleep(1)
    for index, credit in enumerate(credits):
        write(macropad, credit["id"])
        time.sleep(1)
        macropad.keyboard.send(macropad.Keycode.TAB)
        time.sleep(0.1)
        if "credited_as" in credit and credit["credited_as"]:
            write(macropad, credit["credited_as"])
            time.sleep(0.1)
        macropad.keyboard.send(macropad.Keycode.TAB)
        time.sleep(0.1)
        if "join_phrase" in credit and credit["join_phrase"]:
            write(macropad, credit["join_phrase"])
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.ESCAPE)
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.TAB)
            time.sleep(0.1)
        if index < len(credits) - 1:
            tab(macropad, 1 if index == 0 else 3)
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(1)
            for _ in range(5):
                macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.TAB)
            time.sleep(0.1)
        else:
            tab(macropad, 6)
            time.sleep(0.1)
            macropad.keyboard.send(macropad.Keycode.SPACE)
            time.sleep(0.5)


def musicbrainz_add_external_links(macropad, links):
    for link in links:
        if "url" not in link or not link["url"]:
            continue
        write(macropad, link["url"])
        time.sleep(0.75)
        macropad.keyboard.send(macropad.Keycode.ENTER)
        time.sleep(0.25)
        if "type" in link and link["type"]:
            write(macropad, link["type"])
            time.sleep(0.1)
            tab(macropad, 2)
            time.sleep(0.1)


def musicbrainz_create_release_group(macropad, release_group, index):
    new_browser_tab(macropad, MUSICBRAINZ_CREATE_RELEASE_GROUP_URL)
    write(macropad, release_group["name"].replace("|index|", f"{index}"))
    time.sleep(0.1)
    tab(macropad, 5)
    musicbrainz_set_artist_credit(macropad, release_group["credits"])
    macropad.keyboard.send(macropad.Keycode.TAB)
    if "disambiguation" in release_group and release_group["disambiguation"]:
        write(macropad, release_group["disambiguation"])
        time.sleep(0.1)
    tab(macropad, 2)
    time.sleep(0.1)
    write(macropad, release_group["primary_type"])
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    write(macropad, release_group["secondary_type"])
    time.sleep(0.1)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    if "series" in release_group and release_group["series"]:
        musicbrainz_add_series(macropad, release_group["series"], i)
    macropad.keyboard.send(macropad.Keycode.TAB)
    time.sleep(0.1)
    musicbrainz_add_external_links(macropad, release_group["links"])
    macropad.keyboard.send(macropad.Keycode.ENTER)
    time.sleep(15)


# To have a special title sort in MusicBrainz, it's necessary to add an alias.
aliases = []
if "aliases" in ORIGINAL_MUSICBRAINZ_WORK:
    aliases = ORIGINAL_MUSICBRAINZ_WORK["aliases"].copy()
if ORIGINAL_MUSICBRAINZ_WORK["title"]["sort"] != "COPY" and ORIGINAL_MUSICBRAINZ_WORK["title"]["text"] != ORIGINAL_MUSICBRAINZ_WORK["title"]["sort"]:
    aliases.append({
        "text": ORIGINAL_MUSICBRAINZ_WORK["title"]["text"],
        "sort": ORIGINAL_MUSICBRAINZ_WORK["title"]["sort"],
        "language": ORIGINAL_MUSICBRAINZ_WORK["title"]["language"],
        "primary": True,
    })
    if SUBTITLES:
        subtitles = {}
        for index, subtitle in SUBTITLES.items():
            if 0 in subtitle and subtitle[0]:
                subtitle[len(aliases)] = subtitle[0]
            subtitles[index] = subtitle
        SUBTITLES = subtitles
ORIGINAL_MUSICBRAINZ_WORK["aliases"] = aliases

TRANSLATED_SUBTITLES = {}
for index, subtitle in SUBTITLES.copy().items():
    if 1 in subtitle and subtitle[1]:
        TRANSLATED_SUBTITLES[index] = {
            0: subtitle[1].copy()
        }

aliases = []
if "aliases" in TRANSLATED_MUSICBRAINZ_WORK:
    aliases = TRANSLATED_MUSICBRAINZ_WORK["aliases"].copy()
if TRANSLATED_MUSICBRAINZ_WORK["title"]["sort"] != "COPY" and TRANSLATED_MUSICBRAINZ_WORK["title"]["text"] != TRANSLATED_MUSICBRAINZ_WORK["title"]["sort"]:
    aliases.append({
        "text": TRANSLATED_MUSICBRAINZ_WORK["title"]["text"],
        "sort": TRANSLATED_MUSICBRAINZ_WORK["title"]["sort"],
        "language": TRANSLATED_MUSICBRAINZ_WORK["title"]["language"],
        "primary": True,
    })
    if TRANSLATED_SUBTITLES:
        for index, subtitle in TRANSLATED_SUBTITLES.items():
            if 0 in subtitle and subtitle[0]:
                TRANSLATED_SUBTITLES[index][len(TRANSLATED_WORK_ALIASES)] = subtitle[0].copy()
TRANSLATED_MUSICBRAINZ_WORK["aliases"] = aliases

macropad = MacroPad()

last_position = 0
while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            # Add a bunch of MusicBrainz works
            if key_event.key_number == 0:
                for i in RANGE:
                    print(f"{i}")

                    original_work = ORIGINAL_MUSICBRAINZ_WORK.copy()

                    original_identifiers = []
                    if i in IDENTIFIERS:
                        original_identifiers = IDENTIFIERS[i].copy()
                    if i in ORIGINAL_MUSICBRAINZ_WORK_IDENTIFIERS:
                        original_identifiers.append(ORIGINAL_MUSICBRAINZ_WORK_IDENTIFIERS[i])
                    if i in ORIGINAL_BOOKBRAINZ_WORK_IDENTIFIERS:
                        original_identifiers.append(ORIGINAL_BOOKBRAINZ_WORK_IDENTIFIERS[i])

                    original_work["identifiers"] = original_identifiers

                    subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 0 in SUBTITLES[i] and SUBTITLES[i][0] and "title" in SUBTITLES[i][0] and SUBTITLES[i][0]["title"]:
                        subtitle = SUBTITLES[i][0]["title"]
                    sort_subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 0 in SUBTITLES[i] and SUBTITLES[i][0] and "sort" in SUBTITLES[i][0] and SUBTITLES[i][0]["sort"]:
                        sort_subtitle = SUBTITLES[i][0]["sort"]

                    original_work["title"]["subtitle"] = subtitle
                    original_work["title"]["sort_subtitle"] = sort_subtitle

                    aliases = []
                    for alias_index, alias in enumerate(original_work["aliases"].copy(), start=1):
                        alias["subtitle"] = ""
                        alias["sort_subtitle"] = ""
                        if i in SUBTITLES and SUBTITLES[i] and alias_index in SUBTITLES[i] and SUBTITLES[i][alias_index]:
                            if "title" in SUBTITLES[i][alias_index] and SUBTITLES[i][alias_index]["title"]:
                                alias["subtitle"] = SUBTITLES[i][alias_index]["title"]
                            if "sort" in SUBTITLES[i][alias_index] and SUBTITLES[i][alias_index]["sort"]:
                                alias["sort_subtitle"] = SUBTITLES[i][alias_index]["sort"]
                        aliases.append(alias)
                    original_work["aliases"] = aliases

                    musicbrainz_create_work(macropad, original_work, i)

                    # todo Get the URL in Python somehow and return it instead
                    copy_browser_url(macropad)

                    # Now create the translated work
                    translated_work = TRANSLATED_MUSICBRAINZ_WORK.copy()
                    translated_work["title"] = TRANSLATED_MUSICBRAINZ_WORK["title"].copy()
                    translated_work["aliases"] = TRANSLATED_MUSICBRAINZ_WORK["aliases"].copy()

                    translated_identifiers = []
                    if i in IDENTIFIERS:
                        translated_identifiers = IDENTIFIERS[i].copy()
                    if i in TRANSLATED_MUSICBRAINZ_WORK_IDENTIFIERS:
                        translated_identifiers.append(TRANSLATED_MUSICBRAINZ_WORK_IDENTIFIERS[i])
                    if i in TRANSLATED_BOOKBRAINZ_WORK_IDENTIFIERS:
                        translated_identifiers.append(TRANSLATED_BOOKBRAINZ_WORK_IDENTIFIERS[i])

                    translated_work["identifiers"] = translated_identifiers
                    translated_work["translation_of"] = "PASTE_FROM_CLIPBOARD"

                    subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 1 in SUBTITLES[i] and SUBTITLES[i][1] and "title" in SUBTITLES[i][1] and SUBTITLES[i][1]["title"]:
                        subtitle = SUBTITLES[i][1]["title"]
                    sort_subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 1 in SUBTITLES[i] and SUBTITLES[i][1] and "sort" in SUBTITLES[i][1] and SUBTITLES[i][1]["sort"]:
                        sort_subtitle = SUBTITLES[i][1]["sort"]

                    translated_work["title"]["subtitle"] = subtitle
                    translated_work["title"]["sort_subtitle"] = sort_subtitle

                    aliases = []
                    for alias_index, alias in enumerate(translated_work["aliases"].copy()):
                        alias["subtitle"] = ""
                        alias["sort_subtitle"] = ""
                        if i in SUBTITLES and TRANSLATED_SUBTITLES[i] and alias_index in TRANSLATED_SUBTITLES[i] and TRANSLATED_SUBTITLES[i][alias_index]:
                            if "title" in TRANSLATED_SUBTITLES[i][alias_index] and TRANSLATED_SUBTITLES[i][alias_index]["title"]:
                                alias["subtitle"] = TRANSLATED_SUBTITLES[i][alias_index]["title"]
                            if "sort" in TRANSLATED_SUBTITLES[i][alias_index] and TRANSLATED_SUBTITLES[i][alias_index]["sort"]:
                                alias["sort_subtitle"] = TRANSLATED_SUBTITLES[i][alias_index]["sort"]
                        aliases.append(alias)
                    translated_work["aliases"] = aliases

                    musicbrainz_create_work(macropad, translated_work, i)

                    # Restore the clipboard contents before continuing
                    clipboard_select(macropad, 1)
                print("Complete")
            # Create multiple Release Groups as part of a Release Group series in MusicBrainz
            if key_event.key_number == 1:
                for i in RANGE:
                    print(f"{i}")
                    release_group = MUSICBRAINZ_RELEASE_GROUP
                    if i in MUSICBRAINZ_RELEASE_GROUP_LINKS:
                        release_group["links"] = MUSICBRAINZ_RELEASE_GROUP_LINKS[i]
                    musicbrainz_create_release_group(macropad, MUSICBRAINZ_RELEASE_GROUP, index=i)
                print("Complete")
            # Create a series of BookBrainz works with their translated works
            if key_event.key_number == 3:
                for i in RANGE:
                    # Create the original work first.
                    print(f"{i}")

                    original_identifiers = []
                    if i in IDENTIFIERS:
                        original_identifiers = IDENTIFIERS[i].copy()
                    if i in ORIGINAL_MUSICBRAINZ_WORK_IDENTIFIERS:
                        original_identifiers.append(ORIGINAL_MUSICBRAINZ_WORK_IDENTIFIERS[i])

                    original_work = ORIGINAL_BOOKBRAINZ_WORK.copy()

                    original_work["identifiers"] = original_identifiers

                    subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 0 in SUBTITLES[i] and SUBTITLES[i][0] and "title" in SUBTITLES[i][0] and SUBTITLES[i][0]["title"]:
                        subtitle = SUBTITLES[i][0]["title"]
                    sort_subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 0 in SUBTITLES[i] and SUBTITLES[i][0] and "sort" in SUBTITLES[i][0] and SUBTITLES[i][0]["sort"]:
                        sort_subtitle = SUBTITLES[i][0]["sort"]

                    original_work["title"]["subtitle"] = subtitle
                    original_work["title"]["sort_subtitle"] = sort_subtitle

                    aliases = []
                    for alias_index, alias in enumerate(original_work["aliases"].copy(), start=1):
                        alias["subtitle"] = ""
                        alias["sort_subtitle"] = ""
                        if i in SUBTITLES and SUBTITLES[i] and alias_index in SUBTITLES[i] and SUBTITLES[i][alias_index]:
                            if "title" in SUBTITLES[i][alias_index] and SUBTITLES[i][alias_index]["title"]:
                                alias["subtitle"] = SUBTITLES[i][alias_index]["title"]
                            if "sort" in SUBTITLES[i][alias_index] and SUBTITLES[i][alias_index]["sort"]:
                                alias["sort_subtitle"] = SUBTITLES[i][alias_index]["sort"]
                        aliases.append(alias)
                    original_work["aliases"] = aliases

                    bookbrainz_create_work(macropad, original_work, i)

                    # todo Get the URL in Python somehow and return it instead
                    copy_browser_url(macropad)

                    # Now create the translated work

                    translated_identifiers = []
                    if i in IDENTIFIERS:
                        translated_identifiers = IDENTIFIERS[i].copy()
                    if i in TRANSLATED_MUSICBRAINZ_WORK_IDENTIFIERS:
                        translated_identifiers.append(TRANSLATED_MUSICBRAINZ_WORK_IDENTIFIERS[i])

                    translated_work = TRANSLATED_BOOKBRAINZ_WORK.copy()

                    translated_work["identifiers"] = translated_identifiers

                    subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 1 in SUBTITLES[i] and SUBTITLES[i][1] and "title" in SUBTITLES[i][1] and SUBTITLES[i][1]["title"]:
                        subtitle = SUBTITLES[i][1]["title"]
                    sort_subtitle = ""
                    if i in SUBTITLES and SUBTITLES[i] and 1 in SUBTITLES[i] and SUBTITLES[i][1] and "sort" in SUBTITLES[i][1] and SUBTITLES[i][1]["sort"]:
                        sort_subtitle = SUBTITLES[i][1]["sort"]

                    if i in TRANSLATED_EDITIONS and TRANSLATED_EDITIONS[i]:
                        translated_work["relationships"] = translated_work["relationships"].copy()
                        translated_work["relationships"].append({
                            "role": "edition",
                            "id": TRANSLATED_EDITIONS[i],
                        })

                    translated_work["title"]["subtitle"] = subtitle
                    translated_work["title"]["sort_subtitle"] = sort_subtitle

                    aliases = []
                    for alias_index, alias in enumerate(translated_work["aliases"].copy()):
                        alias["subtitle"] = ""
                        alias["sort_subtitle"] = ""
                        if i in SUBTITLES and TRANSLATED_SUBTITLES[i] and alias_index in TRANSLATED_SUBTITLES[i] and TRANSLATED_SUBTITLES[i][alias_index]:
                            if "title" in TRANSLATED_SUBTITLES[i][alias_index] and TRANSLATED_SUBTITLES[i][alias_index]["title"]:
                                alias["subtitle"] = TRANSLATED_SUBTITLES[i][alias_index]["title"]
                            if "sort" in TRANSLATED_SUBTITLES[i][alias_index] and TRANSLATED_SUBTITLES[i][alias_index]["sort"]:
                                alias["sort_subtitle"] = TRANSLATED_SUBTITLES[i][alias_index]["sort"]
                        aliases.append(alias)
                    translated_work["aliases"] = aliases

                    bookbrainz_create_work(macropad, translated_work, i)

                    # Close the two Browser tabs
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.W)
                    time.sleep(0.75)
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.W)
                    time.sleep(0.75)

                    # Restore the clipboard contents before continuing
                    clipboard_select(macropad, 1)
                print("Complete")
            if key_event.key_number == 9:
                for i in RANGE:
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.L)
                    time.sleep(0.1)
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.RIGHT_ARROW)
                    time.sleep(0.1)
                    for _ in range(8):
                        macropad.keyboard.send(macropad.Keycode.BACKSPACE)
                    musicbrainz_add_aliases(macropad, [ORIGINAL_WORK_ALIASES[1]], i)
                print("Complete")

    macropad.encoder_switch_debounced.update()
