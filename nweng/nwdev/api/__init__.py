import abc
from nweng.nwdev.api.template import Template

class API(abc.ABC):
    @abc.abstractmethod
    def create_template(self) -> Template:
        """Create a new template.
        Args:
            N/A

        Returns:
            Template: The newly created template.

        Raises:
            ***Error: 

        Examples:
            ```python
            nwdev = NwDev()

            # get ready for templating
            template = nwdev.create_template("test")

            # read manifest
            manifest = template.load('./manifest/junos-node.yml')

            # reder templates defined in manifest
            config = template.render()
            ```
        """
        pass
