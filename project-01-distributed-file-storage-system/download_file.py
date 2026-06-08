import shutil

source_file = "storage-nodes/node-01/sample-document.pdf"

destination = "downloads/sample-document.pdf"

shutil.copy(source_file, destination)

print("File downloaded successfully")
