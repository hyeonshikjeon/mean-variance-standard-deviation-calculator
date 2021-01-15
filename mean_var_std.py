import numpy as np

def calculate(list):
  temp_arr= []
  calculations = {}

  try:
    temp_arr = np.array(list).reshape(3,3)

  except ValueError:
    raise ValueError('List must contain nine numbers.')

  m = [[np.mean(temp_arr[:,0]), np.mean(temp_arr[:,1]), np.mean(temp_arr[:,2])],
      [np.mean(temp_arr[0,:]), np.mean(temp_arr[1,:]), np.mean(temp_arr[2,:])],
      np.mean(temp_arr)]

  v = [[np.var(temp_arr[:,0]), np.var(temp_arr[:,1]), np.var(temp_arr[:,2])],
      [np.var(temp_arr[0,:]), np.var(temp_arr[1,:]), np.var(temp_arr[2,:])],
      np.var(temp_arr)]

  std = [[np.std(temp_arr[:,0]), np.std(temp_arr[:,1]), np.std(temp_arr[:,2])],
      [np.std(temp_arr[0,:]), np.std(temp_arr[1,:]), np.std(temp_arr[2,:])],
      np.std(temp_arr)]

  arr_max = [[np.max(temp_arr[:,0]), np.max(temp_arr[:,1]), np.max(temp_arr[:,2])],
      [np.max(temp_arr[0,:]), np.max(temp_arr[1,:]), np.max(temp_arr[2,:])],
      np.max(temp_arr)]

  arr_min = [[np.min(temp_arr[:,0]), np.min(temp_arr[:,1]), np.min(temp_arr[:,2])],
      [np.min(temp_arr[0,:]), np.min(temp_arr[1,:]), np.min(temp_arr[2,:])],
      np.min(temp_arr)]
  s = [[np.sum(temp_arr[:,0]), np.sum(temp_arr[:,1]), np.sum(temp_arr[:,2])],
      [np.sum(temp_arr[0,:]), np.sum(temp_arr[1,:]), np.sum(temp_arr[2,:])],
      np.sum(temp_arr)]

  calculations['mean'] = m
  calculations['variance'] = v
  calculations['standard deviation'] = std
  calculations['max'] = arr_max
  calculations['min'] = arr_min
  calculations['sum'] = s

  return calculations
