"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 0:
        normal_queue.append(person_name)
        queue = normal_queue
    if ticket_type == 1:
        express_queue.append(person_name)
        queue = express_queue
    return queue


def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    cont = 0
    for name in enumerate(queue):
        if name[1] == person_name:
            cont += 1
    return cont

def remove_the_last_person(queue):
    last = queue[len(queue) - 1]
    queue.pop(len(queue) - 1)
    return last

def sorted_names(queue):
    queue.sort()
    return queue
