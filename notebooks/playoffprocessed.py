import pandas as pd

# Define input and output file names
# Use the actual filename from the error log
input_file = 'Playoffs_edited.csv'
output_file = 'playoff_processed.csv'

try:
    # --- Load Data ---
    # Read the CSV, using the *first* column (index 0) as the DataFrame index.
    # This column is the one pandas initially calls 'Unnamed: 0' based on the log.
    df = pd.read_csv(input_file, index_col=0)
    print(f"Successfully loaded {input_file} using the first column as index.")
    print(f"Columns after loading with index_col=0: {df.columns.tolist()}")
    print(f"Index name after loading: {df.index.name}") # Should be 'Unnamed: 0' initially

    # --- Process Data ---

    # 1. Rename the index (which came from the first column 'Unnamed: 0') to 'playoff_index'
    df.index.name = 'playoff_index'
    print(f"Renamed index to: '{df.index.name}'")

    # 2. Reset the index to make 'playoff_index' a regular column
    df.reset_index(inplace=True)
    print("Reset index, 'playoff_index' is now a column.")
    print(f"Columns after reset_index: {df.columns.tolist()}")


    # 3. Drop the unwanted column (originally header 'Unnamed: 1')
    col_to_drop_name = 'Unnamed: 1'
    if col_to_drop_name in df.columns:
        df.drop(columns=[col_to_drop_name], inplace=True)
        print(f"Dropped the unwanted column: '{col_to_drop_name}'")
    else:
        # This shouldn't happen if the error log was accurate, but good to check.
        print(f"Warning: Could not find the column '{col_to_drop_name}' to drop.")


    # 4. Split the 'year' column into 'season_start' and 'season_end'
    if 'year' in df.columns:
        df['year'] = df['year'].astype(str)
        try:
            df['season_start'] = df['year'].str.slice(0, 4)
            df['season_end'] = '20' + df['year'].str.slice(-2)
            # Optional check for format validity
            if not df['season_start'].str.match(r'^\d{4}$').all() or not df['season_end'].str.match(r'^\d{4}$').all():
                 print("Warning: Some values in 'year' column might not follow the 'YYYY-YY' format.")
        except Exception as e:
            print(f"Error processing 'year' column: {e}. Check format.")
            raise
        print("Split 'year' column into 'season_start' and 'season_end'")
    else:
        print("Error: 'year' column not found. Cannot split season years.")
        raise KeyError("'year' column missing")


    # 5. Rename remaining columns to lowercase
    rename_dict = {
        col: col.lower() for col in df.columns
        if col not in ['playoff_index', 'year', 'season_start', 'season_end'] and col.lower() != col
    }
    if rename_dict:
        df.rename(columns=rename_dict, inplace=True)
        print(f"Renamed other columns to lowercase: {list(rename_dict.keys())}")
    else:
        print("No other columns needed renaming to lowercase.")


    # 6. Define the final desired column order
    final_columns = [
        'playoff_index', 'season_start', 'season_end', 'season_type',
        'player_id', 'rank', 'player', 'team_id', 'team', 'gp', 'min',
        'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct', 'ftm', 'fta',
        'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl', 'blk', 'tov',
        'pf', 'pts', 'ast_tov', 'stl_tov'
    ]

    # 7. Select and reorder columns
    # Ensure 'year' column is dropped *after* splitting
    columns_to_select = [col for col in final_columns if col in df.columns]
    missing_cols = [col for col in final_columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: The following expected columns are missing after processing and won't be in the output: {missing_cols}")

    # Make sure the original 'year' column isn't included if it wasn't dropped implicitly
    if 'year' in columns_to_select:
         columns_to_select.remove('year')
         print("Ensured original 'year' column is not selected for final output.")

    df_final = df[columns_to_select]
    print(f"Selected and reordered columns. Final columns in output: {df_final.columns.tolist()}")


    print(f"\nProcessed Data Head:\n{df_final.head()}")

    # --- Save Output ---
    df_final.to_csv(output_file, index=False, float_format='%.18f')
    print(f"\nSuccessfully processed data and saved to {output_file}. Shape: {df_final.shape}")

except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found. Please make sure it exists and the path is correct.")
except KeyError as e:
    print(f"Error: A required column is missing or could not be processed correctly. Missing/Problem column: {e}")
    print("Please check if the input CSV file structure matches expectations.")
except ValueError as e: # Catch explicit ValueErrors
     print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    import traceback
    traceback.print_exc()