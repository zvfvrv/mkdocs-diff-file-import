# **mkdocs-diff-file-import** MkDocs Plugin

## Overview

The `mkdocs-diff-file-import` plugin for MkDocs allows you to dynamically replace custom code blocks in your Markdown files with the content of specified files. This plugin is particularly useful for managing and displaying differences between imported code files within your documentation.

## Features

- Configurable code block name to identify sections to be replaced.
- Automatically replaces matching code blocks with the content of specified files during the build process.
- Easy integration with existing MkDocs projects.

## Installation

To install the plugin, you can use `pip`:

```bash
pip install mkdocs-diff-file-import
```

## Configuration

To use the `mkdocs-diff-file-import` plugin, add it to your `mkdocs.yml` configuration file:

```yaml
plugins:
  - search
  - diff-file-import:
      codeblock_name: import-diff-file  # Optional, default is 'import-diff-file'
```

## Usage

In your Markdown files, define code blocks with the specified code block name to be replaced by the plugin. For example:

<pre>
```
import-diff-file file=example.txt
```
</pre>

During the MkDocs build process, these code blocks will be replaced by the content of the specified file.

## Example

Given the following content in a Markdown file:

<pre>
```import-diff-file file=example.diff```
</pre>

The `mkdocs-diff-file-import` plugin will replace this block with the content of `example.diff` inside a diff code block:

<pre>
```diff
[edit routing-instances l3vpn-test]
-    vrf-table-label;
[edit protocols bgp]
+    bgp-error-tolerance {
+        malformed-route-limit 0;
+    }
```
</pre>

<!-- ## Development

### Clone the Repository

```bash
git clone https://github.com/zvfvrv/mkdocs-diff-file-import.git
cd mkdocs-diff-file-import
```

### Install Dependencies

```bash
pip install -r requirements.txt
``` -->

<!-- ### Run Tests

To run tests for the plugin, use the following command:

```bash
pytest
``` -->

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details.

## Contact

If you have any questions, issues, or suggestions, please open an issue in the GitHub repository.
