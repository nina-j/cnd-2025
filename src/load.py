from pathlib import Path

import polars as pl
from neo4j import GraphDatabase, ManagedTransaction
from pydantic import TypeAdapter

from models import LocationCsv, NasaSightingCsv, ShapeCsv, SightingCsv
from settings import Settings


def read_files(
    name: str,
) -> pl.DataFrame:
    data_dir = Path(__file__).parent / "files"
    return pl.read_csv(data_dir / f"{name}.csv")


def load_locations(tx: ManagedTransaction) -> None:
    locations = TypeAdapter(list[LocationCsv]).validate_python(
        read_files("locations").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $locations AS location
        MERGE (l:Location {location_id: location.location_id})
        SET l += location
        """,
        locations=[location.model_dump() for location in locations],
    )


def load_shapes(tx: ManagedTransaction) -> None:
    shapes = TypeAdapter(list[ShapeCsv]).validate_python(
        read_files("shapes").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $shapes AS shape
        MERGE (s:Shape {shape_id: shape.shape_id})
        SET s += shape
        """,
        shapes=[shape.model_dump() for shape in shapes],
    )


def load_sightings(tx: ManagedTransaction) -> None:
    sightings = TypeAdapter(list[SightingCsv]).validate_python(
        read_files("sightings").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $sightings AS sighting
        MERGE (s:Sighting {sighting_id: sighting.sighting_id})
        SET s.comments = sighting.comments

        MERGE (dt: ObservationTime {value: sighting.datetime})
        MERGE (dur: Duration {value: sighting.duration_seconds})

        WITH *

        MATCH (l:Location {location_id: sighting.location_id})
        MATCH (sh:Shape {shape_id: sighting.shape_id})
        MERGE (s)-[:ON_LOCATION]->(l)
        MERGE (s)-[:FOR_DURATION]->(dur)
        MERGE (s)-[:OBSERVED_AT]->(dt)
        MERGE (s)-[:HAS_SHAPE]->(sh)
        """,
        sightings=[sighting.model_dump() for sighting in sightings],
    )


def load_nasa_sightings(tx: ManagedTransaction) -> None:
    nasa_sightings = TypeAdapter(list[NasaSightingCsv]).validate_python(
        read_files("nasa_sightings").to_dicts()
    )
    tx.run(
        """//cypher
        UNWIND $nasa_sightings AS nasa_sighting
        MERGE (ns:NasaSighting {case_id: nasa_sighting.case_id})
        SET ns.credibility_score = nasa_sighting.credibility_score
        SET ns.altitude_est_meters = nasa_sighting.altitude_est_meters
        SET ns.notes = nasa_sighting.notes

        MERGE (dt: ObservationTime {value: nasa_sighting.datetime})
        MERGE (cl: Classification {value: nasa_sighting.classification})
        MERGE (tl: ThreatLevel {value: nasa_sighting.threat_level})
        MERGE (invs: InvestigationStatus {value: nasa_sighting.investigation_status})

        WITH *

        MATCH (l:Location {location_id: nasa_sighting.location_id})
        MATCH (s:Shape {shape_id: nasa_sighting.shape_id})
        MERGE (ns)-[:ON_LOCATION]->(l)
        MERGE (ns)-[:OBSERVED_AT]->(dt)
        MERGE (ns)-[:HAS_SHAPE]->(s)
        MERGE (ns)-[:HAS_CLASSIFICATION]->(cl)
        MERGE (ns)-[:HAS_THREAT_LEVEL]->(tl)
        MERGE (ns)-[:HAS_INVESTIGATION_STATUS]->(invs)
        """,
        nasa_sightings=[nasa_sighting.model_dump() for nasa_sighting in nasa_sightings],
    )


def main() -> None:
    settings = Settings()
    driver = GraphDatabase.driver(
        settings.neo4j_uri,
        auth=(settings.neo4j_user, settings.neo4j_password.get_secret_value()),
    )
    with driver.session() as session:
        session.execute_write(load_locations)
        session.execute_write(load_shapes)
        session.execute_write(load_sightings)
        session.execute_write(load_nasa_sightings)


if __name__ == "__main__":
    main()
