#!python3


class PrefixTreeNode:
    """PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose an appropriate type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = dict # list or dict

    def __init__(self, character=None):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Character that this node represents
        self.character = character
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False
        # Data structure to associate character keys to children node values
        self.children = PrefixTreeNode.CHILDREN_TYPE()

    def is_terminal(self):
        """Return True if this prefix tree node terminates a string."""
        # TODO: Determine if this node is terminal
        if self.terminal == True:
            return True
        else:
            return False

    def num_children(self):
        """Return the number of children nodes this prefix tree node has."""
        # TODO: Determine how many children this node has
        number = 0
        for _ in self.children.keys():
            number += 1
        return number

    def has_child(self, character):
        """Return True if this prefix tree node has a child node that
        represents the given character amongst its children."""
        # TODO: Check if given character is amongst this node's children
        for key in self.children.keys():
            if key == character:
                return True
            else:
                return False

    def get_child(self, character):
        """Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not."""
        # TODO: Find child node for given character in this node's children
        if self.has_child(character):
            # This is a bool object 
            for key in self.has_child(character):

                if key == character:
                    return self.children[key]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children."""
        # TODO: Add given character and child node to this node's children
        if not self.has_child(character):
            self.children[character] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'