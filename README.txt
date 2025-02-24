# Conditional Expression Parser using Lark in Python

## Overview

This project implements a simple parser using the **Lark** library to evaluate conditional expressions in a custom syntax. It allows variable assignments and conditional execution based on `if-elif-else` statements.

## Features

- Supports **variable assignments** (`x`, `y`)
- Evaluates **if-elif-else** conditions
- Executes code blocks based on the conditions
- Uses **Lark** for grammar parsing
- Implements an **AST Transformer** to process expressions

## Installation

Make sure you have Python installed, then install the **Lark** library:

```bash
pip install lark-parser

python parser.py

Example Input:

The following program assigns values to x and y, then evaluates a conditional expression:
x = 2;
y = 3;
if (x < 3) { z = 10; } else if (y == 2) { z = 20; } else { z = 30; }

Output
The value of z is: 10
