from assembler import assemble
from cpu import MJCPU

def main():
    file = input("Enter file name: ")

    try:
        memory = assemble(file)

        cpu = MJCPU()
        cpu.memory = memory
        cpu.run()

    except FileNotFoundError:
        print("File not found")

    # catch any exceptions that might occur during cpu run
    except Exception as e:
        print(f"Simulation error: {e}")


if __name__ == "__main__":
    main()
