__author__ = 'Raymund Zacharias'

import json
import io
import itertools
from difflib import SequenceMatcher
import re

def getIPA(word, language):

    # file = io.open("IPADictionary.json")

    # dictionary = json.load(file)
    dictionary =\
        {
            "it_IT":
                (
                    # Digraphs
                    ("ch(?=(e|i))", "k"),
                    ("g(?=(e|i))", "dʒ"),
                    ("sc(?=(e|i))", "ʃ"),
                    ("gl(?=(e|i))", "ʎ"),
                    ("gn", "ɲ"),
                    ("n(?=(g|c|q))", "ŋ"),
                    ("(c'*)(?=(e|i|é|è|í|ì))", "tʃ"),
                    (r"\bz", "dz"),
                    ("\B(zz|z)\B", "ts"),
                    ("\Bss\B", "s"),
                    ("(?<=(e|a))i|i(?=(e|a))|y", "j"),
                    ("u(?=(a|e|i|o))", "w"),
                    ("à", "a"),
                    ("è", "ɛ"),
                    ("ì", "i"),
                    ("ò", "ɔ"),
                    ("ù", "u"),
                    ("c(?!=(e|i))|q", "k"),
                    ("\Bs\B", "z")
                ),
            "ro_RO":
                (
                    # Digraphs
                    ("ch(?=(e|i))", "k"),
                    ("g(?=(e|i))", "dʒ"),
                    ("c(?=(e|i))", "tʃ"),
                    ("(?<=(e|a))i|i(?=(e|a))|y", "j"),
                    ("n(?=(g|c|q))", "ŋ"),
                    ("gn", "ɲ"),
                    ("ț", "ts"),
                    ("ă", "ə"),
                    ("â|î", "ɨ"),
                    ("ș", "ʃ"),
                    ("j", "ʒ"),
                    ("ü", "y"),
                    ("e(?=(a|o))", "e̯)"),
                    ("o(?=a)", "o̯)"),
                    ("w", "v"),
                    ("c", "k")
                ),
            "fr_FR":
                (
                    # Exceptions
                    ("chanson", "ʃɑ̃sɔ"),
                    # Digraphs
                    ("ch", "ʃ"),
                    ("g(?=(e|é|è|i))", "ʒ"),
                    ("sc(?=(e|i))", "s"),
                    ("gl(?=(e|i))", "ʎ"),
                    ("gn", "ɲ"),
                    ("n(?=(g|c|q))", "ŋ"),
                    ("(c'*)(?=(e|i))", "s"),
                    ("zz", "z"),
                    ("\Bss\B", "s"),
                    # Consonants
                    # Vowels
                    ("i(?=(e|a))|y", "j"),
                    ("à", "a"),
                    ("è", "ɛ"),
                    ("ì", "i"),
                    ("ò", "ɔ"),
                    ("ù", "u"),
                    ("é", "e"),
                    ("c(?!=(e|i))|q", "k"),
                    ("r", "ʁ"),
                    ("\Bt(?=(i))\B", "s"),
                    ("ç", "s"),
                    ("â", "ɑ"),
                    ("oi", "wa"),
                    ("(ou|o|u)(?=(a|e|i|o))", "w"),
                    ("th", "t"),
                    ("kh", "k"),
                    ("ai|ei|ay", "ɛ"),
                    ("î", "i"),
                    ("eu|œ", "œ"),
                    ("ô|au|eau", "o"),
                    ("ou|oue", "u"),
                    ("u|û|ue", "y"),
                    # Nasal vowels
                    ("an|am|en|em|ean|aon", "ɑ̃"),
                    ("((a|e|i|y|ai|ei)(?=(n|m)))", "ɛ̃"),
                    ("un|um", "œ̃",),
                    ("on|om", "ɔ̃"),
                    #
                    (r"(m|n|t|p|s)+\b", "!"),
                    (r"(e\b)", ""),
                    ("\Bs\B", "z"),
                ),
            "pt_SI":
                (
                    # Consonants
                    # Digraphs
                    ("ch", "ʃ"),
                    ("g(?=(e|i))", "ʒ"),
                    ("gl(?=(e|i))", "ʎ"),
                    ("gn", "ɲ"),
                    ("n(?=(g|c|q))", "ŋ"),
                    ("(c'*)(?=(e|i))", "s"),
                    ("\Bss\B", "s"),
                    ("\Bs\B", "z"),
                    ("ç", "s"),
                    ("c(?!=(e|i))|q", "k"),
                    # Marginal consonants
                    ("i(?=(e|a))|y", "j"),
                    ("(ou|o|u)(?=(a|e|i|o))", "w"),
                    #
                    #
                    # Vowels
                    ("á", "a"),
                    ("â", "ɐ"),
                    ("é", "ɛ"),
                    ("í", "i"),
                    ("ó", "ɔ"),
                    ("ô", "o"),
                    (r"o\b", "u"),
                    ("ú", "u"),
                    ("é", "e"),
                    ("â", "ɑ"),
                    # Nasal vowels
                    ("[aâ][mn]|ã", "ɐ̃"),
                    ("[eê][mn]", "ẽ"),
                    ("[iî][mn]", "ĩ"),
                    ("[oô][mn]", "õ"),
                    ("[uû][mn]", "ũ"),
                    #
                ),
            "es_ES":
                (
                    # Consonants
                    # Digraphs
                    ("ch", "tʃ"),
                    (r"\bv", "b"),
                    ("\Bv\B", "β"),
                    ("gu(?=e)", "ɡ"),
                    ("y", "ʝ"),
                    ("ll", "ʎ"),
                    ("ñ", "ɲ"),
                    ("n(?=(g|c|q))", "ŋ"),
                    (r"\Br", "ɾ"),
                    (r"\Brr\B", "r"),
                    ("c(?=(e|i))|z", "θ"),
                    ("g(?=(e|i))|j", "x"),
                    # Semivowels
                    ("i(?=(a|e|u))", "j"),
                    ("u(?=(a|e|i|o))", "w"),
                ),
            "es_LA":
                (
                    # Consonants
                    # Digraphs
                    ("ch", "tʃ"),
                    (r"\bv", "b"),
                    ("\Bv\B", "β"),
                    ("gu(?=e)", "ɡ"),
                    ("g(?=n)", "ɣ"),
                    ("y", "ʝ"),
                    ("ll", "ʎ"),
                    ("ñ", "ɲ"),
                    ("n(?=(g|c|q))", "ŋ"),
                    (r"\Br", "ɾ"),
                    (r"\Brr\B", "r"),
                    ("c(?=(e|i))|z", "s"),
                    ("g(?=(e|i))|j", "x"),
                    # Semivowels
                    ("i(?=(a|e|u))", "j"),
                    ("u(?=(a|e|i|o))", "w"),
                ),
            "de_CH":
                (
                    # Consonants
                    (r"\bch", "k"),
                    ("(?<=(i|r|l))ch", "ç"),
                    ("ch", "x"),
                    ("(?<=(r|l))n", "ŋ"),
                    ("sch|s(?=(t|p))", "ʃ"),
                    ("\B(ss|ß)\B", "s"),
                    ("s", "z"),
                    ("th", "t"),
                    ("z|tz", "ts"),
                    ("tsch", "tʃ"),
                    ("w", "v"),

                    # Vowels
                    # Monophthongs
                    ("(?<=(a|e|i|o|u|ä|ö|ü))h", "ː"),
                    (r"ie", "iː"),
                    (r"in\b", "iːn"),
                    (r"e\b|e(?=(r|n)\b)", "ə"),
                    ("e(?=b)", "eː"),
                    ("e", "ɛ"),
                    ("i", "ɪ"),
                    ("o", "ɔ"),
                    ("o(?=b|d)", "oː"),
                    (r"\bö(?=(b|c|d|f|g|k|l|m|n|p|q|r|s|t|v|w|x|y|z))|\Bö\B", "œ"),
                    (r"\bö", "øː"),
                    (r"u(?=b|d|f|g|p|t|w)", "uː"),
                    (r"u", "ʊ"),

                    # Reduced vowels
                    ("ai|ei|ay|ey", "aɪ"),
                    ("au", "aʊ"),
                    ("eu|äu", "ɔɪ"),


                    ("ä", "ɛ"),
                    ("b(?=b)|d(?=d)|f(?=f)|c(?=k)|l(?=l)|m(?=m)|n(?=n)|p(?=p)|r(?=r)|s(?=s)|t(?=t)", "")
                )
        }
    ipaWord = ""
    word = word.casefold()
    matches = []
    from collections import OrderedDict
    langDict = OrderedDict(dictionary[language])
    for pattern in langDict:
        match = re.finditer(pattern, word)
        matches.extend(list(match))
    i = 0
    while (i <= len(word)-1):
        matchFound = False  #match whose start area index equals i
        for match in matches.copy():
            if match.start() == i:
                ipaWord += langDict[match.re.pattern]
                matches.remove(match)
                i = match.end()
                matchFound = True
                break # we can break here since the matches list is ordered by priority, thus not breaking results in duplicates
        if (not matchFound):
            ipaWord += word[i]
            i += 1
    # with open('IPADictionary_generated.json', encoding='utf-8', mode='w+') as outfile:
    #     json.dump(dictionary,outfile,ensure_ascii=False)
    return (ipaWord)

