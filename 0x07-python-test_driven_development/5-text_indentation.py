#!/usr/bin/python3
"""
This is the "5-text_indentation" module
The 5-text_indentation module supplies one function, text_indentation(text).
"""

def text_indentation(text):
    """Indents a text"""
    result = []
    separator = ("?", ".", ":")
    new_word = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for ch in text:
        if new_word == "" and ch == " ":
            continue
        if ch not in separator:
            new_word += ch
        else:
            if new_word:
                new_word += ch
                print("{}\n".format(new_word))
                new_word = ""
                continue
        
    if new_word != "":
            print(new_word)
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
