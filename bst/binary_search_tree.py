class TreeNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, key, value):
    self.root = self._insert(self.root, key, value)

  def _insert(self, node, key, value):
    if node is None:
      return TreeNode(key, value)
    if key < node.key:
      node.left = self._insert(node.left, key, value)
    elif key > node.key:
      node.right = self._insert(node.right, key, value)
    else:
      node.value = value

    node.height = 1 + max(self._get_height(node.left), 
                        self._get_height(node.right))
    
    return node
  
  def search(self, key):
    node = self._search(self.root, key)
    return node.value if node else None
  
  def _search(self, node, key):
    if node is None or node.key == key:
      return node
    if key < node.key:
      return self._search(node.left, key)
    else:
      return self._search(node.right, key)
    
  def delete(self, key):
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):
    if node is None:
      return node
    if key < node.key:
      node.left = self._delete(node.left, key)
    elif key > node.key:
      node.right = self._delete(node.right, key)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      
      successor = self._min_value_node(node.right)

      node.key = successor.key
      node.value = successor.value

      node.right = self._delete(node.right, successor.key)
    
    if node:
      node.height = 1 + max(self._get_height(node.left), 
                          self._get_height(node.right))
        
    return node
  
  def _min_value_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current
  
  def height(self):
    return self._get_height(self.root)
  
  def _get_height(self, node):
    if node is None:
      return 0
    return node.height
  
  def is_balanced(self):
    return self._is_balanced(self.root)
  
  def _is_balanced(self, node):
    if node is None:
      return True
    
    left_height = self._get_height(node.left)
    right_height = self._get_height(node.right)
    balance_factor = abs(left_height - right_height)

    return (balance_factor <= 1 and 
            self._is_balanced(node.left) and 
            self._is_balanced(node.right))