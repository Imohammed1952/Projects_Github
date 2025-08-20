import pandas as pd
import numpy as np

# Load the Excel file
file_path = 'Data/compressed_data_with_labels.xlsx'  
data = pd.read_excel(file_path)

# Determine the standard deviation of the Gaussian noise
std_dev = 0.03  # Adjust this based on how much noise you want to add

# Add Gaussian noise to the numeric data columns only
for column in data.columns[:-1]:  # This excludes the last column assuming it's 'Label'
    data[column] += np.random.normal(0, std_dev, size=data[column].shape)

# Save the modified data back to a new Excel file
output_file_path = 'Data/compressed_data_with_noise.xlsx'  
data.to_excel(output_file_path, index=False)





# import pandas as pd
# import numpy as np

# # Load the Excel file
# file_path = 'Data/compressed_data_with_labels.xlsx'  
# data = pd.read_excel(file_path)

# # Exclude the 'Label' column when calculating the mean
# numeric_data = data[data.columns[:-1]]  # Assuming 'Label' is the last column
# means = numeric_data.mean(axis=0)

# # Determine the standard deviation of the Gaussian noise
# std_dev = 0.1  # Adjust this based on how much noise you want to add

# # Add Gaussian noise to the numeric data columns only
# for column in numeric_data.columns:
#     numeric_data[column] += np.random.normal(0, std_dev, size=numeric_data[column].shape)

# # Combine the numeric data with the labels again
# data_with_noise = pd.concat([numeric_data, data[['Label']]], axis=1)

# # Determine the number of new data points to add
# num_new_points = 50  # Adjust this to how many new points you want to add

# # Create new data points with Gaussian noise
# new_points = np.random.normal(means, std_dev, size=(num_new_points, len(numeric_data.columns)))

# # Create a DataFrame from the new points
# new_points_df = pd.DataFrame(new_points, columns=numeric_data.columns)

# # Add the label column to the new_points_df with the file name
# file_name = 'Noise'  # Replace with the actual file name or label you want to use
# new_points_df['Label'] = file_name

# # Append the new points to the original data
# data_with_new_points_and_noise = pd.concat([data_with_noise, new_points_df], ignore_index=True)

# # Save the modified data back to a new Excel file
# output_file_path = 'Data/compressed_data_with_noise.xlsx'  
# data_with_new_points_and_noise.to_excel(output_file_path, index=False)
