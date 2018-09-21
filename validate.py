import yaml


MANDATORY_FIELDS = ['word', 'trans', 'kana']
OPTIONAL_FIELDS = ['var', 'def', 'ref', 'syn']


def validate_entry(entry):
    if not isinstance(entry, dict):
        raise ValueError('Entry %r is not a dict' % entry)

    for field in MANDATORY_FIELDS:
        if  field not in entry:
            raise ValueError('Entry %r does not have the mandatory `%s` field' % (entry, field))

    unrecognized_fields = set(entry.keys()) - set(MANDATORY_FIELDS) - set(OPTIONAL_FIELDS)
    if unrecognized_fields:
        raise ValueError('Entry %r has unrecognized field(s): %r' % (entry, unrecognized_fields))

    if 'ref' in entry:
        if not isinstance(entry['ref'], list):
            raise ValueError('Entry %r has a `ref` field which is not a list' % entry)


def main():
    with open('aiml-dict-ja.yml') as f:
        data = yaml.load(f)

        if not isinstance(data, list):
            raise ValueError('The dictionary data is not a list')

        print('%d entries found.' % len(data))

        for entry in data:
            validate_entry(entry)

        print('Validation: PASSED')


if __name__ == '__main__':
    main()
