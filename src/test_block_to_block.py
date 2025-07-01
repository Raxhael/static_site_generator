import unittest
from block_to_block import BlockType, block_to_block_type

class TestBlockIdentification(unittest.TestCase):
    def test_block_to_blocks(self):
        test_cases = [
            ("# My Heading",BlockType.HEADING),
            ("### Level Three Heading",BlockType.HEADING),
            ("> This is a quoted line.\n> Another quoted line.",BlockType.QUOTE),        
            ("""```\nthis is Code\n```""",BlockType.CODE),
            ("- First item\n- Second item\n- Third item", BlockType.UNORDERED_LIST),            ("""1. First item\n2. Second item\n3. Third item""",BlockType.ORDERED_LIST),
            ("This is just a regular paragraph block with no special markdown formatting.",BlockType.PARAGRAPH)
            ]
            
        for input,expected_result in test_cases:
            result = block_to_block_type(input)
            self.assertEqual(result,expected_result)



if __name__ == "__main__":
    unittest.main()