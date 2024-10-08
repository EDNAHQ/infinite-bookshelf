from io import BytesIO
from markdown import markdown
from weasyprint import HTML

def create_pdf_file(content: str) -> BytesIO:
    """Create a PDF from Markdown content."""
    
    html_content = markdown(content, extensions=["extra", "codehilite"])

    styled_html = f"""
    <html>
        <head>
            <style>
                :root {{ --text-color: #000; --bg-color: #fff; --title-color: #fbb022; --sub-title-color: #d94f8b; 
                            --code-bg: #ca5a8b; --border-color: #444; --input-bg: #ca5a8b; --input-border: #ca5a8b; }}
                @page {{ size: A4; margin: 1cm 0cm; }}
                body {{ margin: 0cm; padding: 1cm; background: var(--bg-color); color: var(--text-color); font: 12pt Arial; }}
                h1, h2, h3 {{ color: var(--title-color); margin: 1cm 0 1cm; }}
                h4, h5, h6 {{ color: var(--sub-title-color); margin: 1cm 0 1cm; }}
                p {{ margin-bottom: 1cm; margin-top: 1cm; }}
                code {{ background: var(--code-bg); padding: 2px 4px; border-radius: 4px; font: 0.9em 'Arial'; }}
                pre {{ background: var(--code-bg); padding: 1em; border-radius: 4px; white-space: pre-wrap; overflow-x: auto; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 1em; }}
                th, td {{ border: 1px solid var(--border-color); padding: 8px; }}
                th {{ background: rgba(85,85,85,0.7); font-weight: bold; }}
                input, textarea {{ border: 1px solid var(--input-border); color: #fff; background: #ca5a8b; padding: 8px; border-radius: 4px; }}
                @media print {{ body {{ background: #fff; color: #000; }} h1, h2, h3 {{ color: #fbb022; }} h4, h5, h6 {{ color: #d94f8b; }} }}
            </style>
        </head>
        <body>{html_content}</body>
    </html>
    """

    pdf_buffer = BytesIO()
    HTML(string=styled_html).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)

    return pdf_buffer
