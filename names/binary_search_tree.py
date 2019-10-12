class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if value is less than self.value
        # check if left if None
        if value < self.value:
            # if so, set left to be this node
            # if not, call the left node's insert with this value
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # if value is greater than self.value
        # check if right is none
        elif value >= self.value:
            # if it is none, set right to be a node
            # if it has a node, call self.right.insert with this value
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # if self.value is the target,
        # return True
        if self.value == target:
            # else if target < self.value
            # check if we have a left
            # if not return False
            # if so call left.contains on the target
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # otherwise the target must be greater than self.value
        # check if we have a right
        # else, return False
        # if so, call self.right.contains on the target
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # if we have a right
        # return right's get_max
        # otherwise return self.value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        # if self.right
        # cal rightie's for_each with the cb
        if self.right != None:
            self.right.for_each(cb)
        # if self.left
        # leftie's for_each with the cb
        if self.left != None:
            self.left.for_each(cb)
        else:
            return