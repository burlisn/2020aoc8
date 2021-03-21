def main() -> None:
    #variable declaration
    instruction_number: int = 0 #the instruction number
    acc: int = 0 #the accumulator
    instructions_ran: list[int] = [] #keeps a list of the instruction numbers already ran
    keep_running: bool = True #boolean to keep while loop of instructions running

    #open input text file and get input
    with open("input.txt", "r") as fin:
        input_text=fin.read()

    #obtain list of instructions
    instruction_list=input_text.split('\n')

    #instruction while loop (part 2)
    while keep_running:
        if instruction_number not in instructions_ran:
            instructions_ran.append(instruction_number)
            instruction_number, acc = perform_instruction(instruction_list[instruction_number], instruction_number, acc)
        elif instruction_number in instructions_ran:
            keep_running = False

    # -------------- Part 2 -------------------
    for i, inst in enumerate(instruction_list):
        if inst[0:3] == "nop":
            instruction_list[i]=instruction_list[i].replace("nop", "jmp")
            if(perform_run(instruction_list)[1] == True):
                acc = perform_run(instruction_list)[0]
            instruction_list[i]=instruction_list[i].replace("jmp", "nop")
        
        elif inst[0:3] == "jmp":
            instruction_list[i]=instruction_list[i].replace("jmp", "nop")
            if(perform_run(instruction_list)[1] == True):
                acc = perform_run(instruction_list)[0]
            instruction_list[i]=instruction_list[i].replace("nop", "jmp")
            
    #print results
    print(acc)
    
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

#Peforms 'run' of assembly code, checking whether it runs correctly (if the last instruction runs)
#Returns: value of accumulator (if it ran properly), boolean whether it ran properly
def perform_run(instruction_list: list[str]) -> tuple[int, bool]:
    instruction_number: int =0
    keep_running: bool = True
    instructions_ran: list[int] = []
    acc: int = 0

    while keep_running:
        if instruction_number == len(instruction_list):
            return acc, True
        elif instruction_number not in instructions_ran:
            instructions_ran.append(instruction_number)
            instruction_number, acc = perform_instruction(instruction_list[instruction_number], instruction_number, acc)
        elif instruction_number in instructions_ran:
            keep_running = False

    return 0, False





if __name__ == "__main__":
    main()