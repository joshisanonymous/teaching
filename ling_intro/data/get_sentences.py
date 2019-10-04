# This is meant to generate sentences that I can use for syntax questions
import nltk
from nltk.corpus import brown, reuters
import re
import string
import random

# Get the raw text
brown_fiction = brown.raw(categories="fiction")

# Clean it up for modeling
linebreak = re.compile(r"\n")
tags = re.compile(r"\/[a-zA-Z]{2,4}\b")
punctuation = re.compile(f"[{string.punctuation}]")

brown_fiction = linebreak.sub(" ", brown_fiction)
brown_fiction = tags.sub("", brown_fiction)
brown_fiction = punctuation.sub("", brown_fiction)

# Generate
brown_fiction_Text = nltk.Text(brown_fiction.split())
brown_fiction_Text.generate(random_seed=random.randint(1,100))
