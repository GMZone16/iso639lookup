# ISO639Lookup

A simple Python library to look up and convert **ISO 639 language codes**. This tool allows you to easily retrieve information about languages based on their ISO 639-1 (alpha-2), ISO 639-2/T (alpha-3 terminological), ISO 639-2/B (alpha-3 bibliographic), or ISO 639-3 (alpha-3) codes.

-----

## Features

  * **Flexible Lookup:** Search for ISO language information using any of the four common ISO 639 code types (part1, part2b, part2t, part3).
  * **Comprehensive Information Retrieval:** Get full details about an ISO code, including all its variations and the language name.
  * **Easy Conversion:** Convert between different ISO 639 code parts for a given language.
  * **Pandas Powered:** Leverages the power of Pandas DataFrames for efficient data handling.

-----

## Installation
```pip install git+https://github.com/GMZone16/iso639lookup```

OR

To use this library, you'll need `pandas` installed.

```bash
pip install pandas
```

Then, clone this repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/ISO639Lookup.git
cd ISO639Lookup
```

-----

## Usage

First, ensure you have the `iso-info.csv` file in a `resources` directory within your project, or update the `data_path` in the `ISO639Lookup` constructor to point to your CSV file.
Data may not be updated so get the tables from https://iso639-3.sil.org/code_tables/download_tables and place them in the resources directory. Then use the ipynb file.
```python
from iso639lookup import ISO639Lookup

# Initialize the lookup class
# Make sure 'resources/iso-info.csv' points to your data file
iso_lookup = ISO639Lookup(data_path="resources/iso-info.csv")

# Example: Get ISO 639-1 code for 'eng'
part1_code = iso_lookup.get_iso_part1("eng")
print(f"ISO 639-1 for 'eng': {part1_code}") # Expected: en

# Example: Get ISO 639-2/T code for 'en'
part2t_code = iso_lookup.get_iso_part2t("en")
print(f"ISO 639-2/T for 'en': {part2t_code}") # Expected: eng

# Example: Get full ISO information for 'fra'
french_info = iso_lookup.iso_lookup("fra")
print("\nFull info for 'fra':")
print(french_info)

# Example: Handling non-existent entries
non_existent_part1 = iso_lookup.get_iso_part1("xyz")
print(f"\nISO 639-1 for 'xyz': {non_existent_part1}") # Expected: NO PART 1

# Example: Handling existing entries where a specific part doesn't exist
# (e.g., some languages might only have part3 but not part1)
# Assuming 'zxx' (No linguistic content) might not have a part1 or part2t
zxx_part1 = iso_lookup.get_iso_part1("zxx")
print(f"\nISO 639-1 for 'zxx': {zxx_part1}")
```

-----

## API

The `ISO639Lookup` class provides the following methods:

  * `__init__(self, data_path="resources/iso-info.csv")`:

      * Initializes the lookup class, loading the ISO information from the specified CSV file.
      * `data_path` (str): The path to your CSV file containing ISO language data. Defaults to `"resources/iso-info.csv"`.

  * `isoRowFind(self, code)`:

      * (Internal method) Finds the row in the dataset corresponding to the given ISO code across 'part3', 'part2b', 'part2t', and 'part1' columns.
      * `code` (str): The ISO code to search for.
      * Returns: A Pandas DataFrame row if found, otherwise an empty DataFrame.

  * `get_iso_part1(self, code)`:

      * Retrieves the ISO 639-1 (alpha-2) code for the given input `code`.
      * `code` (str): An ISO code (part1, part2b, part2t, or part3).
      * Returns: The ISO 639-1 code (str), "Part 1 does not exist" (str) if the part is empty, or "NO PART 1" (str) if the entry is not found.

  * `get_iso_part2t(self, code)`:

      * Retrieves the ISO 639-2/T (alpha-3 terminological) code for the given input `code`.
      * `code` (str): An ISO code.
      * Returns: The ISO 639-2/T code (str), "Part 2t does not exist" (str) if the part is empty, or "ENTRY NON EXISTENT" (str) if the entry is not found.

  * `get_iso_part2b(self, code)`:

      * Retrieves the ISO 639-2/B (alpha-3 bibliographic) code for the given input `code`.
      * `code` (str): An ISO code.
      * Returns: The ISO 639-2/B code (str), "Part 2b does not exist" (str) if the part is empty, or "ENTRY NON EXISTENT" (str) if the entry is not found.

  * `get_iso_part3(self, code)`:

      * Retrieves the ISO 639-3 (alpha-3) code for the given input `code`.
      * `code` (str): An ISO code.
      * Returns: The ISO 639-3 code (str), "Part 3 does not exist" (str) if the part is empty, or "ENTRY NON EXISTENT" (str) if the entry is not found.

  * `iso_lookup(self, code)`:

      * Retrieves all available ISO information for the given input `code` as a JSON-like dictionary.
      * `code` (str): An ISO code.
      * Returns: A dictionary containing all ISO information for the language, or an empty dictionary if not found.

-----

## Data Source

The library relies on a CSV file named `iso-info.csv`. This file should contain columns corresponding to the different ISO 639 parts (e.g., `part1`, `part2b`, `part2t`, `part3`, along with other relevant language information). You'll need to provide this data file. A common source for such data is the official ISO 639-2 and ISO 639-3 registration authorities.

-----

## Contributing

Feel free to fork this repository, open issues, or submit pull requests. Any contributions to improve the project are welcome\!

-----

## License

MIT
