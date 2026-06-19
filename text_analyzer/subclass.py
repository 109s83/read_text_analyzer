from text_analyzer.core import Document


class Tweet(Document):
    """트윗 클래스!! Document 상속받음

    :param text: 트윗 텍스트
    """

    def __init__(self, text):
        super().__init__(text)

    def hashtag_count(self):
        """해시태그(#) 개수 세기

        :return: 해시태그 개수

        >>> Tweet("I love #python and #coding").hashtag_count()
        2
        """
        count = 0  # 0부터 시작
        for word in self.tokens:  # 토큰에 있는 단어를 보면서
            if word.startswith('#'):  # 만약 word가 #으로 시작한다면
                count += 1  # count에 1을 더해준다
        return count

    def mention_count(self):
        """멘션(@) 개수 세기

        :return: 멘션 개수

        >>> Tweet("Hi @alice and @bob, how are you?").mention_count()
        2
        """
        return sum(1 for word in self.tokens if word.startswith('@'))