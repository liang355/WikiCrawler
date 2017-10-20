from WikiTransformer import transform


FolderName = "CrawledPages"
NumFilesToProcess = 11


# API
def run_transformer(folder_name, num_files_to_process):
    transform(folder_name, num_files_to_process)


# run transform function for testing
transform(FolderName, NumFilesToProcess)
