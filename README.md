# extensionator

Ever come across some files that don't have an extension?
![example](./static/example-files.png)

In *nix systems, it doesn't really matter, but in Windows, it can be troublesome when you want to open them with a specific program.

Extensionator will help you add extensions to files automatically. It does require the `file` command to be installed, which usually comes with [git-for-windows](https://github.com/git-for-windows/git) (if you told it to add the bash tools to your path).

## Installation

This tool is not published to PyPI yet, so you'll have to install it directly from the repo.
```bash
$ pip install git+https://github.com/ethanavatar/extensionator.git
```

## Usage

```bash
$ python -m extensionator --help
usage: extensionator [-h] {file,dir} ...

Add extensions to files that don't have an extension based on their mime type.

positional arguments:
  {file,dir}  Command to run
    file      Add extensions to a single file
    dir       Add extensions to all files in a directory

optional arguments:
  -h, --help  show this help message and exit
```

### Convert a single file

```bash
$ python -m extensionator file path/to/file
```

### Convert all files in a directory

```bash
$ python -m extensionator dir path/to/dir/of/files
```