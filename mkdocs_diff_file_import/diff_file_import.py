import mkdocs
import re
import os


# Define a configuration class for the plugin
class GenericImportDiffConfig(mkdocs.config.base.Config):
    # Configuration option for the name of the code block
    codeblock_name = mkdocs.config.config_options.Type(str, default="import-diff-file")


# Define the main plugin class inheriting from MkDocs BasePlugin
class ImportDiff(mkdocs.plugins.BasePlugin[GenericImportDiffConfig]):
    def __init__(self):
        # Initialize the import block variable
        self.import_block = None
        # Get a logger specific to this plugin
        self.logger = mkdocs.plugins.get_plugin_logger(__name__)

    # Method that gets called for each page's markdown content
    def on_page_markdown(
        self,
        markdown: str,
        page: mkdocs.structure.pages.Page,
        config: mkdocs.config.defaults.MkDocsConfig,
        files: mkdocs.structure.files.Files,
    ):
        # Log a debug message with the page title
        self.logger.debug(f"check on {page.title}")
        # Search for specific code blocks in the markdown content
        for instance in re.finditer(
            rf"(```({self.config.codeblock_name}) file=([^`]+)```)", markdown
        ):
            # Check if there are any matching groups
            if len(instance.groups()) == 3:
                # The whole match to be replaced
                replace = instance.groups()[0]
                file_path = instance.groups()[2]
                replacement_block = self._load_file_to_import(file_path)

                # Replace the matched code block with replacement_block
                markdown = markdown.replace(replace, replacement_block)

        # Return the modified markdown content
        return markdown

    def _load_file_to_import(self, file_path) -> str:
        if os.path.isfile(file_path):
            file_content = open(file_path).read()
            result_code_block = f"```diff \n\n{file_content} \n\n```"
        else:
            result_code_block = f"```diff file not found. cwd {str(os.listdir(os.getcwd()))}```"
        return result_code_block
