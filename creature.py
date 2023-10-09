import random

import numpy as np

from ambiente_params import env_grid_size
from creature_params import (
    org_class_map,
    org_healths,
    org_interaction_priority,
    org_movement_velocity,
    org_sensing_range,
    org_temp_increments,
    org_temp_ranges,
)

np.random.seed(42)
random.seed(42)


class Organism:
    def __init__(self, position, name) -> None:
        self.name = name
        self.x, self.y, self.z = position

        self.name_class_map = org_class_map
        self.temp_range = org_temp_ranges[name]
        self.health = org_healths[name]
        self.temp_incr = org_temp_increments[name]
        self.sensing_range = org_sensing_range[name]
        self.org_interaction_priority = org_interaction_priority[name]
        self.movement_velocity = org_movement_velocity[name]

        self.is_dead = False

    @classmethod
    def create(cls, position, name):
        class_name = org_class_map.get(
            name
        )  # Get class name from map or default to Organism
        module = __import__(
            cls.__module__
        )  # Import the module where this class is defined
        class_ = getattr(module, class_name)  # Get the class from the module
        return class_(position)

    def interact(self, env_space_temps=None):
        delta_pos = self.move(env_space_temps)
        return delta_pos

    def move(self, *kwargs):
        dx, dy, dz = (
            random.randint(-1, 1),
            random.randint(-1, 1),
            random.randint(-1, 1),
        )
        return dx, dy, dz

    def get_surroundings(self):
        rx = (
            max(0, self.x - self.sensing_range),
            min(self.x + self.sensing_range + 1, env_grid_size[0]),
        )
        ry = (
            max(0, self.y - self.sensing_range),
            min(self.y + self.sensing_range + 1, env_grid_size[1]),
        )
        rz = (
            max(0, self.z - self.sensing_range),
            min(self.z + self.sensing_range + 1, env_grid_size[2]),
        )

        return rx, ry, rz

    def get_movement_towards_target(self, pos, target_pos, velocity):
        print(pos, target_pos)
        x, y, z, target_x, target_y, target_z = *pos, *target_pos

        dx = target_x - x
        dy = target_y - y
        dz = target_z - z

        distance = np.sqrt(dx**2 + dy**2 + dz**2)

        if distance == 0:
            return 0, 0, 0

        dx_norm, dy_norm, dz_norm = dx / distance, dy / distance, dz / distance

        dx_step, dy_step, dz_step = (
            round(dx_norm * velocity),
            round(dy_norm * velocity),
            round(dz_norm * velocity),
        )

        # Ensure we don't overshoot the target
        dx_step = min(abs(dx), abs(dx_step)) * (1 if dx > 0 else -1)
        dy_step = min(abs(dy), abs(dy_step)) * (1 if dy > 0 else -1)
        dz_step = min(abs(dz), abs(dz_step)) * (1 if dz > 0 else -1)

        return dx_step, dy_step, dz_step


class Bacteria(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, "bacteria")

    # def interact(self, *kwargs):
    #     pass


class Virus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, "virus")

    def interact(self, env_space_temps):
        detection_ranges = self.get_surroundings()
        local_env_space_temps = self.get_surroundings_values(
            detection_ranges, env_space_temps
        )
        target_pos = self.get_target_move_pos(detection_ranges, local_env_space_temps)
        delta_pos = self.move(target_pos=target_pos)

        return delta_pos

    def move(self, target_pos=None):
        if target_pos:
            # dx, dy, dz = target_pos[0]-self.x, target_pos[1]-self.y, target_pos[2]-self.z
            dx, dy, dz = self.get_movement_towards_target(
                (self.x, self.y, self.z), target_pos, self.movement_velocity
            )
        else:
            dx, dy, dz = super().move()
        return dx, dy, dz

    def get_surroundings_values(self, detection_ranges, env_space_temps):
        rx, ry, rz = detection_ranges
        return env_space_temps[rx[0] : rx[1], ry[0] : ry[1], rz[0] : rz[1]]

    def get_target_move_pos(self, detection_ranges, local_env_space_temps):
        rx, ry, rz = detection_ranges
        max_index_flat = np.argmax(local_env_space_temps)
        local_max_index = np.unravel_index(max_index_flat, local_env_space_temps.shape)
        global_max_index = (
            local_max_index[0] + rx[0],
            local_max_index[1] + ry[0],
            local_max_index[2] + rz[0],
        )
        return global_max_index

    def decide_action(self, surroundings):
        # IDEA:
        # org_value_map = {
        #     'move': self.genome['mobility'] * nutrients,  # Just an example calculation
        #     'attack': self.genome['infectivity'] * len(neighbors),
        #     'rest': self.genome['transmissibility']  # Another example
        # }
        pass


class Fungus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, "fungus")

    def interact(self, *kwargs):
        delta_pos = self.move()
        return delta_pos

    def move(self, *args):
        return 0, 0, 0
