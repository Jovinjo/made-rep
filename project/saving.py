import os

def save_dataframe_to_csv(df, name_csv):
    try:
        # Define the directory where the CSV files will be stored
        save_dir = "../data"

        # Check if the directory exists, and if not, create it
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print(f"{save_dir} Directory Created")

        # Construct the full path to the CSV file
        full_path = os.path.join(save_dir,name_csv)

        # Save the dataframe to a CSV file at the specified path
        df.to_csv(full_path, index=False)
        
        print(f"Saved Dataframe as CSV to {full_path}")

    except Exception as e:
        print(f"An error occured when saving dataframe to csv: {e}")
        return None