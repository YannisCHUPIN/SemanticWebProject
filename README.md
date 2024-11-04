# SemanticWebProject
## The current database contains the data of bodily accidents on France's roads and public space  between 2005 and 2022.

### A few words to understand the DataBase.

This DataBase is the result of the collection by France's Ministery of the Interior of the DATA dealing with bodily
accidents in the public space in France between 2005 and 2022. 

To measure its size here is a few numbers : 
 - 94 493 is how many drivers were involved in those accidents (this does not take into account all the passengers
referenced in the base, as well as pedestrians)
 - 68 refers how many attributes there are once the base is merged from a driver point of view. Note that some are
pivital while some are either poorly referenced such as secu1, secu2, secu3 or completely useless to the project.
Namely pr or pr1 are not interesting DATA to keep.

### Condensed description of Attributes.

| **Attribut**        | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| *Num\_Acc*          | Numéro d'identifiant de l'accident                                               |
| *jour mois*         | Jour de l'accident, mois de l'accident                                           |
| *an*                | Année de l'accident                                                             |
| *hrmn*              | Heure et minutes de l'accident                                                  |
| *lum*               | Conditions d'éclairage dans lesquelles l'accident s'est produit                 |
| *dep*               | Code INSEE du département                                                       |
| *agg*               | Localisation en agglomération                                                   |
| *int*               | Type d'intersection                                                            |
| *atm*               | Conditions atmosphériques                                                      |
| *col*               | Type de collision                                                              |
| *adr*               | Adresse postale (pour les accidents en agglomération)                          |
| *lat*               | Latitude                                                                       |
| *long*              | Longitude                                                                      |
| *catr*              | Catégorie de route                                                             |
| *voie*              | Numéro de la route                                                             |
| *circ*              | Régime de circulation                                                          |
| *nbv*               | Nombre total de voies de circulation                                           |
| *vosp*              | Présence d'une voie réservée                                                   |
| *prof*              | Profil en long de la route                                                     |
| *plan*              | Tracé en plan de la route                                                      |
| *surf*              | État de la surface de la route                                                 |
| *infra*             | Présence d'aménagements ou d'infrastructures                                   |
| *situ*              | Situation géographique de l'accident                                           |
| *vma*               | Vitesses maximale autorisées                                                   |
| *id\_vehicule*      | Identifiant du véhicule (clé étrangère)                                         |
| *catv*              | Catégorie du véhicule impliqué dans l'accident                                  |
| *obs*               | Type d'obstacle heurté                                                         |
| *obsm*              | Type d'obstacle mobile heurté                                                  |
| *choc*              | Point de choc initial                                                          |
| *manv*              | Manœuvre principale avant l'accident                                           |
| *catu*              | Catégorie d'usager (conducteur, passager, piéton)                              |
| *grav*              | Gravité de l'accident pour l'usager                                             |
| *sexe*              | Sexe de la personne                                                            |
| *trajet*            | Motif du déplacement au moment de l'accident                                   |


| **Attribut**        | **Description**                                                             |
|---------------------|-----------------------------------------------------------------------------|
| *id\_vehicule*      | Identifiant numérique unique du véhicule                                    |
| *num\_veh*          | Identifiant du véhicule pour associer les passagers du même véhicule         |
| *id\_usager*        | Identifiant des usagers dans la base                                        |
| *com*               | Numéro de commune (code INSEE)                                              |
| *adr*               | Adresse de l'accident                                                       |
| *lat*               | Latitude de l'accident                                                      |
| *long*              | Longitude de l'accident                                                     |
| *Num\_Acc*          | Numéro d'identifiant de l'accident                                           |
| *voie*              | Numéro de la route                                                          |
| *V1, V2*            | Numéro de la route                                                          |
| *vosp*              | Présence d'une voie réservée                                                |
| *pr, pr1*           | Numéro de borne et distance par rapport à celle-ci                          |
| *lartpc, larrout*   | Largeur du terre-plein central et de la chaussée                            |
| *senc*              | Sens de circulation                                                         |
| *manv*              | Manœuvre en cours lors de l'accident                                        |
| *motor*             | Motorisation du véhicule                                                    |
| *place*             | Place du passager dans l'habitacle                                          |
| *grav*              | Gravité de l'accident pour l'usager                                         |
| *sexe*              | Sexe de l'usager (binaire)                                                  |
| *secu1, secu2, secu3* | Utilisation d'équipements de sécurité                                    | 
| *locp, actp, etatp* | Localisation et action du piéton, accompagnement lors de l'accident         |
| *occutc*            | Nombre d'occupants du transport en commun                                   |
| *jour*              | Numéro du jour de l'accident                                                | 
| *hrmn*              | Heure et minutes                                                           |
| *an*                | Année de l'accident                                                         |
| *an\_nais*          | Année de naissance de l'usager                                              |

