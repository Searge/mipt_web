from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

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


class ReviewSchema(Schema):
    feedback = fields.Str(validate=Length(3, 10))
    grade = fields.Int(validate=Range(1, 100))
