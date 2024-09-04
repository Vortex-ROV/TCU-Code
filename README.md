# Topside Control Unit (TCU) Code Repository

Welcome to the repository for the Topside Control Unit (TCU) of Vortex ROV! This README will guide you through the prerequisites and file structure of the TCU software.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
  
## Introduction

The Topside Control Unit (TCU) serves as the primary interface for controlling the Vortex ROV during underwater operations. It enables operators to monitor real-time data, stream video feeds, and send commands to the ROV, ensuring precise control and mission success.

## Installation

To set up the TCU software on your development environment, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Vortex-ROV/TCU-Code.git
   cd TCU-Code
   ```

2. **Install Packaged Dependencies:**
   ```bash
   pip install .
   ```

3. **Run the TCU Software:**
   ```bash
   python main.py
   ```

## Repository Structure

- **`/src`:** Core source code for communication, control, and data processing.
- **`/tests`:** Test cases to validate the software's functionality and performance.
- **`main.py`:** Main script used to launch the TCU.
- **`Project_Config.toml`:** Configuration file for packaging TCU code.