# print (getIPA("iată", "ro_RO"))
# print (getIPA("c'est", "fr_FR"))
# print (getIPA("c'è", "it_IT"))
# print (getIPA("casa", "it_IT"))
# print (getIPA("cassa", "it_IT"))
# print (getIPA("sasso", "it_IT"))
# print (getIPA("spune-mi", "ro_RO"))
# print (getIPA("canção", "pt_SI"))
# print (getIPA("chanson", "fr_FR"))
# print (getIPA("choisir", "fr_FR"))
# print (getIPA("vivir", "es_ES"))
print (getIPA("genial", "es_ES"))
print (getIPA("genial", "pt_SI"))
print (getIPA("génial", "fr_FR"))
print (getIPA("genial", "it_IT"))
print (getIPA("genial", "ro_RO"))
print (getIPA("ai","ro_RO"))
# print (getIPA("chamar", "pt_SI"))
#
# print (getIPA("chiema", "ro_RO"))
# print(getIPA("chanson", "fr_FR"))
#print(getIPA("abaisse ment", "fr_FR"))
# file = io.open("log.txt", mode="w", encoding="utf-8")
# output = (getIPA("abaissement", "fr_FR"))
# file.writelines(output)
# print (getIPA("demasiado","pt_SI"))
# print (getIPA("demasiado","es_ES"))
# print (getIPA("l'inferno","it_IT"))

print (getIPA("hoch","de_CH"))
print (getIPA("Chinese","de_CH"))
print (getIPA("Straßenbahnhaltestelle","de_CH"))
print (getIPA("Biene","de_CH"))
print (getIPA("Berlin","de_CH"))
print (getIPA("öffnen","de_CH"))
print (getIPA("Öl","de_CH"))
print (getIPA("Ö","de_CH"))
print (getIPA("ungenau","de_CH"))
print (getIPA("Äther","de_CH"))
print (getIPA("ähnlich","de_CH"))
print (getIPA("immer","de_CH"))
print (getIPA("zottelig","de_CH"))

