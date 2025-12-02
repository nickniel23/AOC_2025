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

            index, hit_zero = move(index, steps, total_values)
            if hit_zero: 
                count += 1

    print(count) 
            

def move(index: int, steps: int, total_values: int) -> tuple[int, bool]: 

    new_index = (index + steps) % total_values
    hit_zero = (new_index == 0)   

    return new_index, hit_zero
 
if __name__ == "__main__":
    main()
