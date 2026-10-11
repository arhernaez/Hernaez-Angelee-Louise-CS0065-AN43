
import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------- Get user input from console --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# -------- Agent Definition -----------
class RandomWalker(ap.Agent):
    def setup(self):
        self.path = []

    def step(self):
        x, y = self.position

        # Possible movement directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Get positions occupied by other agents
        occupied = {
            agent.position
            for agent in self.model.agents
            if agent is not self
        }

        # Find valid moves that stay inside the grid and avoid other agents
        valid_moves = []

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if (0 <= new_x < self.model.p.grid_size[0]
                and 0 <= new_y < self.model.p.grid_size[1]
                and (new_x, new_y) not in occupied):
                valid_moves.append((dx, dy))

        # Choose a random valid move
        if valid_moves:
            dx, dy = random.choice(valid_moves)
            self.position = (x + dx, y + dy)

        # Record the position
        self.path.append(self.position)

# -------- Model Definition -----------
class RandomWalkModel(ap.Model):
    def setup(self):
        # Create agents
        self.agents = ap.AgentList(self, self.p.agents, RandomWalker)

        # Assign unique random starting positions
        positions = random.sample(
            [(x, y)
             for x in range(self.p.grid_size[0])
             for y in range(self.p.grid_size[1])],
            self.p.agents
        )

        for agent, position in zip(self.agents, positions):
            agent.position = position
            agent.path.append(position)

        # Create grid
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.grid.add_agents(self.agents)

    def step(self):
        for agent in self.agents:
            agent.step()

# -------- Parameters from user input -----------
parameters = {
    'agents': num_agents,
    'grid_size': (grid_size, grid_size),
    'steps': num_steps
}

# Check that there is enough space for all agents
if num_agents < 1 or num_agents > grid_size * grid_size:
    raise ValueError("Invalid number of agents for the given grid size.")

# -------- Run Model -----------
model = RandomWalkModel(parameters)
model.setup()

# -------- Interactive Animation -----------
fig, ax = plt.subplots()

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_xticks(range(grid_size + 1))
ax.set_yticks(range(grid_size + 1))
ax.grid(True)

scat = ax.scatter([], [], s=200)

# Create a path line for each agent
lines = [ax.plot([], [], linewidth=1)[0] for agent in model.agents]

def update(frame):
    model.step()

    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]
    scat.set_offsets(list(zip(x, y)))

    # Display each agent's path
    for i, agent in enumerate(model.agents):
        path_x = [pos[0] for pos in agent.path]
        path_y = [pos[1] for pos in agent.path]
        lines[i].set_data(path_x, path_y)

    return scat, *lines

ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    blit=True,
    repeat=False
)

plt.show()

# -------- Display Recorded Paths -----------
for i, agent in enumerate(model.agents):
    print(f"Agent {i+1} path: {agent.path}")

# -------- Record Final Positions -----------
print("\n--- Final Agent Positions ---")

final_positions = []

for i, agent in enumerate(model.agents):
    final_position = agent.position
    final_positions.append(final_position)

    print(f"Agent {i+1}: {final_position}")
