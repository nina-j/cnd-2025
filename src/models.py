import re
from datetime import datetime, timezone
from typing import Annotated, Any

from pydantic import AwareDatetime, BaseModel, BeforeValidator, ConfigDict


def parse_datetime(v: Any) -> Any:
    if isinstance(v, str):
        v = re.sub(r"24:00$", "00:00", v)
        v = datetime.strptime(v, "%m/%d/%Y %H:%M")
        v = v.replace(tzinfo=timezone.utc)

    return v


def parse_unknown(v: Any) -> Any:
    if isinstance(v, str) and v.lower() == "unknown":
        return None
    return float(v)


class Base(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_assignment=True,
    )


class LocationCsv(Base):
    location_id: int
    city: str
    state: str
    latitude: float
    longitude: float


class ShapeCsv(Base):
    shape_id: int
    shape: str


class SightingCsv(Base):
    sighting_id: int
    location_id: int
    shape_id: int
    datetime: Annotated[AwareDatetime, BeforeValidator(parse_datetime)]
    duration_seconds: int
    comments: str


class NasaSightingCsv(Base):
    case_id: str
    datetime: Annotated[AwareDatetime, BeforeValidator(parse_datetime)]
    location_id: int
    shape_id: int
    classification: str
    radar_confirmed: bool
    credibility_score: float
    threat_level: str
    investigation_status: str
    assigned_agent: str
    radiation_detected: bool
    electromagnetic_anomaly: bool
    altitude_est_meters: Annotated[int | None, BeforeValidator(parse_unknown)]
    speed_est_kmh: Annotated[int | None, BeforeValidator(parse_unknown)]
    witness_count: int
    military_witness: bool
    photos_collected: int
    samples_collected: int
    notes: str


class Sighting(Base):
    sighting_id: int
    comments: str


class NasaSighting(Base):
    case_id: str
    credibility_score: float
    altitude_est_meters: int
    notes: str


class RelatedSightings(Base):
    private_sighting: Sighting
    nasa_sighting: NasaSighting
    datetime: AwareDatetime
    shape: str
