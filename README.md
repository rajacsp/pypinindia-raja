# pypinindia

A Python library to find Indian pincodes and uncover related geographic details easily.

[![Python Support](https://img.shields.io/pypi/pyversions/pypinindia.svg)](https://pypi.org/project/pypinindia/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Features

- **Optimized Performance**: Utilizes `lru_cache` for efficient singleton instance management, ensuring faster lookups.
- **Refactored Codebase**: Improved internal code structure with helper methods for better maintainability and reduced duplication.
- **Comprehensive Pincode Database**: Complete Indian pincode data with office information
- **Multiple Lookup Methods**: Search by pincode, state, district, or office name
- **Modern Python API**: Clean, type-hinted interface with both functional and object-oriented approaches
- **Command Line Interface**: Full-featured CLI tool for pincode operations
- **Fast Lookups**: Efficient pandas-based data operations
- **Error Handling**: Comprehensive exception handling with meaningful error messages
- **Well Tested**: Extensive test suite with high coverage
- **Type Hints**: Full type annotation support for better IDE experience

## Installation

```bash
pip install pypinindia
```

### Dependencies

- Python 3.8+
- pandas >= 1.0.0

### Optional Dependencies

For development:
```bash
pip install pypinindia[dev]
```

## Quick Start

```python
from pinin import get_pincode_info, get_state, PincodeData

# Quick pincode lookup
info = get_pincode_info("110001")
print(f"Found {len(info)} offices for pincode 110001")

# Get specific information
state = get_state("110001")
print(f"State: {state}")

# Using PincodeData class
pincode_data = PincodeData()
district = pincode_data.get_district("110001")
print(f"District: {district}")
```

## Usage Examples

### Basic Pincode Lookup

```python
from pinin import get_pincode_info, get_state, get_district, get_taluk, get_offices

# Get complete information for a pincode
pincode = "110001"
info = get_pincode_info(pincode)

for office in info:
    print(f"Office: {office['officename']}")
    print(f"Type: {office['officetype']}")
    print(f"Delivery: {office['Deliverystatus']}")
    print(f"State: {office['statename']}")
    print(f"District: {office['districtname']}")
    print("---")

# Quick lookups
state = get_state("110001")          # Returns: DELHI
district = get_district("110001")    # Returns: Central Delhi
taluk = get_taluk("110001")         # Returns: New Delhi
offices = get_offices("110001")      # Returns: List of office names
```

### Search Operations

```python
from pinin import search_by_state, search_by_district, get_states, get_districts

# Search pincodes by state
delhi_pincodes = search_by_state("Delhi")
print(f"Found {len(delhi_pincodes)} pincodes in Delhi")

# Search pincodes by district
mumbai_pincodes = search_by_district("Mumbai", "Maharashtra")
print(f"Found {len(mumbai_pincodes)} pincodes in Mumbai")

# Get all states
states = get_states()
print(f"Total states/territories: {len(states)}")

# Get districts in a state
districts = get_districts("Tamil Nadu")
print(f"Districts in Tamil Nadu: {len(districts)}")
```

### Using PincodeData Class

```python
from pinin import PincodeData

# Create instance
pincode_data = PincodeData()

# Get statistics
stats = pincode_data.get_statistics()
print(f"Total records: {stats['total_records']:,}")
print(f"Unique pincodes: {stats['unique_pincodes']:,}")
print(f"Unique states: {stats['unique_states']}")

# Search by office name
airport_offices = pincode_data.search_by_office("Airport")
print(f"Found {len(airport_offices)} offices with 'Airport' in name")

# Use custom data file
custom_data = PincodeData("/path/to/custom/pincode_data.csv")
```

### Error Handling

```python
from pinin import get_state
from pinin.exceptions import InvalidPincodeError, DataNotFoundError

try:
    state = get_state("12345")  # Invalid format
except InvalidPincodeError as e:
    print(f"Invalid pincode: {e}")

try:
    state = get_state("999999")  # Doesn't exist
except DataNotFoundError as e:
    print(f"Pincode not found: {e}")
```

## Command Line Interface

The library includes a comprehensive CLI tool:

```bash
# Basic pincode lookup
pypinindia 110001

# Get specific information
pypinindia --state 110001
pypinindia --district 110001
pypinindia --offices 110001

# Search operations
pypinindia --search-state "Delhi"
pypinindia --search-district "Mumbai" --in-state "Maharashtra"

# List operations
pypinindia --list-states
pypinindia --list-districts "Tamil Nadu"

# Statistics
pypinindia --stats

# JSON output
pypinindia 110001 --json

# Verbose output
pypinindia 110001 --verbose
```

### CLI Examples

```bash
# Get complete information for a pincode
$ pypinindia 110001
Officename: Connaught Place S.O
Pincode: 110001
Officetype: S.O
Deliverystatus: Delivery
Divisionname: New Delhi Central
Regionname: Delhi
Circlename: Delhi
Taluk: New Delhi
Districtname: Central Delhi
Statename: DELHI

# Get just the state
$ pypinindia --state 110001
DELHI

# Search pincodes in a state
$ pypinindia --search-state "Goa"
403001
403002
403101
...

# Get statistics
$ pypinindia --stats
Total Records: 154,725
Unique Pincodes: 19,300
Unique States: 36
Unique Districts: 640
Unique Offices: 154,725
```

## API Reference

### Functions

#### `get_pincode_info(pincode: Union[str, int]) -> List[Dict[str, Any]]`
Get complete information for a pincode.

**Parameters:**
- `pincode`: The pincode to lookup (string or integer)

**Returns:** List of dictionaries containing pincode information

#### `get_state(pincode: Union[str, int]) -> str`
Get state name for a pincode.

#### `get_district(pincode: Union[str, int]) -> str`
Get district name for a pincode.

#### `get_taluk(pincode: Union[str, int]) -> str`
Get taluk name for a pincode.

#### `get_offices(pincode: Union[str, int]) -> List[str]`
Get office names for a pincode.

#### `search_by_state(state_name: str) -> List[str]`
Get all pincodes for a state.

#### `search_by_district(district_name: str, state_name: Optional[str] = None) -> List[str]`
Get all pincodes for a district.

#### `get_states() -> List[str]`
Get list of all states.

#### `get_districts(state_name: Optional[str] = None) -> List[str]`
Get list of all districts, optionally filtered by state.

### Classes

#### `PincodeData(data_file: Optional[str] = None)`
Main class for pincode data operations.

**Methods:**
- `get_pincode_info(pincode)`: Get complete pincode information
- `get_state(pincode)`: Get state name
- `get_district(pincode)`: Get district name
- `get_taluk(pincode)`: Get taluk name
- `get_offices(pincode)`: Get office names
- `search_by_state(state_name)`: Search by state
- `search_by_district(district_name, state_name=None)`: Search by district
- `search_by_office(office_name)`: Search by office name (partial match)
- `get_states()`: Get all states
- `get_districts(state_name=None)`: Get all districts
- `get_statistics()`: Get dataset statistics

### Exceptions

#### `InvalidPincodeError`
Raised when an invalid pincode format is provided.

#### `DataNotFoundError`
Raised when no data is found for a pincode.

#### `DataLoadError`
Raised when the pincode data fails to load.

## Data Format

The library expects CSV data with the following columns:

- `pincode`: 6-digit pincode
- `officename`: Name of the post office
- `officetype`: Type of office (S.O, B.O, etc.)
- `Deliverystatus`: Delivery status (Delivery, Non-Delivery)
- `divisionname`: Postal division name
- `regionname`: Postal region name
- `circlename`: Postal circle name
- `taluk`: Taluk/Tehsil name
- `districtname`: District name
- `statename`: State/Territory name

## Development

### Setup Development Environment

```bash
git clone https://github.com/kactlabs/pypinindia.git
cd pypinindia
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=pinin --cov-report=html
```

### Code Formatting

```bash
black pinin tests examples
```

### Type Checking

```bash
mypy pinin
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.8
- **Fixed**: Incremented version to resolve PyPI "File already exists" error.

### v0.1.7
- **Performance Enhancement**: Implemented `lru_cache` for `_get_default_instance` to ensure `PincodeData` is a singleton and loaded only once, optimizing performance for repeated calls to convenience functions.
- **Code Refactoring**: Refactored `PincodeData` methods (`get_state`, `get_district`, `get_taluk`, `get_offices`) to use a common helper method `_get_info_field` for improved code reusability and maintainability.
- **Code Clean-up**: Removed redundant global variable `_default_pincode_data` and duplicate import statements (`os`, `re`).
- **Type Hinting**: Ensured type hint compatibility with `mypy` by explicitly casting return types where necessary.

### v0.1.6
- **Complete rewrite with modern Python practices**
- Added comprehensive API with both functional and OOP interfaces
- Added full CLI tool with extensive options
- Added comprehensive test suite with high coverage
- Added type hints throughout the codebase
- Added proper exception handling with custom exceptions
- Added search functionality by state, district, and office name
- Added statistics and data exploration features
- Added examples and comprehensive documentation
- Migrated from setup.py to modern pyproject.toml
- Added support for custom data files
- Added JSON output support in CLI
- Performance improvements with pandas-based operations

### v0.1.2 (Legacy)
- Basic pincode lookup functionality
- Simple API with limited features

## Data Source

The pincode data is sourced from India Post and contains comprehensive information about Indian postal codes, offices, and geographical divisions.

## Acknowledgments

- India Post for providing the comprehensive pincode database
- The Python community for excellent libraries like pandas
- Contributors and users who help improve this library

## Support

If you encounter any issues or have questions, please:

1. Check the [documentation](https://github.com/kactlabs/pypinindia)
2. Search existing [issues](https://github.com/kactlabs/pypinindia/issues)
3. Create a new issue if needed

For general questions, you can also reach out via email: raja.csp@gmail.com
