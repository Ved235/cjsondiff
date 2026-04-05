# fastjsondiff

`fastjsondiff` is a Python package for high-performance JSON diffing inspired by [`jsondiff`](https://github.com/xlwings/jsondiff).
It is implemented in C++ using nanobind to make python bindings.
<img width="2885" height="1035" alt="image" src="https://github.com/user-attachments/assets/4b852e1c-a26c-4ca3-9f86-333b48d5eb50" />


## Status

- Recursive diff and similarity implemented in C++
- JSON/YAML loaders, dumpers, marshaling, and CLI support

## Development

```bash
python3 -m pip install -e . pytest
pytest
```
