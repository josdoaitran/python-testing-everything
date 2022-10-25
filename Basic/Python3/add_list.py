first  = [11, 12, 13, 14, 15, 16]
second = [71, 77, 89, 51, 90, 59]
# Add two lists element-wise using zip() & sum()
final_list = [sum(value) for value in zip(first, second)]
print(final_list)

# ref https://thispointer.com/add-two-lists-element-wise-in-python/

def calculate_sum_list(data):
  tc_data = [sum(value) for value in zip(*data)]
  print(tc_data)
  return tc_data

calculate_sum_list([first, secound])
calculate_sum_list([[1,3], [4,9]])
