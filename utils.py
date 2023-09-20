def calculate_damage(cell, org):
    cell_temp_is_dangerous = not (cell.cell_temp > org.temp_range[0] and cell.cell_temp < org.temp_range[1])
    if cell_temp_is_dangerous:
        dmg = 0
        if cell.cell_temp > org.temp_range[1]:
            dmg = abs(abs(cell.cell_temp) - abs(org.temp_range[1]))
        else:
            dmg = abs(abs(cell.cell_temp) - abs(org.temp_range[0]))
        org.health -= dmg