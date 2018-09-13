"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""
#Import the Portal object.
import geni.portal as portal
import geni.rspec.pg as pg
# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
link = request.LAN("lan")
for i in range(0,4):
    node = request.XenVM(str("Node-") + str(i+1))
    iface = node.addInterface("if" + str(i+1))
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address("192.168.1."+str(i+1),"255.255.255.0"))
    
    link.addInterface(iface)
    if (i == 0):
       node.routable_control_ip ="true"
    
    node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)

