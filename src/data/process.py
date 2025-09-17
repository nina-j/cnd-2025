from pathlib import Path
import polars as pl


def main() -> None:
    """Process UFO data

    We only want US data, and we want it normalized a bit for the demo.
    """
    data_dir = Path(__file__).parent / "files"
    csv_path = data_dir / "scrubbed.csv.gz"
    csv_data = pl.read_csv(csv_path, ignore_errors=True)

    us_data = csv_data.filter(pl.col("country") == "us").rename(str.strip)
    us_data = us_data.drop_nulls().head(1000)
    us_data = us_data.with_columns(pl.col("city").str.replace_all(r"\(.*\)", ""))
    us_data = us_data.with_columns(pl.col("city").str.strip_chars())
    us_data = us_data.with_columns(pl.col("comments").str.replace_all(r"(&#44)", ""))
    us_data = us_data.with_columns(pl.col("comments").str.strip_chars())
    us_data = us_data.rename(
        {
            "duration (seconds)": "duration_seconds",
            "duration (hours/min)": "duration_text",
            "date posted": "date_posted",
        }
    )

    locations = (
        us_data.select(["city", "state", "country", "latitude", "longitude"])
        .unique()
        .with_row_index("location_id", offset=1)
        .sort("location_id")
    )

    shapes = (
        us_data.select("shape")
        .filter(pl.col("shape").is_not_null())
        .unique()
        .with_row_index("shape_id", offset=1)
        .sort("shape_id")
    )

    sightings = (
        us_data.join(
            locations,
            on=["city", "state", "country"],
            how="left",
        )
        .join(shapes, on="shape", how="left")
        .select(
            [
                "datetime",
                "location_id",
                "shape_id",
                "duration_seconds",
                "duration_text",
                "comments",
                "date_posted",
            ]
        )
        .with_row_index("sighting_id", offset=1)
        .sort("sighting_id")
    )

    locations.write_csv(data_dir / "locations.csv")
    shapes.write_csv(data_dir / "shapes.csv")
    sightings.write_csv(data_dir / "sightings.csv")


if __name__ == "__main__":
    main()
