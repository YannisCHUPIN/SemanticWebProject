import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

def csv_to_rdf(csv_file, rdf_file):
    data = pd.read_csv(csv_file)
    g = Graph()

    GEONAMES = Namespace("https://www.geonames.org/ontology#")
    SCHEMA = Namespace("https://schema.org/")
    EX = Namespace("https://example.org/accident/")
    g.bind("ex", EX)

    for index, row in data.iterrows():
        accident_uri = EX[str(row['Identifiant_Accident'])]
        
        g.add((accident_uri, SCHEMA.identifier, Literal(row['Identifiant_Accident'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.speedLimit, Literal(row['Vitesse_Maximale_Autorisee'], datatype=XSD.float)))
        g.add((accident_uri, SCHEMA.day, Literal(row['jour'], datatype=XSD.integer)))
        g.add((accident_uri, SCHEMA.month, Literal(row['mois'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.year, Literal(row['Annee'], datatype=XSD.gYear)))
        g.add((accident_uri, SCHEMA.lighting, Literal(row['Luminosite'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.addressRegion, Literal(row['Departement'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.addressLocality, Literal(row['Commune'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.inCity, Literal(row['Agglomeration'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.weatherCondition, Literal(row['Connition_Atmospheriques'], datatype=XSD.string)))
        g.add((accident_uri, SCHEMA.streetAddress, Literal(row['adresse'], datatype=XSD.string)))

        latitude = row['Latitude']
        longitude = row['Longitude']
        if not pd.isna(latitude) and not pd.isna(longitude):
            g.add((accident_uri, GEONAMES.latitude, Literal(latitude, datatype=XSD.float)))
            g.add((accident_uri, GEONAMES.longitude, Literal(longitude, datatype=XSD.float)))


    g.serialize(destination=rdf_file, format="turtle")

csv_to_rdf('accidents.csv', 'accidents.ttl')
