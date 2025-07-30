# Doctor Appointment Multiagent System

This project is a multi-agent system for managing doctor appointments. It leverages Python and Streamlit for the user interface, and organizes logic into agents, toolkits, and data models for modularity and scalability.

## Features

- Multi-agent architecture for appointment scheduling
- Doctor availability management
- Streamlit-based UI for easy interaction
- Extensible prompt library and toolkit
- Data models for structured information

## Project Structure

```
agent.py                # Main agent logic
main.py                 # Entry point for running the system
streamlit_ui.py         # Streamlit user interface
requirements.txt        # Python dependencies
setup.py                # Package setup
README.md               # Project documentation

/data                   # Doctor availability data
/data_models            # Data models for agents
/prompt_library         # Prompt templates and logic
/toolkit                # Tools for agent operations
/utils                  # Utility functions (e.g., LLMs)
/notebook               # Jupyter notebook for experiments
```

## Getting Started

1. **Clone the repository**
   ```powershell
   git clone https://github.com/adityaraj31/doctor-appoitment-multiagent.git
   cd doctor-appoitment-multiagent-main
   ```
2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Run the Streamlit UI**
   ```powershell
   streamlit run streamlit_ui.py
   ```

## Usage

- Use the Streamlit interface to book appointments and view doctor availability.
- Modify agent logic in `agent.py` for custom workflows.
- Update data in `/data/doctor_availability.csv` as needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
