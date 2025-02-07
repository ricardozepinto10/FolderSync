import os
import shutil
import time
import hashlib
import argparse
import logging


def calculate_file_checksum(file_path):
    """Calculate MD5 checksum for file content."""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
    except FileNotFoundError:
        return None
    return hasher.hexdigest()


def sync_folders(source, replica):
    """Synchronize source folder with replica folder."""
    # Sync files and directories from source to replica
    for root, dirs, files in os.walk(source):
        relative_path = os.path.relpath(root, source)
        target_path = os.path.join(replica, relative_path)

        # Ensure directories in source exist in replica
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            logging.info(f"Created directory: {target_path}")

        # Sync files
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)

            # Check if the file needs copying or updating
            if not os.path.exists(target_file) or calculate_file_checksum(source_file) != calculate_file_checksum(target_file):
                shutil.copy2(source_file, target_file)
                logging.info(f"Copied/Updated file: {target_file}")

    # Remove extra files and directories from replica
    for root, dirs, files in os.walk(replica, topdown=False):
        relative_path = os.path.relpath(root, replica)
        source_path = os.path.join(source, relative_path)

        # Remove files not in source
        for file in files:
            target_file = os.path.join(root, file)
            if not os.path.exists(os.path.join(source_path, file)):
                os.remove(target_file)
                logging.info(f"Removed file: {target_file}")

        # Remove empty directories not in source
        for dir in dirs:
            target_dir = os.path.join(root, dir)
            if not os.path.exists(os.path.join(source_path, dir)):
                shutil.rmtree(target_dir)
                logging.info(f"Removed directory: {target_dir}")


def main():
    parser = argparse.ArgumentParser(description="Synchronize source and replica folders.")
    parser.add_argument("--source", required=True, help="Path to the source folder")
    parser.add_argument("--replica", required=True, help="Path to the replica folder")
    parser.add_argument("--interval", type=int, required=True, help="Synchronization interval in seconds")
    parser.add_argument("--log", required=True, help="Path to the log file")

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(args.log),
            logging.StreamHandler()
        ]
    )

    logging.info("Starting folder synchronization...")

    while True:
        try:
            sync_folders(args.source, args.replica)
            logging.info("Synchronization completed.")
        except Exception as e:
            logging.error(f"Error during synchronization: {e}")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
