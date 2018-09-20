import yaml
from jinja2 import Environment, FileSystemLoader


TARGET_DIR = 'web'


def create_entry_file(entry, env):
    template = env.get_template('entry.html')
    with open(f'{TARGET_DIR}/{entry["url"]}.html', mode='w') as f:
        f.write(template.render(**entry))


def create_index_file(data, env):
    template = env.get_template('index.html')
    with open(f'{TARGET_DIR}/index.html', mode='w') as f:
        f.write(template.render(data=data))


def main():
    env = Environment(loader=FileSystemLoader('templates'))

    with open('aiml-dict-ja.yml') as f:
        data = yaml.load(f)

        for entry in data:
            entry['url'] = entry['word'].replace(' ', '-')

        create_index_file(data, env)

        for entry in data:
            create_entry_file(entry, env)


if __name__ == '__main__':
    main()
