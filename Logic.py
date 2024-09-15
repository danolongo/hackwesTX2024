import time

def logic(rows, cols, cell_array, interation):
    for i in range(rows):
        for j in range(cols):
            if cell_array[i][j].enabled > 0:
                cell_array[i][j].change_enabled(-1)

    for i in range(rows):
        for j in range(cols):
            if cell_array[i][j].state == 1:
                dummy = interation

            elif cell_array[i][j].state == 2:
                if cell_array[i][j].enabled == 0:
                    if cell_array[i][j].signal == 1:
                        for transmitters in cell_array[i][j].find_enabled_transmitters():
                            transmitters.change_signal(1)
                            transmitters.set_enabled(1)
                        cell_array[i][j].set_signal(0)
                        cell_array[i][j].set_enabled(3)
                    elif cell_array[i][j].signal > 1:
                        cell_array[i][j].set_signal(0)
                        for transmitters in cell_array[i][j].find_enabled_transmitters():
                            transmitters.set_enabled(1)

            elif cell_array[i][j].state == 3:
                if cell_array[i][j].enabled == 0:
                    if cell_array[i][j].signal > 0:
                        cell_array[i][j].set_state(4)
                        cell_array[i][j].set_enabled(1)

            elif cell_array[i][j].state == 4:
                if cell_array[i][j].enabled == 0:
                    for transmitters in cell_array[i][j].find_enabled_transmitters():
                        transmitters.change_signal(1)
                        transmitters.change_enabled(1)
                    cell_array[i][j].set_signal(0)
                    cell_array[i][j].set_state(3)
                    cell_array[i][j].set_enabled(1)

    time.sleep(1)
    interation += 1