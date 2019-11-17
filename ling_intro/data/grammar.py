# An example of the grammar proposed when we cover syntax

# Syntactic categories
grammar = """
S -> NP VP
NP -> N | Det N | Adj N | N PP
VP -> V | V NP | V AP | V PP
PP -> P NP
AP -> Adj | Adv Adj
"""

# Lexical categories
lexicon = """
N -> 'dog' | 'house' | 'gumbo' | 'I' | 'elephant' | 'pajamas'
Det -> 'the' | 'a' | 'an' | 'my'
V -> 'run' | 'leave' | 'eat' | 'shot'
P -> 'to' | 'from' | 'with' | 'in'
Adj -> 'tall' | 'small' | 'green'
Adv -> 'very' | 'really'
"""
