def test_function():
  def inner_function():
    return 'Я в области видимости функции test_function'
  return inner_function()
print(test_function())
