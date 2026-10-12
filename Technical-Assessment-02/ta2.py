#Task 1: Set Up Environment

#Initialize two rooms
rooms = {
    "A": "",
    "B": ""
}

#Let the user set the initial state of each room
for room in rooms:
    state = input(f"Is Room {room} dirty or clean? ").lower()

    while state not in ["dirty", "clean"]:
        state = input("Invalid input. Enter dirty or clean: ").lower()

    rooms[room] = state

#function: check if a room is dirty
def is_dirty(room):
    return rooms[room] == "dirty"

#function: clean a room
def clean_room(room):
    rooms[room] = "clean"


#Task 2: Implement Rule-Based Agent
class Agent:
    def __init__(self):
        self.location = "A"

    #function: move to the other room
    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    #function: perceive and act based on the room's state
    def perceive_and_act(self):
        if is_dirty(self.location):
            clean_room(self.location)
            action = "Cleaned Room " + self.location
        else:
            self.move()
            action = "Moved to Room " + self.location

        return action


#Task 3: Run Simulation

agent = Agent()

steps = int(input("\nHow many steps should the simulation run? "))

for step in range(steps):
    print(f"\nStep {step + 1}")

    action = agent.perceive_and_act()

    print("Agent Location:", agent.location)
    print("Action Taken:", action)
    print("Environment State:", rooms)
