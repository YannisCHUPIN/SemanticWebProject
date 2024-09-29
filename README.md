# SemanticWebProject
## The current database contains the data of bodily accidents on France's roads and public space  between 2005 and 2022.

### Les attributs de la base 

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
| *sexe*              | Sexe du conducteur                                                             |
| *trajet*            | Motif du déplacement au moment de l'accident                                   |
| *mortal*            | Indique si le véhicule est impliqué dans un accident mortel (calculé dans le notebook) |


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
