import pytest


@pytest.fixture()
def ejemploFixture():
    print("FIXTURE")
    return 42


# usefixtures no sirve si necesitas devolver un valor a travez del fixture
@pytest.mark.usefixtures("ejemploFixture")
class TestPrueba():
    # debe ir el self
    # si no paso ejemploFixture como parametro no funciona
    # tampoco funciona si hago asset ejemploFixture == 42 porque se toma como un modulo y no el return
    def test_1(self, ejemploFixture):
        valor = ejemploFixture
        assert valor == 42

    def test_2(self, ejemploFixture):
        valor = ejemploFixture
        assert valor == 42
