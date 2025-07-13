# Data Versioning with DVC: Concepts and Workflows

## Introduction
DVC (Data Version Control) enables versioning of large files and datasets alongside code in Git repositories. This document explains core concepts and demonstrates a practical workflow for managing data versions.

## Core Concepts

### The Versioning Analogy
Imagine a warehouse system where:
- **Items** (data files) are stored in storage areas (remote storage)
- **Counters** (DVC) manage item storage/retrieval
- **Coupons** (DVC pointers) reference stored items
- Only with the correct coupon can you retrieve specific versions of items

Similarly, DVC:
1. Stores large files remotely (S3, GCS, etc.)
2. Creates small .dvc pointer files tracked by Git
3. Enables version-specific data retrieval using Git commits

## Workflow: Implementing Data Versioning

### Initial Setup
1. Create and clone a Git repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Create initial code and data:
   ```python
   # mycode.py
   import pandas as pd
   df = pd.DataFrame({'data': [1, 2, 3]})
   df.to_csv('data/data.csv')
   ```

3. Commit initial code to Git:
   ```bash
   git add mycode.py
   git commit -m "Initial code"
   git push
   ```

4. Initialize DVC:
   ```bash
   pip install dvc
   dvc init
   ```

### Versioning Data
5. Configure remote storage (local S3 simulation):
   ```bash
   mkdir s3
   dvc remote add -d myremote s3
   ```

6. Add data to DVC control:
   ```bash
   dvc add data/
   git rm -r --cached 'data'
   git commit -m "Stop tracking data with Git"
   ```

7. Commit DVC metadata:
   ```bash
   git add .gitignore data.dvc
   dvc commit
   dvc push
   git commit -m "Add initial data version"
   git push
   ```

### Updating Data
8. Modify and update data:
   ```python
   # mycode.py (updated)
   df = pd.concat([df, pd.DataFrame({'data': [4]})])
   df.to_csv('data/data.csv')
   ```

9. Commit changes:
   ```bash
   dvc status  # Check changes
   dvc commit  # Create new data version
   dvc push    # Push to remote storage
   git add data.dvc
   git commit -m "Update to data version 2"
   git push
   ```

### Retrieving Previous Versions
10. Revert to specific version:
    ```bash
    git checkout <commit-hash>  # Get historical .dvc pointer
    dvc checkout                 # Retrieve corresponding data
    ```

## Why Remote Storage?
- **Distributed Access**: Enables team collaboration
- **Data Safety**: Prevents loss if local storage fails
- **Scalability**: Handles large datasets beyond Git's capabilities
- **Efficiency**: Only transfers changed data chunks

## Command Reference
| Command | Purpose |
|---------|---------|
| `dvc init` | Initialize DVC in repository |
| `dvc add <file>` | Place file under DVC control |
| `dvc commit` | Save changes to DVC cache |
| `dvc push` | Upload data to remote storage |
| `dvc pull` | Download data from remote |
| `dvc checkout` | Retrieve data matching current .dvc pointer |
