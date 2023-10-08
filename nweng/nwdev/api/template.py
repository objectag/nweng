
import abc
import json
import re
import sys
import yaml
import warnings

from nweng.nwdev.api.types import TagProcessor


class Template:
    def __init__(self):
        super().__init__()

    def show(self):
        """
        Show info section of the Template instance.
        """
        json_data = self.info
        json_string = json.dumps(json_data, indent=4)
        lines = json_string.splitlines()

        for i, line in enumerate(lines, start=1):
            print(f"# {line}")



    def clear(self):
        """
        Clears the member variables of the Template instance.
        """
        self.version = None
        self.head = None
        self.info = None
        self.components = []

    def load(self, file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        self.version = data.get("version")
        self.head = data.get("head")
        self.info = data.get("info")
        self.components = data.get("components")

        return self
    
    def render(self):
        processed_templates = []

        for component in self.components:
            if 'component' in component:
                if 'template' in component:
                    processed_templates.append(self.__process_template(component.get('template'), component.get('tags')))

                if 'sub-components' in component:
                    sub_component_data = component['sub-components']
                    for sub_component in sub_component_data:
                        if 'template' in sub_component:
                            processed_templates.append(self.__process_template(sub_component.get('template'), sub_component.get('tags')))

        return ''.join(processed_templates)

    def __process_template(self, template_file, tags=None):
        try:
            with open(template_file, 'r') as file:
                lines = file.readlines()
        except (FileNotFoundError) as error:
            print(error)
            sys.exit()

        # Remove lines starting with '#'
        lines = [line for line in lines if not line.strip().startswith('#')]
        content = ''.join(lines)

        if tags is not None:
            p_tags = self.__process_tags(tags)
            for tag_name, tag_value in p_tags.items():
                pattern = r'{{\s*%s\s*}}' % tag_name
                content = re.sub(pattern, tag_value, content)

            content = re.sub(r'{{\s*\w+\s*}}', '', content)

        return content

    def __process_tags(self, tags):
        processor = TagProcessor()
        processed_tags = {}
        for tag in tags:
            tag_name = tag['name']
            tag_type = tag['type']
            tag_value = tag['value']

            processed_value = processor.check_tag_value(tag_type, tag_value)
            processed_tags[tag_name] = processed_value

        return processed_tags