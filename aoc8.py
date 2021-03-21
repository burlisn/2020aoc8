def main() -> None:
    #variable declaration
    instruction_number: int = 0
    acc: int = 0 #the accumulator
    instructions_ran: list(int) = [] #keeps a list of the instruction numbers already ran
    keep_running: bool = True #boolean to keep while loop of instructions running

    #open input text file and get input
    with open("input.txt", "r") as fin:
        input_text=fin.read()

    #obtain list of instructions
    instruction_list=input_text.split('\n')

    #instruction while loop
    while keep_running:
        if instruction_number not in instructions_ran:
            instructions_ran.append(instruction_number)
            instruction_number, acc = perform_instruction(instruction_list[instruction_number], instruction_number, acc)
        elif instruction_number in instructions_ran:
            keep_running = False
    
    #print results
    print(acc)

    #testing
    # for instruction in instruction_list:
    #     instruction_parts=instruction.split()
    
    
#Function performs the instruction provided
#Returns: new instruction number and accumulator value
def perform_instruction(instruction: str, instruction_number: int, acc: int) -> int:
    instruction_parts=instruction.split()
    instruction_value=int(instruction_parts[1][1:])
    instruction_sign=instruction_parts[1][0]

    if instruction_parts[0] == "acc":
        if instruction_sign == '+':
            acc += instruction_value
        elif instruction_sign == '-':
            acc -= instruction_value
        instruction_number += 1
    
    elif instruction_parts[0] == "jmp":
        if instruction_sign == '+':
            instruction_number += instruction_value
        elif instruction_sign == '-':
            instruction_number -= instruction_value

    elif instruction_parts[0] == "nop":
        instruction_number += 1

    return instruction_number, acc

if __name__ == "__main__":
    main()