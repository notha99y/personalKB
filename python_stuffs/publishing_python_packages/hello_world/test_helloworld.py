from helloworld import say_hello

def test_hellowold_no_params():
    assert say_hello() == "Hello, World!"

def test_hellowold_with_params():
    assert say_hello("Everyone") == "Hello, Everyone!"
