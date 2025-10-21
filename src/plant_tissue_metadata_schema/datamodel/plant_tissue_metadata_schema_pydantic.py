from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'plant_tissue',
     'default_range': 'string',
     'description': 'A LinkML schema for capturing metadata about plant tissue '
                    'samples, including experimental conditions,\n'
                    'treatments, and sample processing information. Designed for '
                    'compatibility with MIXS standards.',
     'id': 'https://w3id.org/plant-tissue-metadata-schema',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'plant-tissue-metadata-schema',
     'prefixes': {'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'MIXS': {'prefix_prefix': 'MIXS',
                           'prefix_reference': 'https://w3id.org/mixs/'},
                  'ORCID': {'prefix_prefix': 'ORCID',
                            'prefix_reference': 'http://identifiers.org/orcid/'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PO': {'prefix_prefix': 'PO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'plant_tissue': {'prefix_prefix': 'plant_tissue',
                                   'prefix_reference': 'https://w3id.org/plant-tissue-metadata-schema/'}},
     'see_also': ['https://github.com/GenomicsStandardsConsortium/mixs'],
     'source_file': 'src/plant_tissue_metadata_schema/schema/plant_tissue_metadata_schema.yaml',
     'title': 'Plant Tissue Metadata Schema'} )


class PlantTissueSample(ConfiguredBaseModel):
    """
    A sample of plant tissue with associated metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/plant-tissue-metadata-schema'})

    seq_project_id: int = Field(default=..., description="""Project identifier, prefilled""", json_schema_extra = { "linkml_meta": {'alias': 'seq_project_id',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000092']} })
    seq_project_name: str = Field(default=..., description="""Name of the project within which the sequencing was organized""", json_schema_extra = { "linkml_meta": {'alias': 'seq_project_name',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000092'],
         'examples': [{'value': 'Forest soil metagenome'}]} })
    sample_id: int = Field(default=..., description="""Unique identifier assigned to a material sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_id',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000026']} })
    seq_project_pi_name: str = Field(default=..., description="""Principal investigator name for the sequencing project""", json_schema_extra = { "linkml_meta": {'alias': 'seq_project_pi_name', 'domain_of': ['PlantTissueSample']} })
    sample_contact_name: Optional[str] = Field(default=None, description="""Contact person for the sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_contact_name', 'domain_of': ['PlantTissueSample']} })
    tissue_contact_name: Optional[str] = Field(default=None, description="""Contact person for tissue-related questions""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_contact_name', 'domain_of': ['PlantTissueSample']} })
    proposal_id: Optional[int] = Field(default=None, description="""Proposal identifier""", json_schema_extra = { "linkml_meta": {'alias': 'proposal_id', 'domain_of': ['PlantTissueSample']} })
    tube_or_plate_label: str = Field(default=..., description="""Must be unique across all tubes and plates, and <20 characters""", json_schema_extra = { "linkml_meta": {'alias': 'tube_or_plate_label',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'Sb_roots1'}]} })
    sample_container: str = Field(default=..., description="""Select tube or plate""", json_schema_extra = { "linkml_meta": {'alias': 'sample_container',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'tube'}]} })
    plate_location: str = Field(default=..., description="""Required if samples provided in a plate. for partial plates, fill by columns""", json_schema_extra = { "linkml_meta": {'alias': 'plate_location',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'B1'}]} })
    biosafety_material_category: str = Field(default=..., description="""Choose from Algae, Animal, Archaea, Bacteria, Fungi, Plant, Plasmid, Protist, Virus, Synthetic Construct""", json_schema_extra = { "linkml_meta": {'alias': 'biosafety_material_category',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'Plant'}]} })
    sample_name: str = Field(default=..., description="""A local identifier or name for the material sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_name',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001107'],
         'examples': [{'value': 'sbicolor_3d_root_1-1'}]} })
    biological_replicate_sample_group_name: Optional[str] = Field(default=None, description="""Samples that are biological replicates should have the same group name""", json_schema_extra = { "linkml_meta": {'alias': 'biological_replicate_sample_group_name',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'sbicolor_3d_root'}]} })
    combined_tissue_description: Optional[str] = Field(default=None, description="""The number and relationship between tissues if multiple tissue samples were combined""", json_schema_extra = { "linkml_meta": {'alias': 'combined_tissue_description',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '6 lateral root tips from each of two plants'}]} })
    experimental_time_point_number: Optional[int] = Field(default=None, description="""Integer number representing the sequential numbering of time points""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_time_point_number',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '1'}]} })
    experimental_time_point_description: Optional[str] = Field(default=None, description="""Description of the time point sampled""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_time_point_description',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '3 days post germination'}]} })
    genus: str = Field(default=..., description="""Genus of the primary organism being sampled""", json_schema_extra = { "linkml_meta": {'alias': 'genus',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000029'],
         'examples': [{'value': 'Sorghum'}]} })
    species: str = Field(default=..., description="""Species of the primary organism being sampled""", json_schema_extra = { "linkml_meta": {'alias': 'species',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000029'],
         'examples': [{'value': 'bicolor'}]} })
    strain_variety_or_cultivar: str = Field(default=..., description="""Name or ID of the cultivar, variety, strain, or other similar designation""", json_schema_extra = { "linkml_meta": {'alias': 'strain_variety_or_cultivar',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001318'],
         'examples': [{'value': 'RTx430'}]} })
    isolate: Optional[str] = Field(default=None, description="""Isolate or mutant name""", json_schema_extra = { "linkml_meta": {'alias': 'isolate',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'Sb_Mut1'}]} })
    germplasm_collection_and_id: Optional[str] = Field(default=None, description="""Culture collection name and ID from which the original plant germplasm was sourced""", json_schema_extra = { "linkml_meta": {'alias': 'germplasm_collection_and_id',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'ABRC CS22561'}]} })
    ncbi_taxonomy_id: str = Field(default=..., description="""Unique identifier from the NCBI taxonomy database""", json_schema_extra = { "linkml_meta": {'alias': 'ncbi_taxonomy_id',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000250'],
         'examples': [{'value': '4558'}]} })
    ancestral_data: Optional[str] = Field(default=None, description="""Information about either pedigree or other description of ancestral information""", json_schema_extra = { "linkml_meta": {'alias': 'ancestral_data',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000247'],
         'examples': [{'value': 'Hybrid of A x B lines'}]} })
    genetic_modification: Optional[str] = Field(default=None, description="""Genetic modifications of the genome of an organism""", json_schema_extra = { "linkml_meta": {'alias': 'genetic_modification',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000859'],
         'examples': [{'value': 'mlo-11 allele'}]} })
    estimated_genome_size_mb: Optional[int] = Field(default=None, description="""Estimated genome size of the primary species being sampled, between 1-100000""", json_schema_extra = { "linkml_meta": {'alias': 'estimated_genome_size_mb',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '730'}]} })
    gc_content_percent: Optional[int] = Field(default=None, description="""Estimated GC content of the genome of the primary species being sampled""", json_schema_extra = { "linkml_meta": {'alias': 'gc_content_percent',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '45'}]} })
    ploidy: Optional[str] = Field(default=None, description="""The ploidy level of the genome""", json_schema_extra = { "linkml_meta": {'alias': 'ploidy',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000021'],
         'examples': [{'value': 'diploid'}]} })
    reference_genome: str = Field(default=..., description="""Reference genome and annotation to be used for analysis""", json_schema_extra = { "linkml_meta": {'alias': 'reference_genome',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'Phytozome Sorghum bicolor RTx430 v2.1'}]} })
    collection_date_and_time: str = Field(default=..., description="""The time of sampling, either as an instance or interval""", json_schema_extra = { "linkml_meta": {'alias': 'collection_date_and_time',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000011'],
         'examples': [{'value': '2025-08-10T14:00:00-07:00'}]} })
    sample_size: str = Field(default=..., description="""The total amount or size of sample collected""", json_schema_extra = { "linkml_meta": {'alias': 'sample_size',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000001'],
         'examples': [{'value': '0.45 g'}]} })
    tissue: str = Field(default=..., description="""Detailed description of the organ or type of tissue sampled""", json_schema_extra = { "linkml_meta": {'alias': 'tissue',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '5 mm lateral root tips'}]} })
    tissue_plant_ontology_term: Optional[str] = Field(default=None, description="""Plant ontology term corresponding to plant structure sampled""", json_schema_extra = { "linkml_meta": {'alias': 'tissue_plant_ontology_term',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001060'],
         'examples': [{'value': 'seedling cotyledon (PO:0025471);  seedling hypocotyl '
                                '(PO:0025291)'}]} })
    geographic_location_region_and_locality: Optional[str] = Field(default=None, description="""The geographical origin of the sample as defined by country or sea name followed by specific region name""", json_schema_extra = { "linkml_meta": {'alias': 'geographic_location_region_and_locality',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000010'],
         'examples': [{'value': 'USA: California, Berkeley'}]} })
    geographic_location_latitude: Optional[float] = Field(default=None, description="""The geographical origin of the sample as defined by latitude""", json_schema_extra = { "linkml_meta": {'alias': 'geographic_location_latitude',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000009'],
         'examples': [{'value': '37.877184'}]} })
    geographic_location_longitude: Optional[float] = Field(default=None, description="""The geographical origin of the sample as defined by longitude""", json_schema_extra = { "linkml_meta": {'alias': 'geographic_location_longitude',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000009'],
         'examples': [{'value': '-122.250841'}]} })
    depth_meters: Optional[str] = Field(default=None, description="""The vertical distance (in meters) below local surface""", json_schema_extra = { "linkml_meta": {'alias': 'depth_meters',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000018'],
         'examples': [{'value': '0.1'}]} })
    elevation_meters: Optional[str] = Field(default=None, description="""Elevation (in meters) of the sampling site as measured by the vertical distance from mean sea level""", json_schema_extra = { "linkml_meta": {'alias': 'elevation_meters',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000093'],
         'examples': [{'value': '120'}]} })
    temperature_celsius: Optional[str] = Field(default=None, description="""Temperature (in degrees Celsius) of the sample at time of sampling""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_celsius',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000113'],
         'examples': [{'value': '22'}]} })
    broad_scale_environmental_context: Optional[str] = Field(default=None, description="""The major environmental system the sample or specimen came from""", json_schema_extra = { "linkml_meta": {'alias': 'broad_scale_environmental_context',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000012'],
         'examples': [{'value': 'rangeland biome [ENVO:01000247]'}]} })
    local_environmental_context: Optional[str] = Field(default=None, description="""The entity or entities in the sample's local vicinity""", json_schema_extra = { "linkml_meta": {'alias': 'local_environmental_context',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000013'],
         'examples': [{'value': 'hillside [ENVO:01000333]'}]} })
    environmental_medium: Optional[str] = Field(default=None, description="""The environmental material(s) immediately surrounding the sample at time of sampling""", json_schema_extra = { "linkml_meta": {'alias': 'environmental_medium',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000014'],
         'examples': [{'value': 'bluegrass field soil [ENVO:00005789]'}]} })
    growth_facility: str = Field(default=..., description="""Type of facility where the sampled plant was grown""", json_schema_extra = { "linkml_meta": {'alias': 'growth_facility',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001043'],
         'examples': [{'value': 'greenhouse'}]} })
    growth_medium: str = Field(default=..., description="""General specification of the media for growing the plants or tissue cultured samples""", json_schema_extra = { "linkml_meta": {'alias': 'growth_medium',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001057'],
         'examples': [{'value': 'soil'}]} })
    growth_medium_composition: Optional[str] = Field(default=None, description="""Detailed description of the makeup of the plant growth medium""", json_schema_extra = { "linkml_meta": {'alias': 'growth_medium_composition',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '2:1:1 mix of coco coir, sand, and vermiculite'}]} })
    plant_age: str = Field(default=..., description="""The age of the plant from which the tissue was sampled""", json_schema_extra = { "linkml_meta": {'alias': 'plant_age',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000255'],
         'examples': [{'value': '3 days post germination'}]} })
    developmental_stage: str = Field(default=..., description="""The developmental stage of the plant from which the tissue was sampled""", json_schema_extra = { "linkml_meta": {'alias': 'developmental_stage',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000251'],
         'examples': [{'value': 'seedling'}]} })
    air_temperature_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving an exposure to varying temperatures""", json_schema_extra = { "linkml_meta": {'alias': 'air_temperature_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000551'],
         'examples': [{'value': '22�C 12h day / 18�C 12h night'}]} })
    antibiotic_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving antibiotic administration""", json_schema_extra = { "linkml_meta": {'alias': 'antibiotic_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000553'],
         'examples': [{'value': 'kanamycin 50 ug/mL added to agar plates for the full '
                                'duration of growth'}]} })
    biotic_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of biotic factors""", json_schema_extra = { "linkml_meta": {'alias': 'biotic_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001038'],
         'examples': [{'value': 'Agrobacterium tumefaciens GV3101 infiltration'}]} })
    inoculation_method: Optional[str] = Field(default=None, description="""Method and material used for inoculation or infiltration with a biotic agent""", json_schema_extra = { "linkml_meta": {'alias': 'inoculation_method',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'syringe infiltration with GV3101 (OD600=0.5) carrying '
                                'pCAMBIA1300-35S::GFP'}]} })
    time_post_inoculation: Optional[str] = Field(default=None, description="""The time between inoculation with the biotic agent and sample collection""", json_schema_extra = { "linkml_meta": {'alias': 'time_post_inoculation',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '2:12:00'}]} })
    chemical_administration: Optional[str] = Field(default=None, description="""List of chemical compounds administered to the host or site where sampling occurred""", json_schema_extra = { "linkml_meta": {'alias': 'chemical_administration',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000751'],
         'examples': [{'value': '50 mM KNO3 fertilizer, weekly'}]} })
    chemical_mutagen: Optional[str] = Field(default=None, description="""Treatment involving use of mutagens""", json_schema_extra = { "linkml_meta": {'alias': 'chemical_mutagen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000555'],
         'examples': [{'value': 'seeds soaked in EMS, 0.1%, 6h exposure before '
                                'planting'}]} })
    fertilizer_administration: Optional[str] = Field(default=None, description="""Information about treatment involving the use of fertilizers""", json_schema_extra = { "linkml_meta": {'alias': 'fertilizer_administration',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000556'],
         'examples': [{'value': "0.5x Hoagland's solution, weekly"}]} })
    insecticide_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of insecticides""", json_schema_extra = { "linkml_meta": {'alias': 'insecticide_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000573'],
         'examples': [{'value': 'imidacloprid, 0.5 mg/L, soil drench at time of '
                                'planting'}]} })
    fungicide_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of fungicides""", json_schema_extra = { "linkml_meta": {'alias': 'fungicide_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000557'],
         'examples': [{'value': 'azoxystrobin, 100 ppm, foliar spray once at weeks 2, '
                                '3, and 4'}]} })
    gaseous_environment: Optional[str] = Field(default=None, description="""Use of conditions with differing gaseous environments""", json_schema_extra = { "linkml_meta": {'alias': 'gaseous_environment',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000558'],
         'examples': [{'value': 'elevated CO2, 600 ppm, continuous'}]} })
    growth_hormone_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of growth hormones""", json_schema_extra = { "linkml_meta": {'alias': 'growth_hormone_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000560'],
         'examples': [{'value': 'IAA 1 �M for 24h at 6 days old, followed by transfer '
                                'to control condition without hormone for 48h before '
                                'sampling'}]} })
    herbicide_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of herbicides""", json_schema_extra = { "linkml_meta": {'alias': 'herbicide_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000561'],
         'examples': [{'value': 'glyphosate 10 �M, foliar spray, once at 2 weeks'}]} })
    humidity_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving an exposure to varying degree of humidity""", json_schema_extra = { "linkml_meta": {'alias': 'humidity_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000568'],
         'examples': [{'value': '65% RH, constant'}]} })
    radiation_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving exposure to a particular radiation regimen""", json_schema_extra = { "linkml_meta": {'alias': 'radiation_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000575'],
         'examples': [{'value': 'UV-B 1.5 W/m2, 2h/day, for 5 days starting at day 7'}]} })
    light_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving an exposure to light""", json_schema_extra = { "linkml_meta": {'alias': 'light_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000569'],
         'examples': [{'value': '150 �mol m-2 s-1, 16h light / 8h dark'}]} })
    last_light_transition_type: Optional[str] = Field(default=None, description="""The most recent light transition before sampling""", json_schema_extra = { "linkml_meta": {'alias': 'last_light_transition_type',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'lights on'}]} })
    time_after_last_light_transition: Optional[str] = Field(default=None, description="""The time between sampling and the most recent light transition""", json_schema_extra = { "linkml_meta": {'alias': 'time_after_last_light_transition',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '2:00'}]} })
    salt_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving use of salts as supplement""", json_schema_extra = { "linkml_meta": {'alias': 'salt_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000582'],
         'examples': [{'value': 'NaCl 100 mM added to hydroponic medium at day 3, '
                                'followed by transfer to fresh hydroponic medium '
                                'without elevated NaCl for 3 days before sampling'}]} })
    rainfall_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving an exposure to a given amount of rainfall""", json_schema_extra = { "linkml_meta": {'alias': 'rainfall_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000576'],
         'examples': [{'value': '30cm of rainfall during growing season'}]} })
    watering_regimen: Optional[str] = Field(default=None, description="""Information about treatment involving an exposure to watering frequencies""", json_schema_extra = { "linkml_meta": {'alias': 'watering_regimen',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000591'],
         'examples': [{'value': '100 ml per pot every 3 days'}]} })
    other_treatment_regimen: Optional[str] = Field(default=None, description="""Information about treatments not captured by other available treatment categories""", json_schema_extra = { "linkml_meta": {'alias': 'other_treatment_regimen', 'domain_of': ['PlantTissueSample']} })
    perturbation: Optional[str] = Field(default=None, description="""Type of perturbation coupled with perturbation regimen""", json_schema_extra = { "linkml_meta": {'alias': 'perturbation',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000754'],
         'examples': [{'value': 'drought stress beginning at 8 weeks for a period of 4 '
                                'weeks'}]} })
    mechanical_damage: Optional[str] = Field(default=None, description="""Information about any mechanical damage exerted on the plant""", json_schema_extra = { "linkml_meta": {'alias': 'mechanical_damage',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001052'],
         'examples': [{'value': 'root wounding, 24h before sampling'}]} })
    observed_host_symbionts: Optional[str] = Field(default=None, description="""The taxonomic name of organism(s) found living in symbiosis with the specific host""", json_schema_extra = { "linkml_meta": {'alias': 'observed_host_symbionts',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001298'],
         'examples': [{'value': 'arbuscular mycorrhizal fungi'}]} })
    plant_sex: Optional[str] = Field(default=None, description="""Sex of the reproductive parts on the whole plant""", json_schema_extra = { "linkml_meta": {'alias': 'plant_sex',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0001059'],
         'examples': [{'value': 'hermaphrodite'}]} })
    sample_disease_status: Optional[str] = Field(default=None, description="""List of diseases with which the subject has been diagnosed at time of sample collection""", json_schema_extra = { "linkml_meta": {'alias': 'sample_disease_status',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000031'],
         'examples': [{'value': 'infection with Pseudomonas syringae pv. tomato '
                                'DC3000'}]} })
    sample_disease_stage: Optional[str] = Field(default=None, description="""Stage of the disease at the time of sample collection""", json_schema_extra = { "linkml_meta": {'alias': 'sample_disease_stage',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000249'],
         'examples': [{'value': 'infection'}]} })
    sample_material_processing: Optional[str] = Field(default=None, description="""A brief description of any processing applied to the sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_material_processing',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000016'],
         'examples': [{'value': 'roots were removed from pots rinsed with tap water '
                                'before flash freezing with liquid nitrogen'}]} })
    sample_storage_temperature_celsius: str = Field(default=..., description="""Temperature at which sample was stored (in degrees Celsius)""", json_schema_extra = { "linkml_meta": {'alias': 'sample_storage_temperature_celsius',
         'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['MIXS:0000110'],
         'examples': [{'value': '-80'}]} })
    sample_preservation_method: str = Field(default=..., description="""The method employed for preserving or fixing the tissue""", json_schema_extra = { "linkml_meta": {'alias': 'sample_preservation_method',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': 'N2 Freeze'}]} })
    harvest_to_preservation_time: Optional[str] = Field(default=None, description="""The time between sampling and sample preservation, minutes""", json_schema_extra = { "linkml_meta": {'alias': 'harvest_to_preservation_time',
         'domain_of': ['PlantTissueSample'],
         'examples': [{'value': '15'}]} })

    @field_validator('genetic_modification')
    def pattern_genetic_modification(cls, v):
        pattern=re.compile(r"^{PMID}|{DOI}|{URL}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid genetic_modification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid genetic_modification format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ploidy')
    def pattern_ploidy(cls, v):
        pattern=re.compile(r"^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ploidy format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ploidy format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_size')
    def pattern_sample_size(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_size format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_size format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('tissue_plant_ontology_term')
    def pattern_tissue_plant_ontology_term(cls, v):
        pattern=re.compile(r"^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid tissue_plant_ontology_term format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid tissue_plant_ontology_term format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('geographic_location_region_and_locality')
    def pattern_geographic_location_region_and_locality(cls, v):
        pattern=re.compile(r"^([^\s-]{1,2}|[^\s-]+.+[^\s-]+): ([^\s-]{1,2}|[^\s-]+.+[^\s-]+), ([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid geographic_location_region_and_locality format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid geographic_location_region_and_locality format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('depth_meters')
    def pattern_depth_meters(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid depth_meters format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid depth_meters format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('elevation_meters')
    def pattern_elevation_meters(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid elevation_meters format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid elevation_meters format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('temperature_celsius')
    def pattern_temperature_celsius(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid temperature_celsius format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid temperature_celsius format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('broad_scale_environmental_context')
    def pattern_broad_scale_environmental_context(cls, v):
        pattern=re.compile(r"^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid broad_scale_environmental_context format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid broad_scale_environmental_context format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('environmental_medium')
    def pattern_environmental_medium(cls, v):
        pattern=re.compile(r"^([^\s-]{1,2}|[^\s-]+.+[^\s-]+) \[[a-zA-Z]{2,}:[a-zA-Z0-9]\d+\]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid environmental_medium format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid environmental_medium format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('plant_age')
    def pattern_plant_age(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid plant_age format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid plant_age format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_storage_temperature_celsius')
    def pattern_sample_storage_temperature_celsius(cls, v):
        pattern=re.compile(r"^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?( *- *[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)? *([^\s-]{1,2}|[^\s-]+.+[^\s-]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_storage_temperature_celsius format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_storage_temperature_celsius format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PlantTissueSample.model_rebuild()

