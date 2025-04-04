from django import template

register = template.Library()

# Create a custom filter to reverse encoding
@register.filter(name='reverse_encoding')
def reverse_encoding(value):
    """Reverse encoded numerical values back to their categorical labels."""
    encoding_dict = {
        'Genre': {0: 'Female', 1: 'Male'},
        'TypeEtab': {0: 'Public', 1: 'Private'},
        'Niveau': {1: 'Primary', 2: 'Secondary', 3: 'Tertiary'},
        'RetardSco': {0: 'None', 1: '1 year', 2: '2 years'},
        'Provenance': {1: 'Rural', 2: 'Suburban', 3: 'Urban'},
        'Fee_reimbursement': {0: 'No', 1: 'Yes'},
        'Result': {0: 'Continue', 1: 'Discontinue'}
    }

    for key, value_dict in encoding_dict.items():
        if value in value_dict:
            return value_dict[value]
    return value  # Return original value if it's not in the mapping
