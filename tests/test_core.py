from text_analyzer.core import Document
from text_analyzer.subclass import Tweet


# Document 테스트
def test_word_count_normal():
    doc = Document("hello my name is soojeong")
    assert doc.word_count() == 5


def test_most_common_words_normal():
    doc = Document("banana banana apple")
    assert doc.most_common_words(1) == [('banana', 2)]


def test_most_common_words_top3():
    doc = Document("cat cat cat dog dog bird")
    assert doc.most_common_words(3) == [('cat', 3), ('dog', 2), ('bird', 1)]


def test_tokenize_lowercase():
    doc = Document("Hello SOOJEONG")
    assert doc.tokens == ['hello', 'soojeong']


# Tweet 테스트
def test_hashtag_count_normal():
    t = Tweet("add hashtag to #memo and #study")
    assert t.hashtag_count() == 2


def test_mention_count_normal():
    t = Tweet("this is for @soojeong and @alice")
    assert t.mention_count() == 2


# 엣지 케이스
def test_word_count_empty():
    doc = Document("")
    assert doc.word_count() == 0


def test_most_common_words_empty():
    doc = Document("")
    assert doc.most_common_words(5) == []


def test_word_count_spaces():
    doc = Document("     ")
    assert doc.word_count() == 0


def test_hashtag_count_none():
    t = Tweet("this is a test message")
    assert t.hashtag_count() == 0


def test_mention_count_none():
    t = Tweet("hello my name is soojeong")
    assert t.mention_count() == 0