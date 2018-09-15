t_test_case_count = input()

energy_rival_line = raw_input()
energy_rival_line_items = energy_rival_line.split(" ")

for test_case_index in range(0, t_test_case_count):
    e_energy_count = int(energy_rival_line_items[0])
    n_rival_team_count = int(energy_rival_line_items[1])

    rival_energy_line = raw_input()
    rival_energy_line_items = rival_energy_line.split(" ")

    battle_queue = []

    for i in range(0, n_rival_team_count):
        rival_dancing_skill = int(rival_energy_line_items[i])

        battle_queue.append(rival_dancing_skill)

    honor = 0

    # Admittedly, I did not have time to figure out what I should have done
    # I was still experimenting
    # We're out of time, so here's some source code
    # The below IS NOT AN OPTIMAL STRATEGY (or any STRATEGY yet)
    while len(battle_queue) > 0:
        print battle_queue
        if battle_queue[0] < e_energy_count:
            e_energy_count -= battle_queue.pop(0)
            honor += 1
        else:
            if honor > 0:
                e_energy_count -= battle_queue.pop(0)
                honor -= 1
            else:
                battle_queue.append(battle_queue.pop(0))
