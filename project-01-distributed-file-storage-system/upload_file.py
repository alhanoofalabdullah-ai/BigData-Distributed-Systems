import shutil

source_file = "uploads/sample-document.pdf"

destination = "storage-nodes/node-01/sample-document.pdf"

shutil.copy(source_file, destination)

print("File uploaded successfully")
