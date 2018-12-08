
series_of_steps = {}
start_with = ''
sequence = ''
candidates = []
candidate_key = ''
total_length_of_sequence = 0
unique_steps = set()


def calculate_steps(total_length_of_sequence, candidates, sequence):
    if total_length_of_sequence == 1:
        print(sequence)
        print(total_length_of_sequence)
        return
    #import pdb;pdb.set_trace()
    #print(candidates)
    while total_length_of_sequence > 0:
        for candidate in candidates:
            if candidate in sequence:
                continue
            try:
                more_candidates = series_of_steps[candidate]
            except:
                more_candidates = []
            potential_candidate = []
            # are more candidates part of any other key
            if candidate not in sequence:
                sequence = sequence + candidate

            for new_candidate in more_candidates:
                single_only = True
                for key, value in series_of_steps.iteritems():
                    if key not in sequence:
                        if new_candidate in value:
                            single_only = False
                            break
                if single_only:
                    potential_candidate.append(new_candidate)
            #if candidate not in sequence:
            total_length_of_sequence -= 1
            #candidates.remove(candidate)
            candidates = candidates + potential_candidate
            candidates.sort()
        #import pdb;pdb.set_trace()
        
        calculate_steps(total_length_of_sequence, candidates, sequence)
        
        #candidates = [candi for candi in candidates if candi not in sequence]

if __name__ == "__main__":
    with open('input_test.txt') as fp:
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
            candidates = candidates + series_of_steps[key]

    total_length_of_sequence = len(unique_steps) + 1
    sort_seq = []
    for d in sequence:
        sort_seq.append(d)
    sort_seq.sort()
    sequence = ''.join(sort_seq)
    
    while total_length_of_sequence > 1:
        print(candidates)

        for candidate in candidates:
            print(candidate)
            import pdb;pdb.set_trace()
            if candidate in sequence:
                continue
            if candidate not in sequence:
                #print(candidate)
                sequence = sequence + candidate
                total_length_of_sequence -= 1

            try:
                more_candidates = series_of_steps[candidate]
            except:
                more_candidates = []
            potential_candidate = []
            # are more candidates part of any other key
            
            for new_candidate in more_candidates:
                single_only = True
                for key, value in series_of_steps.iteritems():
                    if key not in sequence:
                        if new_candidate in value:
                            single_only = False
                            break
                if single_only:
                    potential_candidate.append(new_candidate)
            #if candidate not in sequence:
            new_c = candidates + potential_candidate
            #print(new_c)
            new_c.sort()
            #print(new_c)
            candidates = list()
            #candidates.remove(candidate)
            candidates = new_c
            
            candidates.sort()
            
    print(sequence)    
    #sequence = calculate_steps(total_length_of_sequence, candidates, sequence)
    
