""" laws of the jungle """

def calculate_food_for_bugs(world):
  """ one food can map to multiple bugs, these bugs will share the food they are on """
  for cell in world._food_cells.items():
    total_bug_size = 0
    for bug in cell.bugs.items():
      total_bug_size += bug._size
    total_food = cell.food.size
    food_per_size = total_food / total_bug_size
    for bug in cell.bugs.items():
      bug.food_supply = bug.size * food_per_size
