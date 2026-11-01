from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class WBSNode:
    """Represents an element or work package within the WBS structure."""

    title: str
    description: str = ""
    owner: str = ""
    parent: Optional["WBSNode"] = field(default=None, repr=False)
    children: List["WBSNode"] = field(default_factory=list)

    def add_child(self, child: "WBSNode") -> "WBSNode":
        """Adds a child to this node and automatically assigns the parent."""
        child.parent = self
        self.children.append(child)
        return child

    @property
    def wbs_code(self) -> str:
        """Automatically calculates the hierarchical code (e.g., 1.2.1)."""
        if self.parent is None or self.parent.parent is None:
            if self.parent is None:
                return ""  # Main root node of the entire project
            idx = self.parent.children.index(self) + 1
            return str(idx)

        idx = self.parent.children.index(self) + 1
        return f"{self.parent.wbs_code}.{idx}"
