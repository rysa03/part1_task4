def last_letter(test):
    return test[-1]
def test_last_letter():
    assert last_letter('hello!') == '!'
    assert last_letter('banana') == 'a'
    assert last_letter('8') == '8'
    assert last_letter('funnyguys') == 's'
    assert last_letter('101') == '1'
print("YOUR CODE IS CORRECT!")
test_last_letter()
#last_letter=input()
#a=last_letter[-1]
#print(a)

