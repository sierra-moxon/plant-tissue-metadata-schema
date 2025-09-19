# Auto generated from plant_tissue_metadata_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-19T13:42:47
# Schema: plant-tissue-metadata-schema
#
# id: https://w3id.org/plant-tissue-metadata-schema
# description: A LinkML schema for capturing metadata about plant tissue samples, including experimental conditions,
#   treatments, and sample processing information. Designed for compatibility with MIXS standards.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
ORCID = CurieNamespace('ORCID', 'http://identifiers.org/orcid/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/mixs/')
PLANT_TISSUE = CurieNamespace('plant_tissue', 'https://w3id.org/plant-tissue-metadata-schema/')
DEFAULT_ = PLANT_TISSUE


# Types

# Class references



@dataclass(repr=False)
class PlantTissueSample(YAMLRoot):
    """
    A sample of plant tissue with associated metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PLANT_TISSUE["PlantTissueSample"]
    class_class_curie: ClassVar[str] = "plant_tissue:PlantTissueSample"
    class_name: ClassVar[str] = "PlantTissueSample"
    class_model_uri: ClassVar[URIRef] = PLANT_TISSUE.PlantTissueSample

    seq_project_id: int = None
    seq_project_name: str = None
    sample_id: int = None
    seq_project_pi_name: str = None
    tube_or_plate_label: str = None
    sample_container: str = None
    plate_location: str = None
    biosafety_material_category: str = None
    sample_name: str = None
    genus: str = None
    species: str = None
    strain_variety_or_cultivar: str = None
    ncbi_taxonomy_id: int = None
    reference_genome: str = None
    collection_date_and_time: str = None
    sample_size: str = None
    tissue: str = None
    growth_facility: str = None
    growth_medium: str = None
    plant_age: str = None
    developmental_stage: str = None
    sample_storage_temperature_celsius: str = None
    sample_preservation_method: str = None
    sample_contact_name: Optional[str] = None
    tissue_contact_name: Optional[str] = None
    proposal_id: Optional[int] = None
    biological_replicate_sample_group_name: Optional[str] = None
    combined_tissue_description: Optional[str] = None
    experimental_time_point_number: Optional[int] = None
    experimental_time_point_description: Optional[str] = None
    isolate: Optional[str] = None
    germplasm_collection_and_id: Optional[str] = None
    ancestral_data: Optional[str] = None
    genetic_modification: Optional[str] = None
    estimated_genome_size_mb: Optional[int] = None
    gc_content_percent: Optional[int] = None
    ploidy: Optional[str] = None
    tissue_plant_ontology_term: Optional[str] = None
    geographic_location_region_and_locality: Optional[str] = None
    geographic_location_latitude: Optional[float] = None
    geographic_location_longitude: Optional[float] = None
    depth_meters: Optional[str] = None
    elevation_meters: Optional[str] = None
    temperature_celsius: Optional[str] = None
    broad_scale_environmental_context: Optional[str] = None
    local_environmental_context: Optional[str] = None
    environmental_medium: Optional[str] = None
    growth_medium_composition: Optional[str] = None
    air_temperature_regimen: Optional[str] = None
    antibiotic_regimen: Optional[str] = None
    biotic_regimen: Optional[str] = None
    inoculation_method: Optional[str] = None
    time_post_inoculation: Optional[str] = None
    chemical_administration: Optional[str] = None
    chemical_mutagen: Optional[str] = None
    fertilizer_administration: Optional[str] = None
    insecticide_regimen: Optional[str] = None
    fungicide_regimen: Optional[str] = None
    gaseous_environment: Optional[str] = None
    growth_hormone_regimen: Optional[str] = None
    herbicide_regimen: Optional[str] = None
    humidity_regimen: Optional[str] = None
    radiation_regimen: Optional[str] = None
    light_regimen: Optional[str] = None
    last_light_transition_type: Optional[str] = None
    time_after_last_light_transition: Optional[str] = None
    salt_regimen: Optional[str] = None
    rainfall_regimen: Optional[str] = None
    watering_regimen: Optional[str] = None
    other_treatment_regimen: Optional[str] = None
    perturbation: Optional[str] = None
    mechanical_damage: Optional[str] = None
    observed_host_symbionts: Optional[str] = None
    plant_sex: Optional[str] = None
    sample_disease_status: Optional[str] = None
    sample_disease_stage: Optional[str] = None
    sample_material_processing: Optional[str] = None
    harvest_to_preservation_time: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.seq_project_id):
            self.MissingRequiredField("seq_project_id")
        if not isinstance(self.seq_project_id, int):
            self.seq_project_id = int(self.seq_project_id)

        if self._is_empty(self.seq_project_name):
            self.MissingRequiredField("seq_project_name")
        if not isinstance(self.seq_project_name, str):
            self.seq_project_name = str(self.seq_project_name)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, int):
            self.sample_id = int(self.sample_id)

        if self._is_empty(self.seq_project_pi_name):
            self.MissingRequiredField("seq_project_pi_name")
        if not isinstance(self.seq_project_pi_name, str):
            self.seq_project_pi_name = str(self.seq_project_pi_name)

        if self._is_empty(self.tube_or_plate_label):
            self.MissingRequiredField("tube_or_plate_label")
        if not isinstance(self.tube_or_plate_label, str):
            self.tube_or_plate_label = str(self.tube_or_plate_label)

        if self._is_empty(self.sample_container):
            self.MissingRequiredField("sample_container")
        if not isinstance(self.sample_container, str):
            self.sample_container = str(self.sample_container)

        if self._is_empty(self.plate_location):
            self.MissingRequiredField("plate_location")
        if not isinstance(self.plate_location, str):
            self.plate_location = str(self.plate_location)

        if self._is_empty(self.biosafety_material_category):
            self.MissingRequiredField("biosafety_material_category")
        if not isinstance(self.biosafety_material_category, str):
            self.biosafety_material_category = str(self.biosafety_material_category)

        if self._is_empty(self.sample_name):
            self.MissingRequiredField("sample_name")
        if not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self._is_empty(self.genus):
            self.MissingRequiredField("genus")
        if not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self._is_empty(self.species):
            self.MissingRequiredField("species")
        if not isinstance(self.species, str):
            self.species = str(self.species)

        if self._is_empty(self.strain_variety_or_cultivar):
            self.MissingRequiredField("strain_variety_or_cultivar")
        if not isinstance(self.strain_variety_or_cultivar, str):
            self.strain_variety_or_cultivar = str(self.strain_variety_or_cultivar)

        if self._is_empty(self.ncbi_taxonomy_id):
            self.MissingRequiredField("ncbi_taxonomy_id")
        if not isinstance(self.ncbi_taxonomy_id, int):
            self.ncbi_taxonomy_id = int(self.ncbi_taxonomy_id)

        if self._is_empty(self.reference_genome):
            self.MissingRequiredField("reference_genome")
        if not isinstance(self.reference_genome, str):
            self.reference_genome = str(self.reference_genome)

        if self._is_empty(self.collection_date_and_time):
            self.MissingRequiredField("collection_date_and_time")
        if not isinstance(self.collection_date_and_time, str):
            self.collection_date_and_time = str(self.collection_date_and_time)

        if self._is_empty(self.sample_size):
            self.MissingRequiredField("sample_size")
        if not isinstance(self.sample_size, str):
            self.sample_size = str(self.sample_size)

        if self._is_empty(self.tissue):
            self.MissingRequiredField("tissue")
        if not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

        if self._is_empty(self.growth_facility):
            self.MissingRequiredField("growth_facility")
        if not isinstance(self.growth_facility, str):
            self.growth_facility = str(self.growth_facility)

        if self._is_empty(self.growth_medium):
            self.MissingRequiredField("growth_medium")
        if not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self._is_empty(self.plant_age):
            self.MissingRequiredField("plant_age")
        if not isinstance(self.plant_age, str):
            self.plant_age = str(self.plant_age)

        if self._is_empty(self.developmental_stage):
            self.MissingRequiredField("developmental_stage")
        if not isinstance(self.developmental_stage, str):
            self.developmental_stage = str(self.developmental_stage)

        if self._is_empty(self.sample_storage_temperature_celsius):
            self.MissingRequiredField("sample_storage_temperature_celsius")
        if not isinstance(self.sample_storage_temperature_celsius, str):
            self.sample_storage_temperature_celsius = str(self.sample_storage_temperature_celsius)

        if self._is_empty(self.sample_preservation_method):
            self.MissingRequiredField("sample_preservation_method")
        if not isinstance(self.sample_preservation_method, str):
            self.sample_preservation_method = str(self.sample_preservation_method)

        if self.sample_contact_name is not None and not isinstance(self.sample_contact_name, str):
            self.sample_contact_name = str(self.sample_contact_name)

        if self.tissue_contact_name is not None and not isinstance(self.tissue_contact_name, str):
            self.tissue_contact_name = str(self.tissue_contact_name)

        if self.proposal_id is not None and not isinstance(self.proposal_id, int):
            self.proposal_id = int(self.proposal_id)

        if self.biological_replicate_sample_group_name is not None and not isinstance(self.biological_replicate_sample_group_name, str):
            self.biological_replicate_sample_group_name = str(self.biological_replicate_sample_group_name)

        if self.combined_tissue_description is not None and not isinstance(self.combined_tissue_description, str):
            self.combined_tissue_description = str(self.combined_tissue_description)

        if self.experimental_time_point_number is not None and not isinstance(self.experimental_time_point_number, int):
            self.experimental_time_point_number = int(self.experimental_time_point_number)

        if self.experimental_time_point_description is not None and not isinstance(self.experimental_time_point_description, str):
            self.experimental_time_point_description = str(self.experimental_time_point_description)

        if self.isolate is not None and not isinstance(self.isolate, str):
            self.isolate = str(self.isolate)

        if self.germplasm_collection_and_id is not None and not isinstance(self.germplasm_collection_and_id, str):
            self.germplasm_collection_and_id = str(self.germplasm_collection_and_id)

        if self.ancestral_data is not None and not isinstance(self.ancestral_data, str):
            self.ancestral_data = str(self.ancestral_data)

        if self.genetic_modification is not None and not isinstance(self.genetic_modification, str):
            self.genetic_modification = str(self.genetic_modification)

        if self.estimated_genome_size_mb is not None and not isinstance(self.estimated_genome_size_mb, int):
            self.estimated_genome_size_mb = int(self.estimated_genome_size_mb)

        if self.gc_content_percent is not None and not isinstance(self.gc_content_percent, int):
            self.gc_content_percent = int(self.gc_content_percent)

        if self.ploidy is not None and not isinstance(self.ploidy, str):
            self.ploidy = str(self.ploidy)

        if self.tissue_plant_ontology_term is not None and not isinstance(self.tissue_plant_ontology_term, str):
            self.tissue_plant_ontology_term = str(self.tissue_plant_ontology_term)

        if self.geographic_location_region_and_locality is not None and not isinstance(self.geographic_location_region_and_locality, str):
            self.geographic_location_region_and_locality = str(self.geographic_location_region_and_locality)

        if self.geographic_location_latitude is not None and not isinstance(self.geographic_location_latitude, float):
            self.geographic_location_latitude = float(self.geographic_location_latitude)

        if self.geographic_location_longitude is not None and not isinstance(self.geographic_location_longitude, float):
            self.geographic_location_longitude = float(self.geographic_location_longitude)

        if self.depth_meters is not None and not isinstance(self.depth_meters, str):
            self.depth_meters = str(self.depth_meters)

        if self.elevation_meters is not None and not isinstance(self.elevation_meters, str):
            self.elevation_meters = str(self.elevation_meters)

        if self.temperature_celsius is not None and not isinstance(self.temperature_celsius, str):
            self.temperature_celsius = str(self.temperature_celsius)

        if self.broad_scale_environmental_context is not None and not isinstance(self.broad_scale_environmental_context, str):
            self.broad_scale_environmental_context = str(self.broad_scale_environmental_context)

        if self.local_environmental_context is not None and not isinstance(self.local_environmental_context, str):
            self.local_environmental_context = str(self.local_environmental_context)

        if self.environmental_medium is not None and not isinstance(self.environmental_medium, str):
            self.environmental_medium = str(self.environmental_medium)

        if self.growth_medium_composition is not None and not isinstance(self.growth_medium_composition, str):
            self.growth_medium_composition = str(self.growth_medium_composition)

        if self.air_temperature_regimen is not None and not isinstance(self.air_temperature_regimen, str):
            self.air_temperature_regimen = str(self.air_temperature_regimen)

        if self.antibiotic_regimen is not None and not isinstance(self.antibiotic_regimen, str):
            self.antibiotic_regimen = str(self.antibiotic_regimen)

        if self.biotic_regimen is not None and not isinstance(self.biotic_regimen, str):
            self.biotic_regimen = str(self.biotic_regimen)

        if self.inoculation_method is not None and not isinstance(self.inoculation_method, str):
            self.inoculation_method = str(self.inoculation_method)

        if self.time_post_inoculation is not None and not isinstance(self.time_post_inoculation, str):
            self.time_post_inoculation = str(self.time_post_inoculation)

        if self.chemical_administration is not None and not isinstance(self.chemical_administration, str):
            self.chemical_administration = str(self.chemical_administration)

        if self.chemical_mutagen is not None and not isinstance(self.chemical_mutagen, str):
            self.chemical_mutagen = str(self.chemical_mutagen)

        if self.fertilizer_administration is not None and not isinstance(self.fertilizer_administration, str):
            self.fertilizer_administration = str(self.fertilizer_administration)

        if self.insecticide_regimen is not None and not isinstance(self.insecticide_regimen, str):
            self.insecticide_regimen = str(self.insecticide_regimen)

        if self.fungicide_regimen is not None and not isinstance(self.fungicide_regimen, str):
            self.fungicide_regimen = str(self.fungicide_regimen)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.growth_hormone_regimen is not None and not isinstance(self.growth_hormone_regimen, str):
            self.growth_hormone_regimen = str(self.growth_hormone_regimen)

        if self.herbicide_regimen is not None and not isinstance(self.herbicide_regimen, str):
            self.herbicide_regimen = str(self.herbicide_regimen)

        if self.humidity_regimen is not None and not isinstance(self.humidity_regimen, str):
            self.humidity_regimen = str(self.humidity_regimen)

        if self.radiation_regimen is not None and not isinstance(self.radiation_regimen, str):
            self.radiation_regimen = str(self.radiation_regimen)

        if self.light_regimen is not None and not isinstance(self.light_regimen, str):
            self.light_regimen = str(self.light_regimen)

        if self.last_light_transition_type is not None and not isinstance(self.last_light_transition_type, str):
            self.last_light_transition_type = str(self.last_light_transition_type)

        if self.time_after_last_light_transition is not None and not isinstance(self.time_after_last_light_transition, str):
            self.time_after_last_light_transition = str(self.time_after_last_light_transition)

        if self.salt_regimen is not None and not isinstance(self.salt_regimen, str):
            self.salt_regimen = str(self.salt_regimen)

        if self.rainfall_regimen is not None and not isinstance(self.rainfall_regimen, str):
            self.rainfall_regimen = str(self.rainfall_regimen)

        if self.watering_regimen is not None and not isinstance(self.watering_regimen, str):
            self.watering_regimen = str(self.watering_regimen)

        if self.other_treatment_regimen is not None and not isinstance(self.other_treatment_regimen, str):
            self.other_treatment_regimen = str(self.other_treatment_regimen)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.mechanical_damage is not None and not isinstance(self.mechanical_damage, str):
            self.mechanical_damage = str(self.mechanical_damage)

        if self.observed_host_symbionts is not None and not isinstance(self.observed_host_symbionts, str):
            self.observed_host_symbionts = str(self.observed_host_symbionts)

        if self.plant_sex is not None and not isinstance(self.plant_sex, str):
            self.plant_sex = str(self.plant_sex)

        if self.sample_disease_status is not None and not isinstance(self.sample_disease_status, str):
            self.sample_disease_status = str(self.sample_disease_status)

        if self.sample_disease_stage is not None and not isinstance(self.sample_disease_stage, str):
            self.sample_disease_stage = str(self.sample_disease_stage)

        if self.sample_material_processing is not None and not isinstance(self.sample_material_processing, str):
            self.sample_material_processing = str(self.sample_material_processing)

        if self.harvest_to_preservation_time is not None and not isinstance(self.harvest_to_preservation_time, str):
            self.harvest_to_preservation_time = str(self.harvest_to_preservation_time)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.seq_project_id = Slot(uri=PLANT_TISSUE.seq_project_id, name="seq_project_id", curie=PLANT_TISSUE.curie('seq_project_id'),
                   model_uri=PLANT_TISSUE.seq_project_id, domain=None, range=int)

slots.seq_project_name = Slot(uri=PLANT_TISSUE.seq_project_name, name="seq_project_name", curie=PLANT_TISSUE.curie('seq_project_name'),
                   model_uri=PLANT_TISSUE.seq_project_name, domain=None, range=str)

slots.sample_id = Slot(uri=PLANT_TISSUE.sample_id, name="sample_id", curie=PLANT_TISSUE.curie('sample_id'),
                   model_uri=PLANT_TISSUE.sample_id, domain=None, range=int)

slots.seq_project_pi_name = Slot(uri=PLANT_TISSUE.seq_project_pi_name, name="seq_project_pi_name", curie=PLANT_TISSUE.curie('seq_project_pi_name'),
                   model_uri=PLANT_TISSUE.seq_project_pi_name, domain=None, range=str)

slots.sample_contact_name = Slot(uri=PLANT_TISSUE.sample_contact_name, name="sample_contact_name", curie=PLANT_TISSUE.curie('sample_contact_name'),
                   model_uri=PLANT_TISSUE.sample_contact_name, domain=None, range=Optional[str])

slots.tissue_contact_name = Slot(uri=PLANT_TISSUE.tissue_contact_name, name="tissue_contact_name", curie=PLANT_TISSUE.curie('tissue_contact_name'),
                   model_uri=PLANT_TISSUE.tissue_contact_name, domain=None, range=Optional[str])

slots.proposal_id = Slot(uri=PLANT_TISSUE.proposal_id, name="proposal_id", curie=PLANT_TISSUE.curie('proposal_id'),
                   model_uri=PLANT_TISSUE.proposal_id, domain=None, range=Optional[int])

slots.tube_or_plate_label = Slot(uri=PLANT_TISSUE.tube_or_plate_label, name="tube_or_plate_label", curie=PLANT_TISSUE.curie('tube_or_plate_label'),
                   model_uri=PLANT_TISSUE.tube_or_plate_label, domain=None, range=str)

slots.sample_container = Slot(uri=PLANT_TISSUE.sample_container, name="sample_container", curie=PLANT_TISSUE.curie('sample_container'),
                   model_uri=PLANT_TISSUE.sample_container, domain=None, range=str)

slots.plate_location = Slot(uri=PLANT_TISSUE.plate_location, name="plate_location", curie=PLANT_TISSUE.curie('plate_location'),
                   model_uri=PLANT_TISSUE.plate_location, domain=None, range=str)

slots.biosafety_material_category = Slot(uri=PLANT_TISSUE.biosafety_material_category, name="biosafety_material_category", curie=PLANT_TISSUE.curie('biosafety_material_category'),
                   model_uri=PLANT_TISSUE.biosafety_material_category, domain=None, range=str)

slots.sample_name = Slot(uri=PLANT_TISSUE.sample_name, name="sample_name", curie=PLANT_TISSUE.curie('sample_name'),
                   model_uri=PLANT_TISSUE.sample_name, domain=None, range=str)

slots.biological_replicate_sample_group_name = Slot(uri=PLANT_TISSUE.biological_replicate_sample_group_name, name="biological_replicate_sample_group_name", curie=PLANT_TISSUE.curie('biological_replicate_sample_group_name'),
                   model_uri=PLANT_TISSUE.biological_replicate_sample_group_name, domain=None, range=Optional[str])

slots.combined_tissue_description = Slot(uri=PLANT_TISSUE.combined_tissue_description, name="combined_tissue_description", curie=PLANT_TISSUE.curie('combined_tissue_description'),
                   model_uri=PLANT_TISSUE.combined_tissue_description, domain=None, range=Optional[str])

slots.experimental_time_point_number = Slot(uri=PLANT_TISSUE.experimental_time_point_number, name="experimental_time_point_number", curie=PLANT_TISSUE.curie('experimental_time_point_number'),
                   model_uri=PLANT_TISSUE.experimental_time_point_number, domain=None, range=Optional[int])

slots.experimental_time_point_description = Slot(uri=PLANT_TISSUE.experimental_time_point_description, name="experimental_time_point_description", curie=PLANT_TISSUE.curie('experimental_time_point_description'),
                   model_uri=PLANT_TISSUE.experimental_time_point_description, domain=None, range=Optional[str])

slots.genus = Slot(uri=PLANT_TISSUE.genus, name="genus", curie=PLANT_TISSUE.curie('genus'),
                   model_uri=PLANT_TISSUE.genus, domain=None, range=str)

slots.species = Slot(uri=PLANT_TISSUE.species, name="species", curie=PLANT_TISSUE.curie('species'),
                   model_uri=PLANT_TISSUE.species, domain=None, range=str)

slots.strain_variety_or_cultivar = Slot(uri=PLANT_TISSUE.strain_variety_or_cultivar, name="strain_variety_or_cultivar", curie=PLANT_TISSUE.curie('strain_variety_or_cultivar'),
                   model_uri=PLANT_TISSUE.strain_variety_or_cultivar, domain=None, range=str)

slots.isolate = Slot(uri=PLANT_TISSUE.isolate, name="isolate", curie=PLANT_TISSUE.curie('isolate'),
                   model_uri=PLANT_TISSUE.isolate, domain=None, range=Optional[str])

slots.germplasm_collection_and_id = Slot(uri=PLANT_TISSUE.germplasm_collection_and_id, name="germplasm_collection_and_id", curie=PLANT_TISSUE.curie('germplasm_collection_and_id'),
                   model_uri=PLANT_TISSUE.germplasm_collection_and_id, domain=None, range=Optional[str])

slots.ncbi_taxonomy_id = Slot(uri=PLANT_TISSUE.ncbi_taxonomy_id, name="ncbi_taxonomy_id", curie=PLANT_TISSUE.curie('ncbi_taxonomy_id'),
                   model_uri=PLANT_TISSUE.ncbi_taxonomy_id, domain=None, range=int)

slots.ancestral_data = Slot(uri=PLANT_TISSUE.ancestral_data, name="ancestral_data", curie=PLANT_TISSUE.curie('ancestral_data'),
                   model_uri=PLANT_TISSUE.ancestral_data, domain=None, range=Optional[str])

slots.genetic_modification = Slot(uri=PLANT_TISSUE.genetic_modification, name="genetic_modification", curie=PLANT_TISSUE.curie('genetic_modification'),
                   model_uri=PLANT_TISSUE.genetic_modification, domain=None, range=Optional[str],
                   pattern=re.compile(r'^{PMID}|{DOI}|{URL}$'))

slots.estimated_genome_size_mb = Slot(uri=PLANT_TISSUE.estimated_genome_size_mb, name="estimated_genome_size_mb", curie=PLANT_TISSUE.curie('estimated_genome_size_mb'),
                   model_uri=PLANT_TISSUE.estimated_genome_size_mb, domain=None, range=Optional[int])

slots.gc_content_percent = Slot(uri=PLANT_TISSUE.gc_content_percent, name="gc_content_percent", curie=PLANT_TISSUE.curie('gc_content_percent'),
                   model_uri=PLANT_TISSUE.gc_content_percent, domain=None, range=Optional[int])

slots.ploidy = Slot(uri=PLANT_TISSUE.ploidy, name="ploidy", curie=PLANT_TISSUE.curie('ploidy'),
                   model_uri=PLANT_TISSUE.ploidy, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$'))

slots.reference_genome = Slot(uri=PLANT_TISSUE.reference_genome, name="reference_genome", curie=PLANT_TISSUE.curie('reference_genome'),
                   model_uri=PLANT_TISSUE.reference_genome, domain=None, range=str)

slots.collection_date_and_time = Slot(uri=PLANT_TISSUE.collection_date_and_time, name="collection_date_and_time", curie=PLANT_TISSUE.curie('collection_date_and_time'),
                   model_uri=PLANT_TISSUE.collection_date_and_time, domain=None, range=str)

slots.sample_size = Slot(uri=PLANT_TISSUE.sample_size, name="sample_size", curie=PLANT_TISSUE.curie('sample_size'),
                   model_uri=PLANT_TISSUE.sample_size, domain=None, range=str,
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.tissue = Slot(uri=PLANT_TISSUE.tissue, name="tissue", curie=PLANT_TISSUE.curie('tissue'),
                   model_uri=PLANT_TISSUE.tissue, domain=None, range=str)

slots.tissue_plant_ontology_term = Slot(uri=PLANT_TISSUE.tissue_plant_ontology_term, name="tissue_plant_ontology_term", curie=PLANT_TISSUE.curie('tissue_plant_ontology_term'),
                   model_uri=PLANT_TISSUE.tissue_plant_ontology_term, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$'))

slots.geographic_location_region_and_locality = Slot(uri=PLANT_TISSUE.geographic_location_region_and_locality, name="geographic_location_region_and_locality", curie=PLANT_TISSUE.curie('geographic_location_region_and_locality'),
                   model_uri=PLANT_TISSUE.geographic_location_region_and_locality, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{1,2}|[^\s-]+.+[^\s-]+): ([^\s-]{1,2}|[^\s-]+.+[^\s-]+), ([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.geographic_location_latitude = Slot(uri=PLANT_TISSUE.geographic_location_latitude, name="geographic_location_latitude", curie=PLANT_TISSUE.curie('geographic_location_latitude'),
                   model_uri=PLANT_TISSUE.geographic_location_latitude, domain=None, range=Optional[float])

slots.geographic_location_longitude = Slot(uri=PLANT_TISSUE.geographic_location_longitude, name="geographic_location_longitude", curie=PLANT_TISSUE.curie('geographic_location_longitude'),
                   model_uri=PLANT_TISSUE.geographic_location_longitude, domain=None, range=Optional[float])

slots.depth_meters = Slot(uri=PLANT_TISSUE.depth_meters, name="depth_meters", curie=PLANT_TISSUE.curie('depth_meters'),
                   model_uri=PLANT_TISSUE.depth_meters, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.elevation_meters = Slot(uri=PLANT_TISSUE.elevation_meters, name="elevation_meters", curie=PLANT_TISSUE.curie('elevation_meters'),
                   model_uri=PLANT_TISSUE.elevation_meters, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.temperature_celsius = Slot(uri=PLANT_TISSUE.temperature_celsius, name="temperature_celsius", curie=PLANT_TISSUE.curie('temperature_celsius'),
                   model_uri=PLANT_TISSUE.temperature_celsius, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.broad_scale_environmental_context = Slot(uri=PLANT_TISSUE.broad_scale_environmental_context, name="broad_scale_environmental_context", curie=PLANT_TISSUE.curie('broad_scale_environmental_context'),
                   model_uri=PLANT_TISSUE.broad_scale_environmental_context, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$'))

slots.local_environmental_context = Slot(uri=PLANT_TISSUE.local_environmental_context, name="local_environmental_context", curie=PLANT_TISSUE.curie('local_environmental_context'),
                   model_uri=PLANT_TISSUE.local_environmental_context, domain=None, range=Optional[str])

slots.environmental_medium = Slot(uri=PLANT_TISSUE.environmental_medium, name="environmental_medium", curie=PLANT_TISSUE.curie('environmental_medium'),
                   model_uri=PLANT_TISSUE.environmental_medium, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$'))

slots.growth_facility = Slot(uri=PLANT_TISSUE.growth_facility, name="growth_facility", curie=PLANT_TISSUE.curie('growth_facility'),
                   model_uri=PLANT_TISSUE.growth_facility, domain=None, range=str)

slots.growth_medium = Slot(uri=PLANT_TISSUE.growth_medium, name="growth_medium", curie=PLANT_TISSUE.curie('growth_medium'),
                   model_uri=PLANT_TISSUE.growth_medium, domain=None, range=str)

slots.growth_medium_composition = Slot(uri=PLANT_TISSUE.growth_medium_composition, name="growth_medium_composition", curie=PLANT_TISSUE.curie('growth_medium_composition'),
                   model_uri=PLANT_TISSUE.growth_medium_composition, domain=None, range=Optional[str])

slots.plant_age = Slot(uri=PLANT_TISSUE.plant_age, name="plant_age", curie=PLANT_TISSUE.curie('plant_age'),
                   model_uri=PLANT_TISSUE.plant_age, domain=None, range=str,
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.developmental_stage = Slot(uri=PLANT_TISSUE.developmental_stage, name="developmental_stage", curie=PLANT_TISSUE.curie('developmental_stage'),
                   model_uri=PLANT_TISSUE.developmental_stage, domain=None, range=str)

slots.air_temperature_regimen = Slot(uri=PLANT_TISSUE.air_temperature_regimen, name="air_temperature_regimen", curie=PLANT_TISSUE.curie('air_temperature_regimen'),
                   model_uri=PLANT_TISSUE.air_temperature_regimen, domain=None, range=Optional[str])

slots.antibiotic_regimen = Slot(uri=PLANT_TISSUE.antibiotic_regimen, name="antibiotic_regimen", curie=PLANT_TISSUE.curie('antibiotic_regimen'),
                   model_uri=PLANT_TISSUE.antibiotic_regimen, domain=None, range=Optional[str])

slots.biotic_regimen = Slot(uri=PLANT_TISSUE.biotic_regimen, name="biotic_regimen", curie=PLANT_TISSUE.curie('biotic_regimen'),
                   model_uri=PLANT_TISSUE.biotic_regimen, domain=None, range=Optional[str])

slots.inoculation_method = Slot(uri=PLANT_TISSUE.inoculation_method, name="inoculation_method", curie=PLANT_TISSUE.curie('inoculation_method'),
                   model_uri=PLANT_TISSUE.inoculation_method, domain=None, range=Optional[str])

slots.time_post_inoculation = Slot(uri=PLANT_TISSUE.time_post_inoculation, name="time_post_inoculation", curie=PLANT_TISSUE.curie('time_post_inoculation'),
                   model_uri=PLANT_TISSUE.time_post_inoculation, domain=None, range=Optional[str])

slots.chemical_administration = Slot(uri=PLANT_TISSUE.chemical_administration, name="chemical_administration", curie=PLANT_TISSUE.curie('chemical_administration'),
                   model_uri=PLANT_TISSUE.chemical_administration, domain=None, range=Optional[str])

slots.chemical_mutagen = Slot(uri=PLANT_TISSUE.chemical_mutagen, name="chemical_mutagen", curie=PLANT_TISSUE.curie('chemical_mutagen'),
                   model_uri=PLANT_TISSUE.chemical_mutagen, domain=None, range=Optional[str])

slots.fertilizer_administration = Slot(uri=PLANT_TISSUE.fertilizer_administration, name="fertilizer_administration", curie=PLANT_TISSUE.curie('fertilizer_administration'),
                   model_uri=PLANT_TISSUE.fertilizer_administration, domain=None, range=Optional[str])

slots.insecticide_regimen = Slot(uri=PLANT_TISSUE.insecticide_regimen, name="insecticide_regimen", curie=PLANT_TISSUE.curie('insecticide_regimen'),
                   model_uri=PLANT_TISSUE.insecticide_regimen, domain=None, range=Optional[str])

slots.fungicide_regimen = Slot(uri=PLANT_TISSUE.fungicide_regimen, name="fungicide_regimen", curie=PLANT_TISSUE.curie('fungicide_regimen'),
                   model_uri=PLANT_TISSUE.fungicide_regimen, domain=None, range=Optional[str])

slots.gaseous_environment = Slot(uri=PLANT_TISSUE.gaseous_environment, name="gaseous_environment", curie=PLANT_TISSUE.curie('gaseous_environment'),
                   model_uri=PLANT_TISSUE.gaseous_environment, domain=None, range=Optional[str])

slots.growth_hormone_regimen = Slot(uri=PLANT_TISSUE.growth_hormone_regimen, name="growth_hormone_regimen", curie=PLANT_TISSUE.curie('growth_hormone_regimen'),
                   model_uri=PLANT_TISSUE.growth_hormone_regimen, domain=None, range=Optional[str])

slots.herbicide_regimen = Slot(uri=PLANT_TISSUE.herbicide_regimen, name="herbicide_regimen", curie=PLANT_TISSUE.curie('herbicide_regimen'),
                   model_uri=PLANT_TISSUE.herbicide_regimen, domain=None, range=Optional[str])

slots.humidity_regimen = Slot(uri=PLANT_TISSUE.humidity_regimen, name="humidity_regimen", curie=PLANT_TISSUE.curie('humidity_regimen'),
                   model_uri=PLANT_TISSUE.humidity_regimen, domain=None, range=Optional[str])

slots.radiation_regimen = Slot(uri=PLANT_TISSUE.radiation_regimen, name="radiation_regimen", curie=PLANT_TISSUE.curie('radiation_regimen'),
                   model_uri=PLANT_TISSUE.radiation_regimen, domain=None, range=Optional[str])

slots.light_regimen = Slot(uri=PLANT_TISSUE.light_regimen, name="light_regimen", curie=PLANT_TISSUE.curie('light_regimen'),
                   model_uri=PLANT_TISSUE.light_regimen, domain=None, range=Optional[str])

slots.last_light_transition_type = Slot(uri=PLANT_TISSUE.last_light_transition_type, name="last_light_transition_type", curie=PLANT_TISSUE.curie('last_light_transition_type'),
                   model_uri=PLANT_TISSUE.last_light_transition_type, domain=None, range=Optional[str])

slots.time_after_last_light_transition = Slot(uri=PLANT_TISSUE.time_after_last_light_transition, name="time_after_last_light_transition", curie=PLANT_TISSUE.curie('time_after_last_light_transition'),
                   model_uri=PLANT_TISSUE.time_after_last_light_transition, domain=None, range=Optional[str])

slots.salt_regimen = Slot(uri=PLANT_TISSUE.salt_regimen, name="salt_regimen", curie=PLANT_TISSUE.curie('salt_regimen'),
                   model_uri=PLANT_TISSUE.salt_regimen, domain=None, range=Optional[str])

slots.rainfall_regimen = Slot(uri=PLANT_TISSUE.rainfall_regimen, name="rainfall_regimen", curie=PLANT_TISSUE.curie('rainfall_regimen'),
                   model_uri=PLANT_TISSUE.rainfall_regimen, domain=None, range=Optional[str])

slots.watering_regimen = Slot(uri=PLANT_TISSUE.watering_regimen, name="watering_regimen", curie=PLANT_TISSUE.curie('watering_regimen'),
                   model_uri=PLANT_TISSUE.watering_regimen, domain=None, range=Optional[str])

slots.other_treatment_regimen = Slot(uri=PLANT_TISSUE.other_treatment_regimen, name="other_treatment_regimen", curie=PLANT_TISSUE.curie('other_treatment_regimen'),
                   model_uri=PLANT_TISSUE.other_treatment_regimen, domain=None, range=Optional[str])

slots.perturbation = Slot(uri=PLANT_TISSUE.perturbation, name="perturbation", curie=PLANT_TISSUE.curie('perturbation'),
                   model_uri=PLANT_TISSUE.perturbation, domain=None, range=Optional[str])

slots.mechanical_damage = Slot(uri=PLANT_TISSUE.mechanical_damage, name="mechanical_damage", curie=PLANT_TISSUE.curie('mechanical_damage'),
                   model_uri=PLANT_TISSUE.mechanical_damage, domain=None, range=Optional[str])

slots.observed_host_symbionts = Slot(uri=PLANT_TISSUE.observed_host_symbionts, name="observed_host_symbionts", curie=PLANT_TISSUE.curie('observed_host_symbionts'),
                   model_uri=PLANT_TISSUE.observed_host_symbionts, domain=None, range=Optional[str])

slots.plant_sex = Slot(uri=PLANT_TISSUE.plant_sex, name="plant_sex", curie=PLANT_TISSUE.curie('plant_sex'),
                   model_uri=PLANT_TISSUE.plant_sex, domain=None, range=Optional[str])

slots.sample_disease_status = Slot(uri=PLANT_TISSUE.sample_disease_status, name="sample_disease_status", curie=PLANT_TISSUE.curie('sample_disease_status'),
                   model_uri=PLANT_TISSUE.sample_disease_status, domain=None, range=Optional[str])

slots.sample_disease_stage = Slot(uri=PLANT_TISSUE.sample_disease_stage, name="sample_disease_stage", curie=PLANT_TISSUE.curie('sample_disease_stage'),
                   model_uri=PLANT_TISSUE.sample_disease_stage, domain=None, range=Optional[str])

slots.sample_material_processing = Slot(uri=PLANT_TISSUE.sample_material_processing, name="sample_material_processing", curie=PLANT_TISSUE.curie('sample_material_processing'),
                   model_uri=PLANT_TISSUE.sample_material_processing, domain=None, range=Optional[str])

slots.sample_storage_temperature_celsius = Slot(uri=PLANT_TISSUE.sample_storage_temperature_celsius, name="sample_storage_temperature_celsius", curie=PLANT_TISSUE.curie('sample_storage_temperature_celsius'),
                   model_uri=PLANT_TISSUE.sample_storage_temperature_celsius, domain=None, range=str,
                   pattern=re.compile(r'^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$'))

slots.sample_preservation_method = Slot(uri=PLANT_TISSUE.sample_preservation_method, name="sample_preservation_method", curie=PLANT_TISSUE.curie('sample_preservation_method'),
                   model_uri=PLANT_TISSUE.sample_preservation_method, domain=None, range=str)

slots.harvest_to_preservation_time = Slot(uri=PLANT_TISSUE.harvest_to_preservation_time, name="harvest_to_preservation_time", curie=PLANT_TISSUE.curie('harvest_to_preservation_time'),
                   model_uri=PLANT_TISSUE.harvest_to_preservation_time, domain=None, range=Optional[str])
