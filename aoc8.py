def main() -> None:
    #variable declaration
    instruction_number=0
    acc=0 #the accumulator

    #open input text file and get input
    with open("input.txt", "r") as fin:
        input_text=fin.read()

    #obtain list of instructions
    instruction_list=input_text.split('\n')

    #testing
    for instruction in instruction_list:
        print(instruction)
    
    

if __name__ == "__main__":
    main()