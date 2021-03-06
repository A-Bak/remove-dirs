# rmdirs
---
Rmdirs is a python utility package for removing subdirectories. The files located in the subdirectories are preserved and they are moved into the root directory. The moved files are renamed according to the relative path from the root directory to the subdirectory they are located in. Any `'\'` and `'/'` separators on the relative path are replaced by the separator character. The separator character is `'_'` by default. 

If there are any naming conflicts that arise as a result of renaming moved files then a space and an integer in brackets is appended to the file name as follows:
```python
'target/file/path.ext'
=> 'target/file/path' + ' (i)' + '.ext'
=> 'target/file/path (i).ext'
```


## Instalation
---
You can use pip to install rmdirs.
```
pip install rmdirs
```

## Usage
---

You can call rmdirs as a script with the `-m` module call.
```
python -m rmdirs -r root_dir
```
```
python -m rmdirs -r root_dir -s '_'
```
Or you can import rmdirs and use the remove function.
```python
import rmdirs
rmdirs.remove(root_dir, separator='_')
```

## Examples
---

Input directory structure:
```
root_dir/
|-- file1.ext
|-- 1/
|   |-- a/
|   |   |-- i/
|   |   |   |-- file1.ext
|   |   |   |-- file2.ext
|   |   |-- ii/
|   |   |   |-- file1.ext
|   |   |-- iii/
|   |-- b/
|   |   |-- i/
|   |   |-- ii/
|   |   |   |-- file1.ext
|   |   |   |-- file2.ext
|   |   |   |-- file3.ext
|-- 2/
|   |-- a/
|   |-- b/
|   |   |-- i/
|-- 3/
|   |-- a/
|   |-- b/
|   |   |-- file1.ext
|   |-- c/
|-- 4/
|   |-- file1.ext
```

Resulting directory structure:
```
root_dir/
|-- 1_a_ii_file1.ext
|-- 1_a_i_file1.ext
|-- 1_a_i_file2.ext
|-- 1_b_ii_file1.ext
|-- 1_b_ii_file2.ext
|-- 1_b_ii_file3.ext
|-- 3_b_file1.ext
|-- 4_file1.ext
|-- file1.ext
```

Input directory structure:
```
root_dir/
|-- 1_a_file.ext
|-- 1_file.ext
|-- 1/
|   |-- a_file.ext
|   |-- file.ext
|   |-- a/
|   |   |-- file.ext
```
Resulting directory structure:
```
root_dir/
|-- 1_a_file (1).ext
|-- 1_a_file (2).ext
|-- 1_a_file.ext
|-- 1_file (1).ext
|-- 1_file.ext
```
---