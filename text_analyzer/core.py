from collections import Counter


class Document:
    """텍스트 문서를 나타내는 클래스입니다.

    :param text: 분석할 텍스트
    :ivar text: 원본 텍스트
    :ivar tokens: 토큰화된 단어 리스트
    """

    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize(text)

    def _tokenize(self, text):
        """텍스트를 소문자로 변환 후 단어 단위로 분리합니다

        :param text: 분리할 텍스트
        :return: 단어들의 리스트

        예시

        >>> Document("Hello World")._tokenize("Hello World")
        ['hello', 'world']

        설명:Document(괄호안에들어온 문장)을 _tokenize가 단어별로 쪼개어준다. 그리고 소문자로 바꿔준다.
        """
        return text.lower().split()

    def word_count(self):
        """문서의 총 단어 수를 반환한다.

        :return: 단어 개수
        예시

        >>> Document("Hello World").word_count()
        2

        설명:Document(괄호안에들어온 문장)의 토큰리스트의 길이를 보여준다.       """
        return len(self.tokens)

    def most_common_words(self, n=5):
        """가장 자주 등장하는 단어 상위 n개를 반환한다.

        :param n: 반환할 단어 개수 (기본값 5)
        :return: (단어, 빈도수) 튜플의 리스트

        예시

        >>> Document("a a b").most_common_words(1)
        [('a', 2)]

        설명:Document(괄호안에들어온 문장)의 토큰리스트에서 가장 많이 등장하는 단어를 n개 보여준다. 반환된 값은 [('a', 2)]로 a가 2번 나왔다는 뜻이다.
        """
        return Counter(self.tokens).most_common(n)