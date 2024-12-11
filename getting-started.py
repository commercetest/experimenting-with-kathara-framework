import yaml
from rich import print
from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara

lab = Lab("kathara-tutorial-three-eleven-two-too")

pc1 = lab.new_machine("pc1")
pc2 = lab.new_machine("pc2")

lab.connect_machine_to_link(pc1.name, "A")
lab.connect_machine_to_link(pc2.name, "A")

Kathara.get_instance().deploy_lab(lab)

lab_status = next(Kathara.get_instance().get_machines_stats(lab_name=lab.name))
# print(yaml.dump(str(lab_status), default_flow_style=False))
print(lab_status)


print(Kathara.get_instance().get_link_stats(lab_name=lab.name, link_name="A"))

Kathara.get_instance().wipe()

