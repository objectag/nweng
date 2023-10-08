from nweng.nwdev.api.template import Template
from nweng.nwdev.api import API

class APIImple(API):
    def __init__(self) -> None:
        super().__init__()

    def create_template(self) -> Template:
        template = Template()
        return template