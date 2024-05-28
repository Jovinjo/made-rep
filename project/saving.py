import os

def save_dataframe_to_csv(df, name_csv):
    try:
        save_dir = "../data"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print(f"{save_dir} Directory Created")

        full_path = os.path.join(save_dir,name_csv)
        df.to_csv(full_path, index=False)
        
        print(f"Saved Dataframe as CSV to {full_path}")

    except Exception as e:
        print(f"An error occured when saving dataframe to csv: {e}")
        return None