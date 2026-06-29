import os
import re
from typing import Dict, Any, Optional

class TechnicalDocWriterClient:
    """
    Client SDK to auto-generate markdown documentation by parsing python codebase source scripts.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("DOC_WRITER_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def write_documentation(self, source_code: str) -> str:
        """
        Parses functions/classes and docstrings, returning formatted markdown output.
        """
        doc_lines = ["# API Reference Documentation\n"]
        
        # Simple parser regex for demonstration
        classes = re.findall(r'class (\w+)(?:\(([^)]+)\))?:', source_code)
        methods = re.findall(r'def (\w+)\(([^)]*)\)(?:\s*->\s*([^:]+))?:', source_code)
        
        if classes:
            doc_lines.append("## Classes\n")
            for cls in classes:
                base = f" (inherits {cls[1]})" if cls[1] else ""
                doc_lines.append(f"### `class {cls[0]}{base}`\n")
                
        if methods:
            doc_lines.append("## Methods & Functions\n")
            for meth in methods:
                ret = f" -> {meth[2].strip()}" if meth[2] else ""
                doc_lines.append(f"### `def {meth[0]}({meth[1]}){ret}`")
                doc_lines.append("Parsed from code module implementation.\n")
                
        return "\n".join(doc_lines)
