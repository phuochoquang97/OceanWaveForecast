# IF YOU WANT TO USE THIS SCRIPT,
# UNCOMMENT ALL AND SPECIFY THE FILE PATH HERE :

# file_path = YOUR_PATH

"""

import netCDF4 as nc
import pandas as pd
from sklearn.model_selection import train_test_split

output_folder = 'data5'

try:
    with nc.Dataset(file_path, 'r') as file:
        # Initialize an empty dictionary to store variable data
        variable_data = {}

        variables_name = list(file.variables.keys())[3:]

        # Iterate over all variables in the NetCDF file
        for var_name in variables_name:
            # Get the variable object
            var = file.variables[var_name]

            # Fill masked values with NaN
            values = var[:]
            values = values.filled(fill_value=float('nan'))

            # Reshape the array to 1D if it's multi-dimensional
            if values.ndim > 1:
                values = values.flatten()

            # Store variable data in the dictionary
            variable_data[var_name] = values

        # Create a DataFrame from the variable data dictionary
        df = pd.DataFrame(variable_data)

        # Drop rows with NaN values
        df.dropna(inplace=True)

        # Separate the column 'VPED' as the target value
        test_size = 0.2  # Adjust as needed

        # Perform the random split
        df_train, df_test = train_test_split(
    df, test_size=test_size, random_state=42
)

        # Sample 1% for manageable size

        df_train = df_train.sample(frac=0.01, random_state=42)
        df_test = df_test.sample(frac=0.01, random_state=42)

        # Write to CSV files
        df_train.to_csv(output_folder + '/train.csv', index=False)
        df_test.to_csv(output_folder + '/test.csv', index=False)

        print("Data processed and saved successfully.")

except Exception as e:
    print(f"Error: {e}")

    """
