import yaml
from jinja2 import Environment, FileSystemLoader


TARGET_DIR = 'web'


def word_to_url(word):
    word = word.lower()
    word = word.replace('/', '')
    word = word.replace(' ', '-')
    return f'{word}.html'


def get_ref_list(entry):
    """Given a raw list of references (from YAML), convert it to a list of (text, url)."""
    if 'ref' not in entry:
        return []

    ref_list = []
    for ref in entry['ref']:
        if isinstance(ref, str):
            ref_list.append((ref, word_to_url(ref)))
        elif isinstance(ref, dict):
            assert len(ref) == 1
            text, url = list(ref.items())[0]
            ref_list.append((text, url))
        else:
            assert False

    return ref_list


def create_entry_file(entry, env, prev_entry=None, next_entry=None):
    page_data = dict(entry)  # shallow copy
    page_data['ref_list'] = get_ref_list(entry)
    page_data['prev_entry'] = prev_entry
    page_data['next_entry'] = next_entry

    template = env.get_template('entry.html')
    with open(f'{TARGET_DIR}/{entry["url"]}', mode='w') as f:
        f.write(template.render(**page_data))


def create_index_file(data, env):
    template = env.get_template('index.html')
    with open(f'{TARGET_DIR}/index.html', mode='w') as f:
        f.write(template.render(data=data))


def main():
    env = Environment(loader=FileSystemLoader('templates'))

    with open('aiml-dict-ja.yml') as f:
        data = yaml.load(f)

        for entry in data:
            entry['url'] = word_to_url(entry['word'])

        create_index_file(data, env)

        for i, entry in enumerate(data):
            prev_entry = data[i-1] if i > 0 else None
            next_entry = data[i+1] if i < len(data) - 1 else None
            create_entry_file(entry, env, prev_entry=prev_entry, next_entry=next_entry)


if __name__ == '__main__':
    main()
