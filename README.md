# IAS Processor Simulator and Assembler

A Python-based implementation of the **IAS (Institute for Advanced Study) Computer Architecture**, developed as part of the EG-212 Computer Architecture course.

This project implements the complete workflow of a stored-program computer:

```text
C Program
    ↓
IAS Assembly Program
    ↓
Assembler
    ↓
Machine Code
    ↓
IAS Processor Simulation
    ↓
Program Output
```

The processor follows the classical **Von Neumann architecture**, where instructions and data share the same memory.

---

## Repository Structure

```text
Python Files/
│
├── __pycache__/
│   ├── IMT2023566_assembler.cpython-311.pyc
│   ├── IMT2023602_assembler.cpython-311.pyc
│   └── assembler.cpython-311.pyc
│
├── IMT2023602_Assembly_Code.txt
│   └── IAS Assembly program for HCF and LCM computation
│
├── IMT2023602_Processor.py
│   └── IAS processor simulator implementation
│
├── IMT2023602_assembler.py
│   └── Custom IAS assembler
│
├── Memory of the program.txt
│   └── Generated machine code / memory contents
│
├── IMT2023602_report.pdf
│   └── Project report and implementation details
│
└── Von_Neumann_Qn_Set.pdf
    └── Original assignment specification
```
---

# Project Objective

The objective is to design and simulate an IAS processor capable of:

- Fetching instructions from memory
- Decoding instructions
- Executing instructions
- Updating processor registers
- Performing memory operations
- Executing a complete assembly program

The project demonstrates how a stored-program computer executes instructions internally.

---

# Implemented Example Program

The assembly program computes:

- Highest Common Factor (HCF)
- Lowest Common Multiple (LCM)

for two user-provided positive integers.

### Example

```text
Enter a number : 12
Enter a number : 40

HCF = 4
LCM = 120
```

---

# IAS Components Simulated

The processor models the major IAS architecture blocks:

### Registers

- Program Counter (PC)
- Memory Address Register (MAR)
- Memory Buffer Register (MBR)
- Instruction Register (IR)
- Instruction Buffer Register (IBR)
- Accumulator (AC)
- Multiplier Quotient Register (MQ)

### Memory

- Unified instruction and data memory
- Simulated using Python lists

### Processor Stages

1. Fetch
2. Decode
3. Execute

---

# Custom Instructions Added

The original IAS ISA was extended with additional instructions.

| Instruction | Description |
|------------|-------------|
| MAX M(X) | Loads the larger of AC and M(X) into AC |
| MIN M(X) | Loads the smaller of AC and M(X) into AC |
| LTHAN0 M(X) | AC = 1 if M(X) ≤ 0 else AC = -1 |
| EQ0 M(X) | AC = 1 if M(X) = 0 else AC = -1 |
| MULT M(X) | AC = AC × M(X) |
| INPUT | Reads user input into AC |
| STOP | Terminates execution |

---

# Instruction Set Used

The assembly program uses:

- LOAD
- STORE
- ADD
- SUB
- DIV
- JUMP
- JUMP+
- MAX
- MIN
- MULT
- EQ0
- LTHAN0
- INPUT
- STOP

---

# How the Project Works

### Step 1 – Assembly Program

The IAS assembly code is stored in:

```text
IMT2023602_Assembly_Code.txt
```

This file contains the HCF-LCM algorithm written using IAS instructions.

---

### Step 2 – Assembler

The assembler reads the assembly file and converts it into machine code.

File:

```text
IMT2023602_assembler.py
```

Responsibilities:

- Parse assembly instructions
- Generate binary opcodes
- Generate machine memory image

---

### Step 3 – Processor Simulation

The processor loads the machine code and executes it instruction-by-instruction.

File:

```text
IMT2023602_Processor.py
```

Execution follows:

```text
Fetch
  ↓
Decode
  ↓
Execute
  ↓
Update Registers
  ↓
Next Instruction
```

until the STOP instruction is encountered.

---

# Running the Project

## Requirements

- Python 3.8+

Verify installation:

```bash
python --version
```

---

## Clone Repository

```bash
git clone https://github.com/<your-username>/IAS-Processor-Simulator.git
cd IAS-Processor-Simulator
```

---

## Execute the Processor

Run:

```bash
python IMT2023602_Processor.py
```

The processor automatically:

1. Imports the assembler
2. Loads machine code
3. Initializes memory
4. Simulates IAS execution
5. Requests user input
6. Displays HCF and LCM

---

## Example Run

```text
Enter a number : 12
Enter a number : 40

HCF = 4
LCM = 120
```

---

# Academic Context

This project was developed as part of:

**EG-212 – Computer Architecture**

Assignment Objectives:

- Design an IAS Assembly Program
- Implement an Assembler
- Implement an IAS Processor Simulator
- Extend the ISA with custom instructions
- Demonstrate execution of a complete program

---

# References

- IAS Computer Architecture
- Von Neumann Architecture
- Computer Organization and Design
- EG-212 Computer Architecture Course Material

---

## Contributors

- R. Vaikunth (IMT2023566)
- A. Shudharshan (IMT2023602)
- S. Santhosh Kiran (IMT2023065)

---

## Acknowledgements

Developed as part of the EG-212 Computer Architecture course project on IAS Processor Design and Simulation.
