from asyncio import gather
import src.lessons.greg.funcs as g

def test_addup():
    assert g.addup(4, 6) == 10

def test_divide():
    assert g.divide(9, 3) == 3
