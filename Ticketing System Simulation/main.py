import time
import random
from collections import *
from datetime import datetime
import unittest

class Ticket:
    #ticket with ticket number and timestamp
    def __init__(self,ticketNumber):
        self.ticketNumber = ticketNumber
        self.timestamp = datetime.now()

    def __str__(self):
        return ""

class TicketQueue:
    #present the ticket queue system
    def __init__(self):
        self.queue = deque()
        self.ticket_counter = 1

    #Generate ticket
    def generate_ticket(self):
        ticket = Ticket(self.ticket_counter)
        self.queue.append(ticket)
        self.ticket_counter += 1
        return ticket


    #Process the ticket
    def process_ticket(self):
        if self.queue:
            ticket = self.queue.popleft()
            return ticket
        return None
    
    def is_empty(self):
        return len(self.queue) == 0


def QueueSimulation(ticket_queue, num_ticket = 10):
    #simulate ticket generation and processing

    #Generate
    print("\nGenerate Ticket: ")
    for _ in range(num_ticket):
        ticket = ticket_queue.generate_ticket()
        print (f"Generated: {ticket}")
        time.sleep(random.uniform(.1,1))#simulate random arrival time
    #Process
    print("\nProcessing Ticket: ")
    while not ticket_queue.not_empty():
        ticket = ticket_queue.process_ticket()
        print(f"Processing Ticket {ticket}")
        time.sleep(random.uniform(1,2))




class testTicketSystem(unittest.TestCase):
    def setUp(self):
        self.queue = TicketQueue()

    #normal test
    def test_ticket_generation(self):
        ticket1 = self.queue.generate_ticket()
        self.assertEqual(ticket1.ticketNumber,1)

    def test_ticket_process(self):
        self.queue.generate_ticket()
        ticket1 = self.queue.process_ticket()
        self.assertEqual(ticket1.ticketNumber, 1)

    def test_process_empty_queue(self):
        self.assertIsNone(self.queue.process_ticket())

    
    def test_timestamp(self):
        time1 = self.queue.generate_ticket()
        time.sleep(1)
        time2 = self.queue.generate_ticket()
        self.assertTrue(time1.timestamp < time2.timestamp)

    def test_queue_is_empty_initial(self):
        self.assertTrue(self.queue.is_empty())
    
    def test_large_number_of_ticket(self):
        for _ in range(1000):
            self.queue.generate_ticket()
            time.sleep(1)
        for _ in range(1000):
            self.queue.process_ticket()
        self.assertTrue(self.queue.is_empty)

if __name__ == "__main__":
    unittest.main()
    queue = TicketQueue()
    QueueSimulation(queue, num_ticket= 10)