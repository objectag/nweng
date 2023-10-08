from nweng.nwdev import NwDev
import json


nwdev = NwDev()

# get ready for templating
template = nwdev.create_template("test")


# INFRA
#

# read manifest
manifest_infra = template.load('./manifest/junos-node-infra.yml')
#manifest = template.load('./manifest/junos-service-port.yml')
#print(json.dumps(manifest.components, indent=4))

# reder templates linked in manifest
config_infra = manifest_infra.render()
template.show()
print(config_infra)

# clear member variables before loading another yml file
template.clear()

# IGP
#
manifest_igp = template.load('./manifest/junos-node-igp.yml')
config_igp = manifest_igp.render()
template.show()
print(config_igp)

# clear member variables before loading another yml file
template.clear()

# MPLS
#
manifest_mpls = template.load('./manifest/junos-node-mpls.yml')
config_mpls = manifest_mpls.render()
template.show()
print(config_mpls)


# clear member variables before loading another yml file
template.clear()

# BGP
#
manifest_bgp = template.load('./manifest/junos-node-bgp.yml')
config_bgp = manifest_bgp.render()
template.show()
print(config_bgp)


# clear member variables before loading another yml file
template.clear()

# POLICY
#
manifest_policy = template.load('./manifest/junos-node-policy.yml')
config_policy = manifest_policy.render()
template.show()
print(config_policy)






