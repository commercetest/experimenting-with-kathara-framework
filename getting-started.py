# Getting started example that cleans up after itself.
# NB: AFAIK the wipe command removes any Kathara lab instance created by
# this linux user's (i.e. your user) account.

import os
import yaml
from rich import print
from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara

lab = Lab("kathara-tutorial-three-eleven-two-too")

pc1 = lab.new_machine("pc1")
pc2 = lab.new_machine("pc2")
webserver = lab.new_machine("webserver")

# Create a router, here using the bird.cz docker image
birdrouter1 = lab.new_machine("birdrouter1", **{"image": "kathara/bird"})
birdrouter2 = lab.new_machine("birdrouter2", **{"image": "kathara/bird"})

lab.connect_machine_to_link(pc1.name, "A")
lab.connect_machine_to_link(pc2.name, "A")
lab.connect_machine_to_link(webserver.name, "B")
lab.connect_machine_to_link(birdrouter1.name, "A")
lab.connect_machine_to_link(birdrouter1.name, "C")
lab.connect_machine_to_link(birdrouter2.name, "B")
lab.connect_machine_to_link(birdrouter2.name, "C")

# NB: the following commands silently fail without the commas.
# I think the last of the commands is processed as the web server does start apache2
lab.create_file_from_list(
    [
        "ip address add 100.1.2.11/24 dev eth0",
        "ip route add default via 100.1.2.1 dev eth0"
    ],
    "pc1.startup"
)

lab.create_file_from_list(
    [
        "ip address add 100.1.2.12/24 dev eth0",
        "ip route add default via 100.1.2.1 dev eth0"
    ],
    "pc2.startup"
)


lab.create_file_from_list(
    [
        "ip address add 100.1.3.90/24 dev eth0",
        "ip route add default via 100.1.3.1 dev eth0",
        "systemctl start apache2"
    ],
    "webserver.startup"
)

lab.create_file_from_list(
    [
        "ip address add 100.1.2.1/24 dev eth0",
        "ip address add 10.0.0.1/24 dev eth1",
        "/usr/local/bin/systemctl start bird",
    ],
    "birdrouter1.startup"
)

lab.create_file_from_list(
    [
        "ip address add 100.1.3.1/24 dev eth0",
        "ip address add 10.0.0.2/24 dev eth1",
        "/usr/local/bin/systemctl start bird",
    ],
    "birdrouter2.startup"
)

birdrouter1.create_file_from_path(os.path.join("configs", "birdrouter1-bird.conf"), "/etc/bird/bird.conf")
birdrouter2.create_file_from_path(os.path.join("configs", "birdrouter2-bird.conf"), "/etc/bird/bird.conf")

Kathara.get_instance().deploy_lab(lab)

lab_status = next(Kathara.get_instance().get_machines_stats(lab_name=lab.name))
print(lab_status)
Kathara.get_instance().connect_tty(birdrouter1.name, lab_name=lab.name)
Kathara.get_instance().connect_tty(birdrouter2.name, lab_name=lab.name)
Kathara.get_instance().connect_tty(webserver.name, lab_name=lab.name)
Kathara.get_instance().connect_tty(pc1.name, lab_name=lab.name)

print("Network A follows")
print(Kathara.get_instance().get_link_stats(lab_name=lab.name, link_name="A"))
print("Network B follows")
print(Kathara.get_instance().get_link_stats(lab_name=lab.name, link_name="B"))
print("Network C follows")
print(Kathara.get_instance().get_link_stats(lab_name=lab.name, link_name="C"))

# Currently there are 3 python errors reported, seemingly one for each connect_tty call.
Kathara.get_instance().wipe()
