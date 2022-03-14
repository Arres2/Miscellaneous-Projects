import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    calculations = {} 
    mod = [list[0:3],list[3:6],list[6:9]] 
    arr = np.array(mod)

    calculations["mean"] = [

      [arr[:, 0].mean(),arr[:, 1].mean(),arr[:,2].mean()], 
      [arr[0, :].mean(),arr[1, :].mean(),arr[2, :].mean()]
      
      , arr.mean()]

    calculations["variance"] = [
      [arr[:, 0].var(),arr[:, 1].var(),arr[:,2].var()],[arr[0, :].var(),arr[1, :].var(),arr[2, :].var()],arr.var()]

    calculations["standard deviation"] = [
      
      [arr[:, 0].std(),arr[:, 1].std(),arr[:,2].std()], 
      [arr[0, :].std(),arr[1, :].std(),arr[2, :].std()]
      
      , arr.std()]

    calculations["max"] = [
      
      [arr[:, 0].max(),arr[:, 1].max(),arr[:,2].max()], 
      [arr[0, :].max(),arr[1, :].max(),arr[2, :].max()]
      
      , arr.max()]

    calculations["min"] = [
      
      [arr[:, 0].min(),arr[:, 1].min(),arr[:,2].min()], 
      [arr[0, :].min(),arr[1, :].min(),arr[2, :].min()]
      
      , arr.min()]

    calculations["sum"] = [
      
      [arr[:, 0].sum(),arr[:, 1].sum(),arr[:,2].sum()], 
      [arr[0, :].sum(),arr[1, :].sum(),arr[2, :].sum()]
      
      , arr.sum()]

  return calculations