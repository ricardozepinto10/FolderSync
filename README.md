FolderSync - Folder Synchronization Tool

Overview

FolderSync is a Python-based utility that synchronizes two folders: a source folder and a replica folder. The program ensures that the content of the replica folder is always a full, identical copy of the source folder.

Features

One-way synchronization from source to replica

Periodic synchronization based on user-defined intervals

Logging of all file operations (creation, copying, deletion) to both console and a log file

Error handling for smooth execution

How It Works

Checksum Comparison: Files are compared using MD5 checksums to detect changes.

Folder Traversal: The program recursively scans directories to identify differences.

Logging: All operations are logged to a user-specified log file.

Periodic Execution: Synchronization is performed at regular intervals specified by the user.

Setup and Usage

Prerequisites

Ensure you have Python 3.x installed on your system.

Installation

Clone the repository to your local machine:

git clone <repository-url>
cd FolderSync

Usage

Run the program with the following command:

python foldersync.py --source <source_folder_path> --replica <replica_folder_path> --time <interval_in_seconds> --log <log_file_path>

Command-Line Arguments

--source: Path to the source folder

--replica: Path to the replica folder

--time: Interval in seconds for periodic synchronization

--log: Path to the log file

Example

python foldersync.py --source "C:\Data\Source" --replica "D:\Data\Replica" --time 30 --log "C:\Logs\sync.log"

Key Components

calculate_file_checksum(file_path)

Calculates the MD5 checksum for a file to detect changes.

sync_folders(source, replica)

Synchronizes the replica folder to match the source folder.

main()

Handles argument parsing, logging setup, and periodic synchronization.

Error Handling

Catches FileNotFoundError during file operations

Logs unexpected errors to help with troubleshooting

Ensures synchronization continues even if an error occurs

Improvements

Here are potential enhancements for future versions:

Use file timestamps: Replace checksum comparisons with modification time checks for faster synchronization.

Multi-threading: Use ThreadPoolExecutor for parallel file operations.

Dry-run Mode: Allow previewing changes before execution.

Enhanced Logging: Include timestamps and log levels.

Exclusion Rules: Allow users to exclude specific files or directories.

Testing

To test the program:

Create test directories with various file types and subdirectories.

Modify files between synchronization intervals to observe behavior.

Check the log file for detailed operation reports.

License

This project is licensed under the MIT License. See LICENSE for details.

Contact

For issues or suggestions, please create a GitHub issue or reach out at <contact_email>.
