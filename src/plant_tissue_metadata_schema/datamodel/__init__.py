from pathlib import Path
from .plant_tissue_metadata_schema import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "plant_tissue_metadata_schema.yaml"
