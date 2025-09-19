"""Basic tests for the plant tissue metadata schema."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


def test_schema_loads():
    """Test that the schema loads without errors."""
    schema_path = "src/plant_tissue_metadata_schema/schema/plant_tissue_metadata_schema.yaml"
    view = SchemaView(schema_path)
    
    # Check that the main class exists
    assert "PlantTissueSample" in view.all_classes()
    
    # Check that some key slots exist
    plant_tissue_class = view.get_class("PlantTissueSample")
    assert plant_tissue_class is not None
    
    # Verify some required slots exist
    required_slots = [
        "seq_project_id",
        "seq_project_name", 
        "sample_id",
        "seq_project_pi_name",
        "genus",
        "species",
        "ncbi_taxonomy_id"
    ]
    
    class_slot_names = view.class_slots("PlantTissueSample")
    
    for required_slot in required_slots:
        assert required_slot in class_slot_names, f"Required slot {required_slot} not found in class"


def test_required_fields():
    """Test that required fields are properly marked."""
    schema_path = "src/plant_tissue_metadata_schema/schema/plant_tissue_metadata_schema.yaml"
    view = SchemaView(schema_path)
    
    # Get required slots for PlantTissueSample
    required_slots = []
    for slot_name in view.class_slots("PlantTissueSample"):
        slot = view.get_slot(slot_name)
        if slot.required:
            required_slots.append(slot_name)
    
    # Should have some required fields
    assert len(required_slots) > 0, "No required fields found"
    
    # Check some specific required fields exist
    expected_required = [
        "seq_project_id",
        "seq_project_name", 
        "sample_id",
        "seq_project_pi_name"
    ]
    
    for field in expected_required:
        assert field in required_slots, f"Expected required field {field} is not marked as required"


def test_mixs_mappings():
    """Test that MIXS mappings are present."""
    schema_path = "src/plant_tissue_metadata_schema/schema/plant_tissue_metadata_schema.yaml"
    view = SchemaView(schema_path)
    
    # Count slots with MIXS mappings
    slots_with_mixs = 0
    for slot in view.all_slots().values():
        if hasattr(slot, 'exact_mappings') and slot.exact_mappings:
            for mapping in slot.exact_mappings:
                if str(mapping).startswith('MIXS:'):
                    slots_with_mixs += 1
                    break
    
    # Should have substantial MIXS mapping coverage
    assert slots_with_mixs >= 20, f"Expected at least 20 slots with MIXS mappings, found {slots_with_mixs}"