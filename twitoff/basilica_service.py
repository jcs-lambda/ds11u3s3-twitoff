"""Basilica service."""

import os

import basilica
from dotenv import load_dotenv

# establish environment
assert load_dotenv(), 'failed to initialize environment'
BASILICA_KEY = os.getenv('BASILICA_KEY')
assert BASILICA_KEY is not None, \
    'falied to load BASILICA_KEY from environment'


def basilica_api():
    return basilica.Connection(BASILICA_KEY)


if __name__ == '__main__':
    with basilica_api() as c:
        sentences = ["Hello world!", "How are you?"]
        embeddings = c.embed_sentences(sentences)
        print(type(embeddings))
        for embedding in embeddings:
            print(type(embedding), len(embedding))
            print(embedding)
            print()
