

def menu() ->  int: 
    print(''' Главное меню:
    1. Открыть файл.
    2. Сохранить файл.
    3. показать файл. 
    4. Добавить файл.
    5. Найти контакт. 
    6. Изменить контакт. 
    7. Удалить контакт. 
    8. Выход. ''')
    choice = int(input('Выберите пункт меню: '))
    return choice

def show_contact(phone_book: list):
     print()
     if phone_book:
      for i, contact in enumerate(phone_book, 1):
          print(f'{i}. {contact.get("name"):<20} ' 
                f'{contact.get("phone"):<20} '
                f'{contact.get("comment"):<20}')
      print()     
     else:
      print('\nТелефонная книга не открыта или пуста\n')   

def save(phone_book, list):
   return 
   

def new_contact() -> dict:
   print()
   name = input('Введите имя контакта: ')      
   phone = input('Введите номер контакта: ')     
   comment = input('Введите комментарий: ')    
   print()   
   return {'name': name, 'phone': phone, 'comment': comment }


def input_request(text: str) -> str:
   request = input(f'Введите {text}: ')
   return request

def change_contact(book: list) -> tuple:
   show_contact(book)
   choice = int(input('Выберите контакт который хотите изменить: '))
   name = input('Введите новое имя или Enter оставить без изменений: ')
   phone = input('Введите новый номер или Enter оставить без изменений: ')
   comment = input('Введите новый комментарий или Enter оставить без изменений: ')
   return choice - 1, {'name': name if name else book[choice -1].get('name'),
                       'phone': phone if phone else book[choice -1].get('phone'),
                       'comment': comment if comment else book[choice -1].get('comment')}
   
   
def select_to_delete(book: list):
   show_contact(book)
   return int(input('Введите номер элемента который хотите удалить: '))  - 1


def goodbye():
    print('Досвидания')     

    