import pytest
from model import Model
from controller import Controller

@pytest.fixture
def model():
    return Model()

@pytest.fixture
def controller(model):
    return Controller(model)

def test_clear_button(model, controller):
    #model = Model()
    #controller = Controller(model)
    controller.button_pressed("C")
    assert "0" == model.display
    # assert expected outcome == reference implementation

def test_number_button (model, controller):
    controller.button_pressed("7")
    assert  "7" == model.display

def test_digit_concatination(model, controller):
    controller.button_pressed("4")
    controller.button_pressed("5")
    assert "45" == model.display

def test_clear_digit_button(model, controller):
    controller.button_pressed("5")
    controller.button_pressed("C")
    controller.button_pressed("6")
    assert "6" == model.display

def test_del_button(model, controller):
    controller.button_pressed("8")
    controller.button_pressed("Del")
    controller.button_pressed("7")
    assert "7" == model.display