### Working SPARQL qwery 

#### On Accidents 
```SPARQL
PREFIX ns1: <https://www.geonames.org/ontology#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?accident ?accidentLat ?accidentLong
WHERE {
  # Dataset des accidents de voitures
  SERVICE <http://localhost:3030/Projet_Web_sem_accidents_voitures/sparql> {
    ?accident schema:identifier ?id;
              ns1:latitude ?accidentLat;
              ns1:longitude ?accidentLong.
  }
}
LIMIT 10
```

#### On powerplants
```SPARQL
PREFIX ns1: <https://www.geonames.org/ontology#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX ns2: <https://fuseki.nishyda.tech/ontology#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?powerPlant ?plantLat ?plantLong
WHERE {
  # Dataset des centrales électriques
  SERVICE <http://localhost:3030/dataset_Power_Plant/sparql> {
    ?powerPlant a ns2:PowerPlant;
                geo:lat ?plantLat;
                geo:long ?plantLong.
  }
}
LIMIT 10
```

#### On Airports
```SPARQL
PREFIX ns1: <https://www.geonames.org/ontology#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX ns2: <https://fuseki.nishyda.tech/ontology#>
PREFIX ns3: <http://sw-portal.deri.org/ontologies/swportal#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?airport ?airportLat ?airportLong
WHERE {
  # Dataset des aéroports
  SERVICE <http://localhost:3030/dataset_aeroport/sparql> {
    ?airport ns3:inCity ?city;
             geo:lat ?airportLat;
             geo:long ?airportLong.
  }
}
LIMIT 10
```


### Working SPARQL Federated qwery 

```SPARQL
PREFIX ns1: <https://www.geonames.org/ontology#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX ns2: <https://fuseki.nishyda.tech/ontology#>
PREFIX ns3: <http://sw-portal.deri.org/ontologies/swportal#>
PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?accidentLat ?accidentLong ?plantLat ?plantLong ?airportLat ?airportLong
WHERE {
  # Dataset des accidents de voitures
  SERVICE <http://localhost:3030/Projet_Web_sem_accidents_voitures/sparql> {
    ?accident schema:identifier ?id;
              ns1:latitude ?accidentLat;
              ns1:longitude ?accidentLong.
  }
  
  # Dataset des centrales électriques
  SERVICE <http://localhost:3030/dataset_Power_Plant/sparql> {
    ?powerPlant a ns2:PowerPlant;
                geo:lat ?plantLat;
                geo:long ?plantLong.
  }
  
  # Dataset des aéroports
  SERVICE <http://localhost:3030/dataset_aeroport/sparql> {
    ?airport ns3:inCity ?city;
             geo:lat ?airportLat;
             geo:lat ?airportLong.
  }
  
  # Condition de proximité basée sur la distance géographique (simplifiée)
  #FILTER(
  #  (ABS(?accidentLat - ?plantLat) < 1 && ABS(?accidentLong - ?plantLong) < 1) ||
  #  (ABS(?accidentLat - ?airportLat) < 1 && ABS(?accidentLong - ?airportLong) < 1)
  #)

}
limit 10
```