import os
import requests
import json
import pandas as pd
from typing import Union, List

def upload_audio_file(file_path: str) -> Union[dict, None]:
    """
    Upload a single audio file to the API and return the response.
    """
    url = "http://27.111.72.61:8001/upload"
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': f"Upload failed for {file_path}, status code: {response.status_code}"}
    except Exception as e:
        return {'error': f"Exception for {file_path}: {str(e)}"}

def save_response_to_json_and_excel(response_data: Union[dict, list], base_file_name: str):
    """
    Save response data to both JSON and Excel formats using the base file name.
    """
    upload_dir = 'upload'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    json_path = os.path.join(upload_dir, f"{base_file_name}.json")
    with open(json_path, 'w') as json_file:
        json.dump(response_data, json_file, indent=4)

    if isinstance(response_data, list) and len(response_data) > 0 and isinstance(response_data[0], dict):
        df = pd.DataFrame(response_data)
        excel_path = os.path.join(upload_dir, f"{base_file_name}.xlsx")
        df.to_excel(excel_path, index=False)
        print(f"Saved: {json_path}, {excel_path}")
    else:
        print(f"Saved only JSON due to unexpected format: {json_path}")

def process_audio_files(audio_files: Union[str, List[str]]):
    """
    Process audio file(s): upload and save results individually.
    """
    if isinstance(audio_files, str):
        audio_files = [audio_files]

    for file_path in audio_files:
        print(f"\nUploading: {file_path}")
        response = upload_audio_file(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        save_response_to_json_and_excel(response, base_file_name=base_name)

# ------------------ MAIN ------------------ #
if __name__ == "__main__":
    # Specify test files
    test_single = "77524001.mp3"
    test_multiple = ["77524001.mp3", "79729302.mp3"]

    # Run test for single file
    print("=== Testing Single File ===")
    process_audio_files(test_single)

    # Run test for multiple files
    print("\n=== Testing Multiple Files ===")
    process_audio_files(test_multiple)
