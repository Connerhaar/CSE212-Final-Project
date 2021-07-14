class Linked_List:
    class Song_List:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None


    def queue_next_song(self, song):
        # Create the new node
        new_node = Linked_List.Song_List(song)
        
        # if there is no head set the head and tail as the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if there is a head do this
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node      

    def queue_last_song(self, song):
        # Creates a new node with the song name
        new_node = Linked_List.Song_List(song)

        # Checks of there is a tail and if there isnt it sets the head and tail as the new song
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If there is a tail it will set the new song as the tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        
    def delete_song(self, queued_song):
        number = self.head
        # If there is only one node it make an empty list
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # If the queued song is the head it will remove the head
        elif self.head.data == queued_song:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

        # If queued song is the tail it will remove the tail
        elif self.tail.data == queued_song:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        # if its not either of those it will loop through the linked list
        while number is not None:
            if number.data == queued_song:
                number.next.prev = number.prev
                number.prev.next = number.next
                return
            number = number.next

    def move_song(self, song_moved, moved_after_this_song):
        # Here is where you will begin your code
        pass

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "Song Queue: "
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += ""
        return output

Queue = Linked_List()
Queue.queue_next_song("Wow")
Queue.queue_next_song("Rockstar")
Queue.queue_last_song("Heaven")
Queue.queue_next_song("Hello")
print(Queue) # Song Queue: Hello, Rockstar, Wow, Heaven
Queue.delete_song("Rockstar")
Queue.move_song("Heaven", "Hello") 
print(Queue) # Song Queue: Hello, Heaven, Wow



