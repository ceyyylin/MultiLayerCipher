# Legacy Code (v1.0)
## About
This branch contains the initial, monolithic implementation of the Cipher Tool. It is kept here for **historical reference** and comparison purposes.

> **STATUS: DEPRECATED:**
> This version is no longer maintained.

## Architectural Improvements in v2.0
The project has undergone a complete refactoring to adhere to modern software engineering principles:
- **Modular Design:** Logic is now decoupled into `action.py`, `ciphers.py`, and `main.py`.
- **Dictionary Dispatch Pattern:** Replaced complex `if-else` chains with O(1) complexity lookups.
- **Wrapper Implementation:** Standardized function calls across different cipher types.
