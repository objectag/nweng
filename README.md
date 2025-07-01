# nweng


## Overview

`nweng` is a Python API for network engineering, focusing on templated configuration generation using YAML manifests and tag-based substitution/validation. It helps automate the creation of network device configurations with strong validation for common network data types.

## Installation

You can install `nweng` using pip (from the project root):

```bash
pip install .
```

For development (editable install):

```bash
pip install -e .
```

Or clone the repository and install dependencies manually:

```bash
git clone https://github.com/objectag/nweng.git
cd nweng
pip install .
```

## Features
- **YAML Manifest Specification**: Define network configurations in YAML, including metadata, components, and tags.
- **Templating Engine**: Load YAML manifests, process templates, and substitute tags with validation.
- **Tag Validation**: Supports types like string, email, IPv4/IPv6, interface, SID, ASN, with built-in validation.
- **Extensible API**: Modular design for easy extension and integration.

## Project Structure
- `nweng/nwdev/`: Core logic and API
  - `api/`: Templating, tag types, and API implementation
  - `index.md`: Documentation for YAML manifest structure
- `nweng/nwops/`: (Reserved for operational modules)
- `nweng/nwdev/test/`: (Reserved for tests)

## YAML Manifest Specification

```
# Specification Document for YAML Configuration

## Version Information:
version: string  # Version number of the configuration file. Example: "0.1.0"

## Head Details:
head:
  _cat: string  # Date and time of creation in ISO 8601 format. Example: "2021-11-12T10:58:08"
  _chost: string  # Host IP address where the configuration was created. Example: "192.168.0.100"
  _cname: string  # Name of the creator. Example: "username"
  _cemail: string  # Email address of the creator. Example: "username@example.com"
  _template-type: string  # Type of the template used. Example: "node"

## Information:
info:
  title: string  # Title of the configuration. Example: "MPLS/IP backbone node"
  version: string  # Version of the configuration. Example: "0.1.0"
  description: string  # Description of the configuration. Example: "test"

## Components:
components:
  - component:
      group: string  # Group to which the component belongs. Example: "infra"
      name: string  # Name of the component. Example: "routing-engine"
      template: string  # Path to the template file for the component. Example: "./templates/junos/infra_groups_re.conf"
      tags:  # List of tags associated with the component.
        - name: string  # Name of the tag. Example: "hostname", "pop", etc.
          type: string  # Tag type. One of: string, email, ipv4, ipv6, interface, sid, asn
          value: string  # Value of the tag. Example: "r01", "syd02", etc.
      sub-components:  # (Optional) List of sub-components
        - name: string  # Name of the sub-component
          template: string  # Path to the template file for the sub-component
          tags:
            - name: string
              type: string  # Tag type as above
              value: string

  - component:
      group: string  # Group to which the component belongs. Example: "infra"
      name: string  # Name of the component. Example: "snmp"
      template: string  # Path to the template file for the component. Example: "./templates/junos/infra_snmp.conf"
      tags:
        - name: string  # Name of the tag. Example: "pop", "contact", etc.
          type: string  # Tag type as above
          value: string  # Value of the tag. Example: "syd02", "contact@example.com", etc.

```

### Supported Tag Types
- `string`: Any string value
- `email`: Email address
- `ipv4`: IPv4 address or IPv4/prefix (e.g., 192.0.2.1/24)
- `ipv6`: IPv6 address or IPv6/prefix (e.g., 2001:db8::1/64)
- `interface`: Network interface (e.g., ge-0/0/0.0, lo0)
- `sid`: 8-character hexadecimal string
- `asn`: Autonomous System Number (1-4294967295)

### Notes:
- The version, head details, and information sections provide metadata about the configuration.
- The components section lists the different components of the configuration, each with its group, name, template path, and associated tags. Tags have a name, type, and value.
- Components can optionally include `sub-components`, each with their own template and tags.
- The examples provided in the component section are for illustration purposes and may vary in actual configurations.

## Usage Example
```python
from nweng.nwdev.api.template import Template

template = Template()
template.load('path/to/manifest.yaml')
rendered = template.render()
print(rendered)
```

## Links
- [Homepage](https://github.com/objectag/nweng)
- [Bug Tracker](https://github.com/objectag/nweng/issues)

## License
Apache Software License
