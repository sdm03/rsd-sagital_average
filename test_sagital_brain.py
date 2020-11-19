import subprocess
import numpy as np

"""Script to automate git bisect process"""

# Create and save test data
data_input = np.zeros((20,20))
data_input[-1, :]=1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

# Use subprocess to call python script (invoking default input params)
subprocess.run(["python", "sagital_brain.py"])

# Load result
result = np.loadtxt('brain_average.csv', delimiter=',')

# Expected output
expected = np.zeros(20)
expected[-1] =  1

# Assert that the two arrays are the same
np.testing.assert_array_equal(result, expected)
