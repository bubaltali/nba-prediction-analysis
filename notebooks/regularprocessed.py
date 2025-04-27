import pandas as pd

# Define input and output file names
input_file = 'Regular_Season.csv' # Assuming this is your input file name
output_file = 'regular_processed.csv'

try:
    # --- Load Data ---
    # Read the raw player stats data
    df = pd.read_csv(input_file)
    print(f"Successfully loaded {input_file}. Shape: {df.shape}")
    print(f"Original columns: {df.columns.tolist()}")

    # --- Process Data ---

    # 1. Rename 'Unnamed: 0' column
    df.rename(columns={'Unnamed: 0': 'regular_season_index'}, inplace=True)
    print("Renamed 'Unnamed: 0' to 'regular_season_index'")

    # 2. Split the 'year' column into 'season_start' and 'season_end'
    # Ensure the 'year' column is string type
    df['year'] = df['year'].astype(str)
    # Extract start year (first 4 characters)
    df['season_start'] = df['year'].str.slice(0, 4)
    # Extract end year (last 2 characters, prepend '20')
    df['season_end'] = '20' + df['year'].str.slice(-2)
    # Convert new year columns to numeric if desired (optional, depends on use case)
    # df['season_start'] = pd.to_numeric(df['season_start'])
    # df['season_end'] = pd.to_numeric(df['season_end'])
    print("Split 'year' column into 'season_start' and 'season_end'")

    # 3. Rename remaining columns to lowercase
    # Create a dictionary for renaming, excluding already processed/new columns
    rename_dict = {col: col.lower() for col in df.columns if col not in ['regular_season_index', 'year', 'season_start', 'season_end']}
    df.rename(columns=rename_dict, inplace=True)
    print(f"Renamed other columns to lowercase: {list(rename_dict.keys())}")


    # 4. Define the final desired column order
    final_columns = [
        'regular_season_index', 'season_start', 'season_end', 'season_type',
        'player_id', 'rank', 'player', 'team_id', 'team', 'gp', 'min',
        'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct', 'ftm', 'fta',
        'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl', 'blk', 'tov',
        'pf', 'pts', 'ast_tov', 'stl_tov'
    ]

    # 5. Select and reorder columns, drop the original 'year' column
    # Check if all expected final columns exist before selecting
    missing_cols = [col for col in final_columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: The following expected columns are missing after processing: {missing_cols}")
        # Adjust final columns to only include existing ones
        final_columns = [col for col in final_columns if col in df.columns]


    df_final = df[final_columns]
    print(f"Selected and reordered columns. Final columns: {df_final.columns.tolist()}")


    print(f"\nProcessed Data Head:\n{df_final.head()}")

    # --- Save Output ---
    # Save to CSV without the pandas index
    df_final.to_csv(output_file, index=False, float_format='%.18f') # Use float_format for high precision like example
    print(f"\nSuccessfully processed data and saved to {output_file}. Shape: {df_final.shape}")

except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found. Please make sure it exists and the path is correct.")
except KeyError as e:
    print(f"Error: A required column is missing during processing. Missing column: {e}")
    print("Please check if the input CSV file has all the expected columns (like 'year', 'Unnamed: 0', etc.).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

