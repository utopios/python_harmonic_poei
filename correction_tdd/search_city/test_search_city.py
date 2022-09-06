import pytest
from search_city import city_search, CITIES


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

#3
@pytest.mark.parametrize("query, expected", [("PaR", ["Paris"]), ("vA", ["Valence", "Vancouver"]), ("vi", ["Vienne"])])
def test_city_search_should_return_matching_cities_case_insensitive_when_query_is_city_beginning_chars(query, expected):
    result = city_search(query)
    assert result == expected

#4
@pytest.mark.parametrize("query, expected", [("ri", ["Paris"]), ("en", ["Valence", "Vienne"]), ("dam", ["Rotterdam", "Amsterdam"]), ("g k", ["Hong Kong"])])
def test_city_search_should_return_matching_cities_when_query_is_part_of_cities(query, expected):
    result = city_search(query)
    assert result == expected

#5
def test_city_search_should_return_matching_all_cities_when_query_is_asterisk():
    result = city_search("*")
    assert result == CITIES

#6
# @pytest.mark.parametrize("query", [1,2.5])
def test_city_search_should_raise_type_error_when_query_si_not_string():
    with pytest.raises(TypeError):
        city_search(3)
