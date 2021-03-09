class Room:
    def __init__(self, name: str, linked_rooms: dict = dict()):
        """
        Initializes new room.
        """
        self.name = name
        self.linked_rooms = dict()
        self.item = None
        self.character = None


    def set_description(self, description):
        """
        Sets description of the room.
        """
        self.description = description


    def link_room(self, room, route: str):
        """
        Set another room which is linked with current one.
        """
        self.linked_rooms.update({route: room})


    def set_character(self, character):
        """
        Put a Character into your room.
        """
        self.character = character


    def set_item(self, item):
        """
        Put an Item into your room.
        """
        self.item = item


    def get_details(self):
        """
        Shows details about certain room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)

        if len(self.linked_rooms) > 0:
            for direction in self.linked_rooms:
                room = "The " + self.linked_rooms[direction].name + " is " + direction
                print(room)


    def get_character(self):
        """
        Returns a Character which is located in this room.
        """
        return self.character


    def get_item(self):
        """
        Returns item which is in the room.
        """
        return self.item


    def move(self, direction):
        """
        Returns room object which is chosen.
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]


class Character:
    def __init__(self, name, description):
        """
        Initializes a Character.
        """
        self.name = name
        self.description = description


    def set_conversation(self, conversation):
        """
        Sets character's quote.
        """
        self.conversation = conversation


    def describe(self):
        """
        Describes a character.
        """
        character = self.name + " is here!"
        print(character)
        print(self.description)


    def talk(self):
        """
        Returns Character's quote.
        """
        print(self.conversation)


class Enemy(Character):
    defeated = 0

    def __init__(self, name, description):
        """
        Initializes a new Enemy.
        """
        super().__init__(name, description)


    def set_weakness(self, weakness):
        """
        Sets Enemy's weakness.
        """
        self.weakness = weakness


    def fight(self, item):
        """
        You put a fight with this Enemy while using item.
        """
        if item == self.weakness:
            Enemy.defeated += 1
        return item == self.weakness


    def get_defeated(self):
        """
        Returns how many Enemies did you defeat.
        """
        return Enemy.defeated


class Ally(Character):
    pass


class Item:
    def __init__(self, name):
        """
        Initializes an Item.
        """
        self.name = name


    def set_description(self, description):
        """
        Sets description of an Item.
        """
        self.description = description


    def describe(self):
        """
        Returns item's description.
        """
        print(f"The {self.name} is here - {self.description}")


    def get_name(self):
        """
        Returns item's name.
        """
        return self.name
