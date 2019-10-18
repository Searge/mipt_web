REVIEW_SCHEMA = {
    "$schema": "http://json-schema.org/schema#",
    'type': 'object',
    'properties': {
        'feedback': {
            'type': 'string',
            'minLength': 3,
            'maxLength': 10,
        },
        'grade': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 100,
        },
    },
    'requred': ['feedback', 'grade'],
}
