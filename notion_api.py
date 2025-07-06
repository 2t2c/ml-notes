import os
from notion_client import Client
from pprint import pprint
from notion_exporter import NotionExporter
from python_notion_exporter import NotionExporter, ExportType, ViewExportType

# secrets
notion = Client(auth=os.environ["NOTION_TOKEN"])
token_v2 = os.environ["NOTION_TOKEN_V2"]
file_token = os.environ["NOTION_FILE_TOKEN"]

# notion page id
page_id = "21181ba4f78a800b83e6d55971c0d1df"

if __name__ == "__main__":
    exporter = NotionExporter(
        token_v2=token_v2,
        file_token=file_token,
        pages={"Page Name": page_id},
        export_directory="./",
        flatten_export_file_tree=False,
        export_type=ExportType.MARKDOWN,
        current_view_export_type=ViewExportType.CURRENT_VIEW,
        include_files=True,
        recursive=True
    )
    exporter.process()