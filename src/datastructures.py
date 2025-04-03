"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.next_id = 1
        self._members = [{"id": self._generate_id(), "first_name": "John", "last_name": self.last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
                         {"id": self._generate_id(), "first_name": "Jane", "last_name": self.last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
                         {"id": self._generate_id(), "first_name": "Jimmy", "last_name": self.last_name, "age": 5, "lucky_numbers": [1]}
                         ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self.next_id
        self.next_id += 1
        return generated_id
    
    def add_member(self, member):
        if "id" not in member: # Aqui se verifica si el miembro no tiene un id, sino lo tiene...
            member["id"] = self._generate_id() # se le agrega un id aqui.
        member["last_name"] = self.last_name  # Asegurar que todos sean Jackson
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False 

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    
    # Actualizar un miembro por ID
    def update_member(self, id, updates):
        for member in self._members:
            if member["id"] == id:
                member.update(updates)
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
