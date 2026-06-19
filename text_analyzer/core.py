from collections import Counter


class Document:
    """텍스트 문서 클래스

    :param text: 분석할 텍스트
    :ivar text: 원본 텍스트
    :ivar tokens: 단어 리스트
    """

    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize(text)

    def _tokenize(self, text):
        """텍스트를 단어로 쪼갬!! 소문자로 바꿔줌

        :param text: 입력 텍스트
        :return: 단어 리스트

        >>> Document("Hello World")._tokenize("Hello World")
        ['hello', 'world']
        """
        return text.lower().split()

    def word_count(self):
        """단어 개수 세기

        :return: 단어 수

        >>> Document("Hello World").word_count()
        2
        """
        return len(self.tokens)

    def most_common_words(self, n=5):
        """많이 나온 단어 n개 반환

        :param n: 몇 개 볼건지 (기본 5개)
        :return: (단어, 횟수) 리스트

        >>> Document("a a b").most_common_words(1)
        [('a', 2)]
        """
        return Counter(self.tokens).most_common(n)
