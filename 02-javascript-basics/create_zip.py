import os
import zipfile

def create_zip(output_filename, directory):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zipf.write(file_path, arcname)

if __name__ == '__main__':
    project_dir = 'javascript-basics'  # Der Ordnername des Projekts
    output_file = 'submission.zip'
    create_zip(output_file, project_dir)
    print(f"ZIP-Datei '{output_file}' wurde erfolgreich erstellt.")
