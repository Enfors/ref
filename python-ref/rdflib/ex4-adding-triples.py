#!/usr/bin/env python3

"""
A simple example from 
https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html.
"""

from rdflib import URIRef, BNode, Literal

# Creating nodes:
bob = URIRef("http://example.org/people/Bob")
linda = BNode() # a GUID is generated. BNode = blank node

name = Literal("Bob") # passing a string
age = Literal(24) # passing a python int
height = Literal(76.5) # passing a python float

# To create many URIRefs in the same namespace, that is, URIs with the
# same prefix, RDFLib has the rdflib.namespace.Namespace class:

from rdflib import Namespace

n = Namespace("http://example.org/people/")
n.bob # = rdflib.term.URIRef(u"http://example.org/people/bob")
n.eve # = rdflib.term.URIRef(u"http://example.org/people/eve")

# This is very useful for schemas where all properties and classes
# have the same URI prefix, RDFLib pre-defines Namespaces for the most
# common RDF schemas:

from rdflib.namespace import RDF, FOAF

RDF.type
# = rdflib.term.URIRef(u"http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

FOAF.knows
# = rdflib.term.URIRef(u"http://xmlns.com/foaf/0.1/knows")

from rdflib import Graph
g = Graph()

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

output = g.serialize(format="turtle").decode("UTF-8")
print(output.replace("\\n", "\n"))
