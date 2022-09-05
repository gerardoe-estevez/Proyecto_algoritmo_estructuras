from contact_book.contact import Contact
from contact_book.list import LinkedList

def run():
    manuel = Contact("user1","last_name1","user3@gmail.com","Home",2)

    moises = Contact("user2","last_name2","user3@gmail.com","Home",5)

    kikejose = Contact("user3","last_name3","user2@gmail.com","Office",4)



    linkedlist = LinkedList()
    linkedlist.append(manuel)
    linkedlist.append(moises)
    linkedlist.append(kikejose)

    print(linkedlist)

if __name__=="__main__":
    run()