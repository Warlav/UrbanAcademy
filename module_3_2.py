msg = input('Введите сообщение:')
sndr = input('Введите адрес отправителя:')
rcpnt = input('Введите получателя:')
letter = (msg, rcpnt)
if sndr != '':
  letter = letter + (sndr,)
  
  
def send_email(message, recipient, sender='university.help@gmail.com'):
  global letter
  ends = ('.com', '.ru', '.net')
  if '@' not in sender or '@' not in recipient or not sender.endswith(ends) or not recipient.endswith(ends):
    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
  elif sender == recipient:
    print('Нельзя отправить письмо самому себе!')
  else:
    if sender == 'university.help@gmail.com':
      print(f'Письмо успешно отправлено с адреса\n{sender}\nна адрес\n{recipient}')
    else:
      print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!\nПисьмо отправлено с адреса\n{sender}\nна адрес\n{recipient}.')


send_email(*letter)
