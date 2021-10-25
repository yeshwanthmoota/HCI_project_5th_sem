from constants import *
import pygame
import random

class Node(): # Nodes of a Double Linked list

    def __init__(self, x, y, dir_num, prev, next):
        self.x = x # x-coordinate
        self.y = y # y-coordinate
        self.vel_direction = dir_num # direction number
        self.prev = prev
        self.next = next
        self.change_value = 0 # can be 0 or 1. 1 - for change, 0 - no change
    
    def update_x_y(self): # This function is the velocity function which updates the x and y of the nodes.
        if self.vel_direction == 1: # go up

            if self.y + SNAKE_NODE_SIDE > 0:
                self.y -= SNAKE_SPEED
            else: # Snake's node has gone off screen
                # We have to move to snake's node to the bottom of the screen to show continuity in the screen
                # Here self.y + SNAKE_NODE_SIDE <= 0
                self.y = HEIGHT - SNAKE_NODE_SIDE

        if self.vel_direction == 2: # go down

            if self.y + SNAKE_NODE_SIDE < HEIGHT:
                self.y += SNAKE_SPEED
            else: # Snake's node has gone off screen
                # We have to move to snake's node to the top of the screen to show continuity in the screen
                # Here self.y >= HEIGHT
                self.y = 0

        if self.vel_direction == 3: # go left

            if self.x + SNAKE_NODE_SIDE > 0:
                self.x -= SNAKE_SPEED
            else: # Snake's node has gone off screen
                # We have to move to snake's node to the right of the screen to show continuity in the screen
                # Here self.x + SNAKE_NODE_SIDE <= 0
                self.x = WIDTH - SNAKE_NODE_SIDE
        if self.vel_direction == 4: # go right

            if self.x + SNAKE_NODE_SIDE < WIDTH:
                self.x += SNAKE_SPEED
            else: # Snake's node has gone off screen
                # We have to move to snake's node to the left of the screen to show continuity in the screen
                # Here self.x >= WIDTH
                self.x = 0

class Snake(): # head of the Linked list



    def __init__(self):
        self.head = None # This is just the header node which points to the Snake.


    def initialize_snake(self):
        self.head = None
        for i in range(SNAKE_BIRTH_LENGTH):
            self.insert_node()



    def insert_node(self): # inserts the node at the end of the snake => the tail part of the snake
        if(self.head is None):
            node = Node(WIDTH//2,HEIGHT//2, 4, None,None) # first node is created
            self.head = node # first node of the snake
        else:
            ptr = Snake()
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next

            # now ptr.next = None => now ptr is at the last position in the Linked list

            # Now ptr.vel_direction tells the velocity direction of the last part of the node.

            if ptr.vel_direction == 1: # last node is moving in upwards 
                node = Node(ptr.x, ptr.y + SNAKE_NODE_SIDE, 1, ptr, None) # Node is inserted
                ptr.next = node

            elif ptr.vel_direction == 2: # last node is moving in downwards
                node = Node(ptr.x, ptr.y - SNAKE_NODE_SIDE, 2, ptr, None) # Node is inserted
                ptr.next = node

            elif ptr.vel_direction == 3: # last node is moving towards left
                node = Node(ptr.x + SNAKE_NODE_SIDE, ptr.y, 3, ptr, None) # Node is inserted
                ptr.next = node

            elif ptr.vel_direction == 4: # last node is moving towards right
                node = Node(ptr.x - SNAKE_NODE_SIDE, ptr.y, 4, ptr, None) # Node is inserted
                ptr.next = node

    def __len__(self):
        ptr = Snake()
        ptr = self.head
        count = 0

        while ptr is not None:
            count += 1
            ptr = ptr.next

        return count


    def update_all_nodes(self):
        ptr = Snake()
        ptr = self.head
        while ptr is not None:
            ptr.update_x_y()
            ptr = ptr.next

    def snake_movement(self):
        # This function is responsible for change in directions of all nodes with respect to the node before them.  
        ptr = Snake()
        ptr = self.head

        while ptr.next is not None:
            ptr = ptr.next
        # Now ptr.next is None => ptr is at the last node of the linked list
        while ptr is not self.head:
            if ptr.prev.change_value == 1:
                ptr.vel_direction = ptr.prev.vel_direction
                ptr.change_value = 1 # change the value since vel_direction changed
                ptr.prev.change_value = 0 # reset value to zero
            ptr = ptr.prev # move ptr backwards in the list
    

    def head_collision(self):
        rect1 = pygame.Rect(self.head.x, self.head.y, SNAKE_NODE_SIDE, SNAKE_NODE_SIDE) # head node's rectangle
        ptr = Snake()
        ptr = self.head.next # Checking from the 2nd node
        while ptr is not None:
            if(rect1.colliderect(pygame.Rect(ptr.x, ptr.y, SNAKE_NODE_SIDE, SNAKE_NODE_SIDE))): 
                return 1 # checking for head collision with body parts
            ptr = ptr.next
        return 0

    def food_spawn(self):
        ptr = Snake()
        ptr = self.head
        conditional = True
        while conditional: # first loop
            count = 1
            x = random.randrange(0, WIDTH - SNAKE_NODE_SIDE + 1, SNAKE_NODE_SIDE)
            y = random.randrange(0, HEIGHT - SNAKE_NODE_SIDE + 1, SNAKE_NODE_SIDE)

            while ptr is not None: # second loop
                if (x == ptr.x) and (y == ptr.y):
                    count = 0
                    break # breaks from the second loop
                ptr = ptr.next

            if count == 0:
                continue # rerun the first loop
            else:
                # count is not zero => it satisfied all the conditions
                return [x, y]

    def food_eaten(self, snake_food): # if food gets eaten then the snake increases in size by 1 node
        # returns true and false. And if true it increases the length of the snake by one node
        rect1 = pygame.Rect(self.head.x, self.head.y, SNAKE_NODE_SIDE, SNAKE_NODE_SIDE) # since head eats the food
        rect2 = pygame.Rect(snake_food[0], snake_food[1], SNAKE_NODE_SIDE, SNAKE_NODE_SIDE)
        condition = rect1.colliderect(rect2)
        if condition == True: # snake has eaten the food
            # snake's length has to be increased
            self.insert_node()
        return condition