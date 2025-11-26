# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/

import string


class Codec:
    def __init__(self):
        self.numeric_id: int = 0
        self.chars: str = string.digits + string.ascii_letters
        self.id_to_url: dict[str, str] = {}

    def _get_key(self) -> str:
        """Generate a bijective base-62 encoded key from the current numeric_id."""
        cnt = self.numeric_id
        key = ""
        base = len(self.chars)

        while cnt >= 0:
            key = self.chars[cnt % base] + key
            cnt = cnt // base - 1

        return key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        key = self._get_key()
        self.id_to_url[key] = longUrl
        self.numeric_id += 1
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.replace("http://tinyurl.com/", "")
        return self.id_to_url[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
