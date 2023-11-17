# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    import logging
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

    if linkedList is None:
        return None

    if linkedList.next is None:
        return linkedList

    head = first_duplicate = current = previous = linkedList

    while current is not None:
        if current.next is not None:
            if head == current:
                # first node. increment current
                current = current.next

                logging.debug("first node")
                print_linked_list(head)

            else:
                # if matching value found, increment previous and current
                if previous.value == current.value:
                    previous = previous.next
                    current = current.next

                    logging.debug("matching value found")
                    logging.debug(f"{previous.value = }")
                    logging.debug(f"{first_duplicate.value = }")
                    logging.debug(f"{current.value = }")
                    print_linked_list(head)

                elif first_duplicate != previous and first_duplicate.value == previous.value:
                    # current is the end of a chain of duplicates.
                    previous.next = None
                    first_duplicate.next = current
                    first_duplicate = current
                    previous = current
                    current = current.next

                    logging.debug("current is end of chain of duplicates")
                    logging.debug(f"{previous.value = }")
                    logging.debug(f"{first_duplicate.value = }")
                    logging.debug(f"{current.value = }")
                    print_linked_list(head)

                else:
                    # not a duplicate and not the end of a chain of duplicates
                    # set previous to previous.next, fdn to current.next, and current to current.next
                    previous = previous.next
                    first_duplicate = previous
                    current = current.next

                    logging.debug("not duplicate and not end of chain of duplicates")
                    logging.debug(f"{previous.value = }")
                    logging.debug(f"{first_duplicate.value = }")
                    logging.debug(f"{current.value = }")
                    print_linked_list(head)

        else:
            # current is the last node
            # if last current is a duplicate, set previous.next to None, fdn.next to None, and fd and current to current.next
            if previous.value == current.value:
                previous.next = None
                first_duplicate.next = None
                current = current.next
                
                logging.debug("last node. current node is a duplicate")
                print_linked_list(head)

            elif first_duplicate != current:
                # current is the end of a chain of duplicates
                # set previous.next to None, previous to fd, fd.next to current, and fdn and current to current.next
                previous.next = None
                first_duplicate.next = current
                current = current.next
                
                logging.debug("last node. current node is end of chaing of duplicates")
                print_linked_list(head)
                
            else:
                current = current.next
                
                logging.debug("last node. not a duplicate or a chain of duplicates")
                print_linked_list(head)

    return head


def create_linked_list(list_of_values):
    head = LinkedList(list_of_values[0])
    current = head

    for value in list_of_values[1:]:
        current.next = LinkedList(value)
        current = current.next

    return head


def print_linked_list(linked_list):
    if linked_list is not None:
        current = linked_list
        print("Linked list: ", end="")

        while current is not None:
            if current.next is not None:
                print(f"{current.value} -> ", end="")

            else:
                print(current.value)

            current = current.next

        print()


# linked_list = create_linked_list([1,1,3,4,4,4,5,6,6])
linked_list = create_linked_list([1,1,1,1,1,4,4,5,6,6])
removeDuplicatesFromLinkedList(linked_list)
