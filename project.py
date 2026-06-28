import random


def main():
    loop_count = 3
    heads_count = 0
    
    print("\nWho are you?")
    name = input(">")
    print(f"Hello, {name}!")
    
    print("\nTossing a coin...\n")
    
    for i in range(loop_count):
        print(f"Round {i}: ", end="")
        isHeads = random.randint(0, 1)
        if isHeads: 
            heads_count += 1
            print("Heads")
        else:
            print("Tails")

    print(f"\nHeads: {heads_count}, Tails: {loop_count - heads_count}\n")
    print(f"You {'won' if heads_count > (loop_count - heads_count) else 'lost'}")

    
if __name__ == "__main__":
    main()
