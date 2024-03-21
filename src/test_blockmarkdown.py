import unittest
from block_markdown import (
    block_type_heading,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,

    markdown_to_blocks,
    block_to_block_type,
    create_heading_node,
    create_blockquote_node,
    create_paragraph_node,
    create_ul_node,
    create_ol_node,
    create_code_node,
    markdown_to_html_node,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_heading_single_check(self):
        md = "# This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_heading_three_check(self):
        md = "### This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_heading_six(self):
        md = "###### This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_not_heading(self):
        md = "####### This is a heading"
        self.assertNotEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_paragraph(self):
        md = "This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_paragraph
        )
    def test_quote(self):
        md = "> this is a quote"
        self.assertEqual(
            block_to_block_type(md),
            block_type_quote
        )
    def test_unordered_list_star(self):
        md = """* this is an unordered list
* second part of unordered list """
        self.assertEqual(
            block_to_block_type(md),
            block_type_unordered_list
        )
    def test_unordered_list_dash(self):
        md = """- this is an unordered list
- second part of unordered list
- third part of unordered list"""
        self.assertEqual(
            block_to_block_type(md),
            block_type_unordered_list
        )
    def test_ordered_list(self):
        md = """1. this is an unordered list
2. second part of unordered list
3. third part of unordered list"""
        self.assertEqual(
            block_to_block_type(md),
            block_type_ordered_list
        )
    def test_block_code(self):
        md = '''``` a block of code goes here
more stuff goes into this
```'''
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_create_heading_node(self):
        block = "## text that is the heading"
        htmlnode = create_heading_node(block, block_type_heading)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(h2, text that is the heading, children: None, None)"
        )
    def test_create_heading_no_space(self):
        block = "##text that is the heading"
        htmlnode = create_heading_node(block, block_type_heading)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(h2, text that is the heading, children: None, None)"
        )
    def test_create_quote(self):
        block = "> text that is the heading"
        htmlnode = create_blockquote_node(block, block_type_quote)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(blockquote, text that is the heading, children: None, None)"
        )
    def test_create_quote_no_space(self):
        block = ">text that is the heading"
        htmlnode = create_blockquote_node(block, block_type_quote)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(blockquote, text that is the heading, children: None, None)"
        )
    def test_create_paragraph(self):
        block = "text that goes into the paragraph"
        htmlnode = create_paragraph_node(block, block_type_paragraph)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(p, text that goes into the paragraph, children: None, None)"
        )

    def test_create_ul_node(self):
        block = """- list line one
- list line two
* list line three
+ list line four
"""
        htmlnode = create_ul_node(block, block_type_unordered_list)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(ul, None, children: [HTMLNode(li, list line one, children: None, None), HTMLNode(li, list line two, children: None, None), HTMLNode(li, list line three, children: None, None), HTMLNode(li, list line four, children: None, None), HTMLNode(li, , children: None, None)], None)"
        )

    def test_create_ol_node(self):
        block = """- list line one
- list line two
* list line three
+ list line four
"""
        htmlnode = create_ol_node(block, block_type_ordered_list)
        self.assertEqual(
            htmlnode.__repr__(),
            f"HTMLNode(ol, None, children: [HTMLNode(li, list line one, children: None, None), HTMLNode(li, list line two, children: None, None), HTMLNode(li, list line three, children: None, None), HTMLNode(li, list line four, children: None, None), HTMLNode(li, , children: None, None)], None)"
        )
    
    def test_create_code_node(self):
        block = """``` code block looks like this
with more text ongoing blah blah blah

```"""
        htmlnode = create_code_node(block, block_type_code)
        self.assertEqual(
            htmlnode.__repr__(),
            f"""HTMLNode(pre, None, children: HTMLNode(code, ``` code block looks like this
with more text ongoing blah blah blah

```, children: None, None), None)"""
        )

    def test_markdown_to_html_node(self):
        markdown = """ # Heading of the markdown

        
- unordered item one
- unoredered item two

> quote block test

1. ordered_list
2. ordered_list 2

``` def func(self):
    do things ```

"""
        # print(markdown)
        htmlnode = markdown_to_html_node(markdown)
        self.assertEqual(
            htmlnode.__repr__(),
            f"""HTMLNode(div, None, children: [HTMLNode(h1, Heading of the markdown, children: None, None), HTMLNode(ul, None, children: [HTMLNode(li, unordered item one, children: None, None), HTMLNode(li, unoredered item two, children: None, None)], None), HTMLNode(blockquote, quote block test, children: None, None), HTMLNode(ol, None, children: [HTMLNode(li, 1. ordered_list, children: None, None), HTMLNode(li, 2. ordered_list 2, children: None, None)], None), HTMLNode(pre, None, children: HTMLNode(code, ``` def func(self):
    do things ```, children: None, None), None)], None)"""

        )
    

if __name__ == "__main__":
    unittest.main()