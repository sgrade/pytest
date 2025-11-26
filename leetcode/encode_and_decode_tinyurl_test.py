"""Tests for the TinyURL encoder/decoder (LeetCode #535)."""

import pytest
from encode_and_decode_tinyurl import Codec


class TestCodec:
    """Test suite for the Codec class."""

    @pytest.fixture
    def codec(self):
        """Fixture to create a fresh Codec instance for each test."""
        return Codec()

    def test_encode_single_url(self, codec):
        """Test encoding a single URL returns a valid short URL."""
        long_url = "https://leetcode.com/problems/design-tinyurl"
        short_url = codec.encode(long_url)

        assert isinstance(short_url, str)
        assert short_url == "http://tinyurl.com/0"  # First encoded URL should have ID 0

    def test_decode_encoded_url(self, codec):
        """Test that decoding an encoded URL returns the original URL."""
        long_url = "https://leetcode.com/problems/design-tinyurl"
        short_url = codec.encode(long_url)
        decoded_url = codec.decode(short_url)

        assert decoded_url == long_url

    # def test_encode_multiple_different_urls(self, codec):
    #     """Test encoding multiple different URLs produces different short URLs."""
    #     url1 = "https://leetcode.com/problems/design-tinyurl"
    #     url2 = "https://google.com"
    #     url3 = "https://github.com"

    #     short1 = codec.encode(url1)
    #     short2 = codec.encode(url2)
    #     short3 = codec.encode(url3)

    #     # Each URL should get a different ID
    #     assert short1 != short2
    #     assert short2 != short3
    #     assert short1 != short3

    #     # Verify all can be decoded correctly
    #     assert codec.decode(short1) == url1
    #     assert codec.decode(short2) == url2
    #     assert codec.decode(short3) == url3

    # def test_encode_same_url_twice_returns_same_short_url(self, codec):
    #     """Test that encoding the same URL twice returns the same short URL."""
    #     long_url = "https://leetcode.com/problems/design-tinyurl"

    #     short_url1 = codec.encode(long_url)
    #     short_url2 = codec.encode(long_url)

    #     assert short_url1 == short_url2

    # def test_encode_same_url_twice_does_not_increment_id(self, codec):
    #     """Test that encoding the same URL multiple times doesn't create duplicate entries."""
    #     url1 = "https://leetcode.com"
    #     url2 = "https://google.com"

    #     codec.encode(url1)
    #     codec.encode(url1)  # Encode same URL again
    #     short_url2 = codec.encode(url2)

    #     # Second unique URL should get ID 1, not 2
    #     assert short_url2 == "1"

    # def test_decode_nonexistent_url_raises_error(self, codec):
    #     """Test that decoding a non-existent short URL raises ValueError."""
    #     with pytest.raises(ValueError, match="No such URL was previously encoded"):
    #         codec.decode("999")

    # def test_decode_without_encoding_raises_error(self, codec):
    #     """Test that decoding without any encoding raises ValueError."""
    #     with pytest.raises(ValueError):
    #         codec.decode("0")

    # def test_encode_empty_string(self, codec):
    #     """Test encoding an empty string."""
    #     empty_url = ""
    #     short_url = codec.encode(empty_url)
    #     decoded_url = codec.decode(short_url)

    #     assert decoded_url == empty_url

    # def test_encode_very_long_url(self, codec):
    #     """Test encoding a very long URL."""
    #     long_url = "https://example.com/" + "a" * 1000 + "?param=" + "b" * 1000
    #     short_url = codec.encode(long_url)
    #     decoded_url = codec.decode(short_url)

    #     assert decoded_url == long_url
    #     assert len(short_url) < len(long_url)

    # def test_encode_url_with_special_characters(self, codec):
    #     """Test encoding URLs with special characters."""
    #     urls = [
    #         "https://example.com/path?query=value&other=123",
    #         "https://example.com/path#fragment",
    #         "https://user:pass@example.com:8080/path",
    #         "https://example.com/path with spaces",
    #         "https://example.com/path?emoji=😀",
    #     ]

    #     for url in urls:
    #         short_url = codec.encode(url)
    #         decoded_url = codec.decode(short_url)
    #         assert decoded_url == url

    # def test_sequential_id_generation(self, codec):
    #     """Test that IDs are generated sequentially."""
    #     urls = [f"https://example{i}.com" for i in range(5)]
    #     short_urls = [codec.encode(url) for url in urls]

    #     expected_ids = ["0", "1", "2", "3", "4"]
    #     assert short_urls == expected_ids

    # def test_multiple_codec_instances_are_independent(self):
    #     """Test that multiple Codec instances maintain separate state."""
    #     codec1 = Codec()
    #     codec2 = Codec()

    #     url1 = "https://example1.com"
    #     url2 = "https://example2.com"

    #     short1 = codec1.encode(url1)
    #     short2 = codec2.encode(url2)

    #     # Both should start with ID 0
    #     assert short1 == "0"
    #     assert short2 == "0"

    #     # Each codec should decode its own URLs correctly
    #     assert codec1.decode(short1) == url1
    #     assert codec2.decode(short2) == url2

    #     # But codec1's ID 0 maps to url1, not url2
    #     assert codec1.decode("0") == url1
    #     assert codec2.decode("0") == url2

    #     # Codec1 shouldn't know about codec2's second URL
    #     codec2.encode("https://example3.com")  # This gets ID 1 in codec2
    #     with pytest.raises(ValueError):
    #         codec1.decode("1")  # codec1 doesn't have ID 1 yet


# Additional integration test
def test_full_workflow():
    """Integration test for the full encode-decode workflow."""
    codec = Codec()

    # Encode multiple URLs
    urls = [
        "https://leetcode.com/problems/design-tinyurl",
        "https://www.google.com",
        "https://github.com/python/cpython",
    ]

    short_urls = [codec.encode(url) for url in urls]

    # Decode all URLs
    decoded_urls = [codec.decode(short_url) for short_url in short_urls]

    # Verify all URLs match
    assert decoded_urls == urls


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
