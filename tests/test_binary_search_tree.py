import pytest
from bst import BinarySearchTree, TreeNode


class TestTreeNode:
  def test_tree_node_creation(self):
    node = TreeNode(10, "value_10")
    assert node.key == 10
    assert node.value == "value_10"
    assert node.left is None
    assert node.right is None
    assert node.height == 1


class TestBinarySearchTree:
  def test_empty_tree(self):
    bst = BinarySearchTree()
    assert bst.root is None
    assert bst.height() == 0
    assert bst.is_balanced() == True
  
  def test_insert_and_search(self):
    bst = BinarySearchTree()
    
    bst.insert(10, "value_10")
    bst.insert(5, "value_5")
    bst.insert(15, "value_15")
    bst.insert(3, "value_3")
    bst.insert(7, "value_7")
      
    assert bst.search(10) == "value_10"
    assert bst.search(5) == "value_5"
    assert bst.search(15) == "value_15"
    assert bst.search(3) == "value_3"
    assert bst.search(7) == "value_7"
      
    assert bst.search(20) is None
    assert bst.search(1) is None
    
  def test_insert_duplicate_key(self):
    bst = BinarySearchTree()
    bst.insert(10, "value_10")
    bst.insert(10, "new_value_10")
    
    assert bst.search(10) == "new_value_10"
  
  def test_delete(self):
    bst = BinarySearchTree()
    
    bst.insert(10, "10")
    bst.insert(5, "5")
    bst.insert(15, "15")
    bst.insert(3, "3")
    bst.insert(7, "7")
    bst.insert(12, "12")
    
    assert bst.search(5) == "5"
    
    bst.delete(15)
    assert bst.search(15) is None
    assert bst.search(12) == "12"
    
    bst.delete(3)
    assert bst.search(3) is None
    
    bst.delete(5)
    assert bst.search(5) is None
    assert bst.search(3) is None
    assert bst.search(7) == "7"
    
    bst.delete(10)
    assert bst.search(10) is None
  
  def test_height(self):
    bst = BinarySearchTree()
    
    assert bst.height() == 0
    
    bst.insert(10, "10")
    assert bst.height() == 1
    
    bst.insert(5, "5")
    assert bst.height() == 2
    
    bst.insert(15, "15")
    assert bst.height() == 2
    
    bst.insert(3, "3")
    assert bst.height() == 3
    
    bst.insert(7, "7")
    assert bst.height() == 3
    
    bst.insert(12, "12")
    assert bst.height() == 3
    
    bst.insert(20, "20")
    assert bst.height() == 3
    
    bst.insert(1, "1")
    assert bst.height() == 4
  
  def test_is_balanced(self):
    bst = BinarySearchTree()
    
    assert bst.is_balanced() == True
    
    bst.insert(10, "10")
    bst.insert(5, "5")
    bst.insert(15, "15")
    assert bst.is_balanced() == True
    
    bst.insert(3, "3")
    assert bst.is_balanced() == True
    
    bst.insert(1, "1")
    assert bst.is_balanced() == False
  

  def test_comprehensive(self):
    bst = BinarySearchTree()
    
    elements = [(50, "50"), (30, "30"), (70, "70"), (20, "20"), 
                (40, "40"), (60, "60"), (80, "80"), (10, "10"), 
                (25, "25"), (35, "35"), (45, "45"), (55, "55"), 
                (65, "65"), (75, "75"), (85, "85")]
    
    for key, value in elements:
        bst.insert(key, value)
    
    assert bst.height() == 4
    
    assert bst.is_balanced() == True
    
    for key, value in elements:
      assert bst.search(key) == value
    
    bst.delete(50)
    assert bst.search(50) is None
    
    remaining_elements = [(30, "30"), (70, "70"), (20, "20"), (40, "40"), 
                          (60, "60"), (80, "80"), (10, "10"), (25, "25"), 
                          (35, "35"), (45, "45"), (55, "55"), (65, "65"), 
                          (75, "75"), (85, "85")]
    
    for key, value in remaining_elements:
      assert bst.search(key) == value


if __name__ == "__main__":
    pytest.main()