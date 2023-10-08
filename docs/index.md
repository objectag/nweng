




## Manifest Yaml Specification 

```# Specification Document for YAML Configuration

## Version Information:
version: string  # Version number of the configuration file. Example: "0.1.0"

## Head Details:
_head:
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
        value: string  # Value of the tag. Example: "r01", "syd02", etc.

  - component:
    group: string  # Group to which the component belongs. Example: "infra"
    name: string  # Name of the component. Example: "snmp"
    template: string  # Path to the template file for the component. Example: "./templates/junos/infra_snmp.conf"
    tags:  # List of tags associated with the component.
      - name: string  # Name of the tag. Example: "pop", "contact", etc.
        value: string  # Value of the tag. Example: "syd02", "contact@example.com", etc.


```

## Notes:
- The version, head details, and information sections provide metadata about the configuration.
- The components section lists the different components of the configuration, each with its group, name, template path, and associated tags. Tags have a name and corresponding value.
- The examples provided in the component section are for illustration purposes and may vary in actual configurations.