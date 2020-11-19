import subprocess
import numpy as np

data_input = np.zeros((20,20))
data_input[-1, :]=1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

subprocess.run(["python", "sagital_brain.py"])

result = np.loadtxt('brain_average.csv', delimiter=',')

expected = np.zeros(20)
expected[-1] =  1

np.testing.assert_array_equal(result, expected)
