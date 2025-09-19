<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# Plant Tissue Metadata Schema

A LinkML schema for standardizing plant tissue sample metadata collection, developed by the Joint Genome Institute (JGI) to support **genomic innovation for a sustainable bioeconomy**.


![JGI Logo](jgi_logo.png)

**A DOE Office of Science User Facility Initiative**

## Overview

The Plant Tissue Metadata Schema is a LinkML-based standardized schema for capturing comprehensive metadata about plant tissue samples. This schema supports the Joint Genome Institute's mission to **lead genomic innovation for a sustainable bioeconomy** by enabling reproducible, interoperable plant genomics research.

## Documentation

- [Schema Overview and Documentation](../../docs/elements/index.md)
- [About This Project](about.md)

## JGI Context

This schema aligns with the JGI 2024 Strategic Plan's focus on:

- **Nutrient Cycling**: Understanding biological drivers of carbon and biogeochemical cycles
- **Functional Diversity**: Characterizing functional traits across plant species in DOE-relevant ecosystems  
- **Data and Connectivity**: Providing standardized, high-quality data for AI/ML applications
- **Stewarding Resources**: Supporting the global research community with professional expertise

By standardizing plant tissue metadata collection, this schema enables researchers to contribute to transformative research addressing environmental and energy challenges in support of a sustainable bioeconomy.

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
