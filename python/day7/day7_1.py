
series_of_steps = {}
sequence = ''
candidates = []
total_length_of_sequence = 0
unique_steps = set()



if __name__ == "__main__":
    with open('input.txt') as fp:
        for input in fp:
            step = input.replace("Step","").replace("must be finished before step", "").replace("can begin.","").strip().split(' ')
            if step[0] not in series_of_steps:
                series_of_steps[step[0]] = [step[2]]
                unique_steps.add(step[2])
            else:
                series_of_steps[step[0]].append(step[2])
                unique_steps.add(step[2])

    for key, value in series_of_steps.iteritems():
        found = False
        value = value.sort()
        for ikey, ivalue in series_of_steps.iteritems():
            if ikey == key:
                continue
            else:
                if key in ivalue:
                    found = True

        if found == False:
            sequence = sequence + key
            if len(sequence) == 1:
                pot_candi = series_of_steps[key]
                
                for new_candidate in pot_candi:
                    single_only = True
                    for ikey, value in series_of_steps.iteritems():
                            if new_candidate in value and ikey != key:
                                single_only = False
                                break
                    if single_only:
                        candidates.append(new_candidate)

            else:
                pass

    total_length_of_sequence = len(unique_steps) + 1
    sort_seq = []
    for d in sequence:
        sort_seq.append(d)
    sort_seq.sort()
    sequence = sort_seq[0]
    candidates = candidates + [sort_seq[1]]
    candidates = candidates + [sort_seq[2]]
    candidates.sort()
    
    restart = False
    while total_length_of_sequence > -1:
        for candidate in candidates:
            if candidate in sequence:
                continue
            if candidate not in sequence:
                canbe_step_now = True
                for key, value in series_of_steps.iteritems():
                    if key not in sequence:
                        if candidate in value:
                            canbe_step_now = False
                            break
                if canbe_step_now:
                    sequence = sequence + candidate
                    total_length_of_sequence -= 1
            try:
                more_candidates = series_of_steps[candidate]
            except:
                more_candidates = []
            potential_candidate = []
                        
            for new_candidate in more_candidates:
                if new_candidate not in candidates:
                    potential_candidate.append(new_candidate)
            candidates.remove(candidate)
            new_c = candidates + potential_candidate
            new_c.sort()
            candidates = new_c
            break
            
    print(sequence)    

    
