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

This project uses [just](https://github.com/casey/just/) as a command runner for common development tasks. To list all available commands, run `just` or `just --list`.

### Setting up a Development Environment

1. **Install dependencies**:
   ```bash
   just install
   ```
   This installs all required Python packages using `uv`.

2. **Generate initial project files**:
   ```bash
   just gen-project
   ```
   This generates Python models, Java classes, OWL, and TypeScript representations from the schema.

### Making Schema Changes

1. **Edit the schema**: Make your changes to the LinkML schema files in `src/plant_tissue_metadata_schema/schema/`

2. **Lint your schema** (optional but recommended):
   ```bash
   just lint        # Check for issues
   just lint-fix    # Auto-fix issues where possible
   ```

3. **Test your schema changes**:
   ```bash
   just gen-project
   ```
   This command regenerates all project files from your updated schema. If it runs without errors, your schema changes are syntactically valid.

4. **Run comprehensive tests**:
   ```bash
   just test
   ```
   This runs schema validation, Python unit tests, and example validation.

### Local Development and Testing

To deploy the data harmonizer and documentation locally for testing:

1. **Build and serve the documentation with data harmonizer**:
   ```bash
   just testdoc
   ```
   This command:
   - Generates documentation from the schema
   - Builds the data harmonizer web interface
   - Copies harmonizer assets to the docs directory
   - Generates a JSON schema for the harmonizer
   - Starts a local development server (typically at http://localhost:8000)

2. **View your changes**:
   - Documentation will be available at http://localhost:8000
   - The data harmonizer interface will be at http://localhost:8000/harmonizer.html

### Other Useful Commands

- `just site` - Generate project files and documentation without starting a server
- `just gen-doc` - Generate only the markdown documentation
- `just test-examples` - Validate example data against the schema
- `just clean` - Remove all generated files

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
