# https://docs.pytest.org/en/latest/

def fatorial(numero):
	f = 1
	if numero == 0:
		return 1
	if numero == 1:
		return 1
	if numero < 0:
		return "Número negativo não rola."

	while numero >= 1:
		f *= numero		
		numero -= 1
	return f

def test_fatorial_5():
	assert fatorial(5) == 120

def test_fatorial_0():
	assert fatorial(0) == 1

def test_fatorial_1():
	assert fatorial(1) == 1
