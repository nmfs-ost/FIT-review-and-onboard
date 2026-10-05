import argparse
import json
from pathlib import Path
import sys

from jsonschema.validators import validator_for


def parse_json(content):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'Duplicate JSON property: {key}')
            result[key] = value
        return result

    return json.loads(content, object_pairs_hook=unique_object)


def read_json(path):
    return parse_json(Path(path).read_text())


def validate(data, schema):
    validator = validator_for(schema)
    validator.check_schema(schema)
    return [
        f"Schema ({'.'.join(map(str, error.absolute_path)) or '$'}): {error.message}"
        for error in sorted(validator(schema).iter_errors(data), key=lambda error: str(list(error.absolute_path)))
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['validate'])
    parser.add_argument('--schema', required=True)
    parser.add_argument('--metadata', required=True)
    args = parser.parse_args()
    schema = read_json(args.schema)
    data = read_json(args.metadata)
    errors = validate(data, schema)
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print('Metadata passed JSON Schema validation.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())