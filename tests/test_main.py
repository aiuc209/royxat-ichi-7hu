import pytest

def eng_yuqori_ball(royxat):
    natija = []
    for tup in royxat:
        ism, ball1, ball2, ball3 = tup
        eng_yuqori = max(ball1, ball2, ball3)
        natija.append((ism, eng_yuqori))
    return natija

@pytest.mark.parametrize("royxat, natija", [
    ([("Ali", 90, 80, 70), ("Vali", 95, 85, 75)], [("Ali", 90), ("Vali", 95)]),
    ([("Hasan", 60, 70, 80), ("Husan", 65, 75, 85)], [("Hasan", 80), ("Husan", 85)]),
    ([("Jasur", 40, 50, 60), ("Farrux", 45, 55, 65)], [("Jasur", 60), ("Farrux", 65)]),
])
def test_eng_yuqori_ball(royxat, natija):
    assert eng_yuqori_ball(royxat) == natija
