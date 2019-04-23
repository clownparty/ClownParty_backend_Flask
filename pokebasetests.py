#!/usr/bin/env python3

import pokebase as pb
import json, os, sys
import requests
import psycopg2


conn = psycopg2.connect(os.environ['DATABASE_URL'])
cur = conn.cursor()
sql = '''INSERT INTO pokemon(name, pokemonnumber, pokemondescription, pokemonimage)
         VALUES(%s, %s, %s, %s) returning id;'''

for i in range(1, 808):
    # grab pokemon from library
    pokemon = pb.pokemon(i)
    species = pb.pokemon_species(i)
    description = ""
    # check if always english
    for fte in species.flavor_text_entries:
        if fte.language.name =="en" and fte.version.name == "alpha-sapphire" or fte.language.name == "en" and fte.version.name == "ultra-sun":
            description = fte.flavor_text

    name = pokemon.name,
    pokemonnumber = pokemon.id,
    pokemondescription = description,
    pokemonimage = pokemon.sprites.front_default

    cur.execute(sql, (name, pokemonnumber, pokemondescription, pokemonimage,))
    conn.commit()

cur.close()
conn.close()

