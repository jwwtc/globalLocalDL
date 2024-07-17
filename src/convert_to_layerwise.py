import pandas as pd
import numpy as np
import sys
import os

def generate_fabricated_data(input_file):
    # Read the input file
    data = pd.read_csv(input_file, delimiter=',')

    # Extract the unique z values and sort them
    unique_z_values = sorted(data['z'].unique())

    # Identify the layers to keep (every 10th layer)
    layers_to_keep = unique_z_values[::10]

    # Function to format the floating-point numbers to 10 significant figures
    def format_float(val):
        return f"{val:.10f}"

    # Prepare the output data
    output_data = []
    for z_val in unique_z_values:
        layer_data = data[data['z'] == z_val]
        if z_val in layers_to_keep:
            # Keep the data as is
            for _, row in layer_data.iterrows():
                formatted_row = [format_float(row['x']), format_float(row['y']), format_float(row['z']),
                                 format_float(row['tm']), format_float(row['tl']), format_float(row['cr'])]
                output_data.append(formatted_row)
        else:
            # Convert to layerwise data (use mean of tm, tl, cr for the entire layer)
            tm_mean = layer_data['tm'].mean()
            tl_mean = layer_data['tl'].mean()
            cr_mean = layer_data['cr'].mean()
            for _, row in layer_data.iterrows():
                formatted_row = [format_float(row['x']), format_float(row['y']), format_float(row['z']),
                                 format_float(tm_mean), format_float(tl_mean), format_float(cr_mean)]
                output_data.append(formatted_row)

    # Convert the output data to a DataFrame
    output_df = pd.DataFrame(output_data, columns=['x', 'y', 'z', 'tm', 'tl', 'cr'])

    # Generate the output file name
    output_file = os.path.splitext(input_file)[0] + '-fab.txt'

    # Save the output data to a new file
    output_df.to_csv(output_file, index=False)
    print(f"Fabricated data saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fabricate_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    generate_fabricated_data(input_file)
