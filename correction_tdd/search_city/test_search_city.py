import pytest
from search_city import city_search

#1
@pytest.mark.parametrize("query", ["P", "b", "A", "", "."])
def test_city_search_should_return_empty_when_query_less_than_two_chars(query):
    result = city_search(query)
    assert result == []

#2
@pytest.mark.parametrize("query, expected", [("Paris", ["Paris"]), ("Va", ["Valence", "Vancouver"]), ("Vi", ["Vienne"])])
def test_city_search_should_return_matching_cities_when_query_is_city_beginning_chars(query, expected):
    result = city_search(query)
    assert result == expected