"""
Example module demonstrating the project structure.

This module shows how to use pandas and dotenv in the project.
"""

import os
import pandas as pd
from dotenv import load_dotenv


def main():
    """Main function to demonstrate the project setup."""
    # Load environment variables from .env file
    load_dotenv()

    # Get configuration from environment variables
    debug = os.getenv("DEBUG", "False") == "True"
    data_path = os.getenv("DATA_PATH", "./data")

    print("Project Configuration:")
    print(f"Debug mode: {debug}")
    print(f"Data path: {data_path}")

    # Example: Create a simple DataFrame
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "London", "Paris"],
    }
    df = pd.DataFrame(data)

    print("\nExample DataFrame:")
    print(df)


if __name__ == "__main__":
    main()
