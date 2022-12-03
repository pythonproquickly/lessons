"""Blog feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import blog


@scenario('first.feature', 'Publishing the article')
def test_publishing_the_article():
    """Publishing the article."""


@given('I have an article')
def test_find_article():
    assert blog.search(tag="article")


@given('I\'m an author user')
def _():
    """I'm an author user."""
    raise NotImplementedError


@when('I go to the article page')
def _():
    """I go to the article page."""
    raise NotImplementedError


@when('I press the publish button')
def _():
    """I press the publish button."""
    raise NotImplementedError


@then('I should not see the error message')
def _():
    """I should not see the error message."""
    raise NotImplementedError


@then('the article should be published')
def _():
    """the article should be published."""
    raise NotImplementedError
