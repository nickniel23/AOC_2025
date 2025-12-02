def main():
    
    index: int = 50 # starting index 
    count: int = 0 # num of times the counter is left at 0
    total_values: int = 100

    with open("input.txt", encoding="utf-8" ) as f:
        for line in f:
            line = line.strip()
           
            if not line: 
                continue
            direction = line[0]
            steps = int(line[1:])
 
            if direction == "L":
                steps *= -1

            index, hits = move(index, steps, total_values)
            count += hits

    print(count) 
            

def move(index: int, steps: int, total_values: int) -> tuple[int, int]: 

    hits: int = 0
    step_direction = 1 if steps > 0 else -1

    for i in range(abs(steps)):
        index = (index + step_direction) % total_values
        if index == 0:
            hits +=1

    return index, hits 
 
if __name__ == "__main__":
    main()
