#!/usr/bin/env nu
use std log

# Given a Wikipedia page, parse the chapters of a manga into a format suitable for use in the subtitle section of the macropad script.
def main [
  wikipedia_page: string
] {
  let chapters = (
    http get $"https://en.wikipedia.org/w/api.php?action=parse&page=($wikipedia_page)&contentmodel=wikitext&prop=wikitext&format=json"
    | get parse.wikitext.*
    | lines --skip-empty
    | filter {|line| ($line | str starts-with '|{{nihongo|') or ($line | str starts-with '|"')}
    | each {|line|
      if ($line | str starts-with '|"') {
        let title = ($line | str trim --left --char '|' | str trim --char '"')
        {
          english: $title
          kanji: $title
          hepburn: $title
        }
      } else {
        $line | parse --regex '\|\{\{nihongo\|"(?P<english>.+)"(?:\|(?P<kanji>.+)\|(?P<hepburn>.+)\}\}){0,1}' | first
      }
    }
    | each {|chapter|
      if ($chapter.kanji | is-empty) {
        $chapter | insert kana ""
      } else {
        $chapter | insert kana ($chapter.kanji | ^kakasi -JH -KH -Ea -s -iutf8 -outf8)
      }
    }
    | enumerate
    | update index {|i| $i.index + 1}
    | rename index title
  )

  # SUBTITLES = {
  #   "1": {
  #       0: {"title": "凛太郎と薫子", "sort": "りんたろう と かおるこ"},
  #       1: {"title": "Rintaro and Kaoruko"},
  #       2: {"title": "Rintarō to Kaoruko"},
  #   },
  #   "2": {
  #       0: {"title": "千鳥と桔梗", "sort": "ちどり と ききょう"},
  #       1: {"title": "Chidori and Kikyo"},
  #       2: {"title": "Chidori to Kikyō"},
  #   },
  # }

  $chapters | reduce --fold '' {|chapter, acc|
    $acc + $"  '($chapter.index)': {\n    0: {'title': '($chapter.title.kanji)', 'sort': '($chapter.title.kana)'},\n    '1': {'title': '($chapter.title.english)'},\n    '2': {'title': '($chapter.title.hepburn)'},\n  },\n"
  }
}
