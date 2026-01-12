#!/usr/bin/env python3
"""
EPUB to JSON Converter

Converts EPUB files to clean JSON format, preserving structure.

Usage:
    python convert.py input.epub output.json
"""

import argparse
import json
import sys
import warnings
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, XMLParsedAsHTMLWarning
from ebooklib import epub, ITEM_DOCUMENT

# Suppress XML parser warning - we're intentionally using HTML parser for flexibility
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


def extract_text_with_structure(html_content: str) -> list[dict]:
    """
    Extract text from HTML content, preserving paragraph structure.

    Returns a list of content blocks (paragraphs, headings, etc.)
    """
    soup = BeautifulSoup(html_content, 'lxml')

    # Remove script and style elements
    for element in soup(['script', 'style', 'meta', 'link']):
        element.decompose()

    blocks = []

    # Find body content (or use whole soup if no body)
    body = soup.find('body') or soup

    # Extract structured content
    for element in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'blockquote', 'li']):
        # Skip if this element is nested inside another we're already processing
        if element.find_parent(['p', 'blockquote', 'li']):
            continue

        text = element.get_text(separator=' ', strip=True)

        if not text:
            continue

        tag_name = element.name

        block = {
            'type': 'heading' if tag_name.startswith('h') else 'paragraph',
            'text': text
        }

        # Add heading level for headings
        if tag_name.startswith('h'):
            block['level'] = int(tag_name[1])

        blocks.append(block)

    # If no structured content found, fall back to plain text extraction
    if not blocks:
        text = body.get_text(separator='\n', strip=True)
        if text:
            # Split by double newlines to create paragraphs
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            for para in paragraphs:
                # Clean up internal whitespace
                para = ' '.join(para.split())
                if para:
                    blocks.append({'type': 'paragraph', 'text': para})

    return blocks


def convert_epub_to_json(epub_path: str) -> dict:
    """
    Convert an EPUB file to a JSON structure.

    Returns a dictionary with metadata and chapters.
    """
    book = epub.read_epub(epub_path)

    # Extract metadata
    metadata = {
        'title': book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else None,
        'author': book.get_metadata('DC', 'creator')[0][0] if book.get_metadata('DC', 'creator') else None,
        'language': book.get_metadata('DC', 'language')[0][0] if book.get_metadata('DC', 'language') else None,
        'identifier': book.get_metadata('DC', 'identifier')[0][0] if book.get_metadata('DC', 'identifier') else None,
    }

    # Clean up None values
    metadata = {k: v for k, v in metadata.items() if v is not None}

    # Extract chapters in reading order (using spine)
    chapters = []
    chapter_num = 0

    for item in book.get_items_of_type(ITEM_DOCUMENT):
        content = item.get_content().decode('utf-8', errors='ignore')
        blocks = extract_text_with_structure(content)

        if not blocks:
            continue

        chapter_num += 1

        # Try to find chapter title from first heading
        title = None
        for block in blocks:
            if block.get('type') == 'heading':
                title = block['text']
                break

        chapter = {
            'chapter_number': chapter_num,
            'title': title,
            'source_file': item.get_name(),
            'content': blocks
        }

        chapters.append(chapter)

    return {
        'metadata': metadata,
        'total_chapters': len(chapters),
        'chapters': chapters
    }


def main():
    parser = argparse.ArgumentParser(
        description='Convert EPUB files to JSON format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python convert.py book.epub book.json
    python convert.py --pretty input.epub output.json
        """
    )

    parser.add_argument('input', help='Input EPUB file path')
    parser.add_argument('output', help='Output JSON file path')
    parser.add_argument('--pretty', '-p', action='store_true',
                        help='Pretty-print JSON output with indentation')

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        sys.exit(1)

    if not input_path.suffix.lower() == '.epub':
        print(f"Warning: Input file does not have .epub extension", file=sys.stderr)

    # Convert
    print(f"Converting: {args.input}")

    try:
        result = convert_epub_to_json(args.input)
    except Exception as e:
        print(f"Error converting EPUB: {e}", file=sys.stderr)
        sys.exit(1)

    # Write output
    output_path = Path(args.output)

    with open(output_path, 'w', encoding='utf-8') as f:
        if args.pretty:
            json.dump(result, f, indent=2, ensure_ascii=False)
        else:
            json.dump(result, f, ensure_ascii=False)

    # Summary
    print(f"Output: {args.output}")
    print(f"Title: {result['metadata'].get('title', 'Unknown')}")
    print(f"Author: {result['metadata'].get('author', 'Unknown')}")
    print(f"Chapters: {result['total_chapters']}")

    total_blocks = sum(len(ch['content']) for ch in result['chapters'])
    print(f"Content blocks: {total_blocks}")


if __name__ == '__main__':
    main()
