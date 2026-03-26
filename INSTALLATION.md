# Installation Instructions

## System Requirements
- Operating System: Windows, macOS, or Linux
- Python: 3.8 or higher

## Installation Steps

1. **Install Python 3.8+**  
   Download and install Python from the official [Python website](https://www.python.org/downloads/). Make sure to add Python to your system's PATH.

2. **Clone the Repository**  
   Open a terminal and run the following command:
   ```bash
   git clone https://github.com/WOLFbl4/my-project-info.git
   ```

3. **Navigate to the Project Directory**  
   ```bash
   cd my-project-info
   ```

4. **Set up a Virtual Environment**  
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**  
   Run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**  
   Finally, start the application with:
   ```bash
   python main.py
   ```

## Additional Notes
  - Make sure your terminal is pointed to the project directory where `main.py` is located before executing the run command.
