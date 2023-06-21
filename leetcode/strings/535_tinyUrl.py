import random
import string


class Codec:
    base = 'htps://tinyurl.com/'
    sym = string.ascii_letters
    codes = {}

    def generate_short(self, size: int = 5):
        return ''.join([random.choice(self.sym) for i in range(size)])

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            short = self.generate_short()

            if short not in self.codes.keys():
                self.codes[short] = longUrl
                return self.base + short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        k = shortUrl.split('/')[-1]
        return self.codes[k]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))