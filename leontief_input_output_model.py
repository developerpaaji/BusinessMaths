import numpy as np
# We have matrix of total production and total consumption by 2 different sectors
# and we have to find consumption ratios
matrix = np.array([[16,20,4],[8,40,32]])
gross_output = np.sum(matrix,axis=1)
final_demand = matrix[:,-1]
industries = matrix[:,:-1]
consumption_ratios = industries/gross_output
print(consumption_ratios)
# We have consumption ratios  and new final demand
# and we have to find new gross output
new_final_demand = np.reshape([18,44],(2,1))
# Using formula (I-R)-1*D=X
inverse = np.linalg.inv(np.eye(consumption_ratios.shape[0])-consumption_ratios)
new_gross_output = np.dot(inverse,new_final_demand)
print(new_gross_output)