def find_second_maximum():
    try:
        user_input = input().strip()
        
        if not user_input:
            print("-1")
            return
            
        numbers = list(map(int, user_input.split()))
        unique_numbers = set(numbers)
        
        if len(unique_numbers) < 2:
            print("-1")
        else:
            sorted_numbers = sorted(list(unique_numbers), reverse=True)
            print(sorted_numbers[1])
            
    except EOFError:
        print("-1")
    except ValueError:
        print("-1")

if __name__ == "__main__":
    find_second_maximum()
