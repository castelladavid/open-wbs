from openwbs.wbs_node import WBSNode


def test_wbs_node_hierarchy():
    """Validates automatic WBS code generation across multiple hierarchy levels."""
    # Create root node
    root = WBSNode(title="Project Root")
    assert root.wbs_code == ""

    # Level 1 elements (Categories / Classification)
    sublevel1 = root.add_child(WBSNode(title="Engineering & Planning"))
    sublevel2 = root.add_child(WBSNode(title="Procurement"))

    assert sublevel1.wbs_code == "1"
    assert sublevel2.wbs_code == "2"

    # Level 2 elements (Sub-deliverables / Work Packages)
    sublevel1_1 = sublevel1.add_child(WBSNode(title="Civil Engineering Design"))
    sublevel1_2 = sublevel1.add_child(WBSNode(title="Piping Specifications"))

    assert sublevel1_1.wbs_code == "1.1"
    assert sublevel1_2.wbs_code == "1.2"

    # Level 3 element
    sublevel1_2_1 = sublevel1_2.add_child(WBSNode(title="Isometrics Review"))
    assert sublevel1_2_1.wbs_code == "1.2.1"
