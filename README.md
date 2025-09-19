<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# Plant Tissue Metadata Schema

A LinkML schema for standardizing plant tissue sample metadata collection, developed by the Joint Genome Institute (JGI) to support **genomic innovation for a sustainable bioeconomy**.

## Overview

This schema enables researchers to capture comprehensive, standardized metadata about plant tissue samples, supporting the JGI's mission to advance environmental and energy genomics research. The schema aligns with MIXS standards and integrates with plant ontologies to ensure data interoperability and reuse.

## Strategic Context

This work supports the [JGI 2024 Strategic Plan](https://jgi.doe.gov/strategic-plan) strategic themes:
- **Nutrient Cycling**: Understanding carbon and biogeochemical cycles
- **Functional Diversity**: Characterizing plant functional traits
- **Data and Connectivity**: Providing standardized data for AI/ML applications  
- **Stewarding Resources**: Supporting the global research community

## Documentation Website

[https://sierra-moxon.github.io/plant-tissue-metadata-schema](https://sierra-moxon.github.io/plant-tissue-metadata-schema)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [plant_tissue_metadata_schema](src/plant_tissue_metadata_schema)
    * [schema/](src/plant_tissue_metadata_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/plant_tissue_metadata_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
