# Conditional-Expression-Parser-using-Lark
A simple conditional expression parser using the Lark library in Python. Supports variable assignments, if-elif-else conditions, and expression evaluation.

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
