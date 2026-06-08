import shutil

source = "storage-nodes/node-01/sample-document.pdf"

replica1 = "storage-nodes/node-02/sample-document.pdf"

replica2 = "storage-nodes/node-03/sample-document.pdf"

shutil.copy(source, replica1)

shutil.copy(source, replica2)

print("Replication completed")
