import netCDF4 as nc
import pandas as pd
from sklearn.model_selection import train_test_split

# PUT YOUR FILE PATH HERE

file_path = r'C:\Users\betze\Downloads\mfwamglocep_2024021812_R20240219_12H.nc'

output_folder = 'data'

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
        y = df['VPED']
        X = df.drop(columns=['VPED'])
        
        # Perform train/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Sample one percent of the data
        X_train_sampled = X_train.sample(frac=0.01, random_state=42)
        X_test_sampled = X_test.sample(frac=0.01, random_state=42)
        y_train_sampled = y_train.sample(frac=0.01, random_state=42)
        y_test_sampled = y_test.sample(frac=0.01, random_state=42)
        
        # Write to CSV files
        X_train_sampled.to_csv(output_folder + '/X_train.csv', index=False)
        X_test_sampled.to_csv(output_folder + '/X_test.csv', index=False)
        y_train_sampled.to_csv(output_folder + '/y_train.csv', index=False, header=False)  # Exclude header for target
        y_test_sampled.to_csv(output_folder + '/y_test.csv', index=False, header=False)  # Exclude header for target
        
        print("Data processed and saved successfully.")
            
except Exception as e:
    print(f"Error: {e}")