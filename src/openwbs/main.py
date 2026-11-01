from openwbs.wbs_node import WBSNode

# Create root project node
root = WBSNode(title="Project Root")

# Level 1 elements
sublevel1 = root.add_child(WBSNode(title="Engineering & Planning"))
sublevel2 = root.add_child(WBSNode(title="Procurement"))

# Level 2 elements (Work Packages)
sublevel1_1 = sublevel1.add_child(WBSNode(title="Civil Engineering Design"))
sublevel1_2 = sublevel1.add_child(WBSNode(title="Piping Specifications"))

# Level 3 element
sublevel1_2_1 = sublevel1_2.add_child(WBSNode(title="Isometrics Review"))

# Print results
nodes = [sublevel1, sublevel2, sublevel1_1, sublevel1_2, sublevel1_2_1]
for node in nodes:
    print(f"[{node.wbs_code}] {node.title}")
