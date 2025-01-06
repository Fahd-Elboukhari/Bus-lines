Bus Line Search Application

Overview

This application is a graphical user interface (GUI) built using Python's Tkinter library. It allows users to search for bus lines, view details such as fares, and display the stops for each line. Users can seamlessly navigate between the main menu and specific bus line details.

Features

Search Functionality: Filter bus lines by number or description using a search bar.

Dynamic Display: View detailed information about each line, including fares.

Stops Display: Show stops for a selected bus line by clicking a button.

Navigation: Return to the main menu from the stops view without retaining previous data.

Scrollable Interface: Allows easy navigation for large lists of bus lines.

Requirements

Python 3.x

Tkinter (included with standard Python installations)

Installation

Clone or download this repository.

Ensure Python is installed on your system.

Save the required files:

The main Python script.

A separate file (lignes.py) containing data for bus lines and stops.

Run the script using:

python main.py

Usage

Launch the application.

Use the search bar to filter bus lines.

Click the '>' button to view stops for a specific line.

Press the "Retour" button to return to the main menu without displaying stops.

File Structure

main.py - The main script containing the application code.

lignes.py - Data file storing bus lines and stops.

Example Data (lignes.py):

bus_lines = [
    ("L201B", "CHATEAU SALAM - ZONE ECONOMIQUE", "5dh"),
    ("AE", "AEROPORT-GARE AGDAL", "25dh")
]

bus_stops = {
    "L201B": ["Stop1", "Stop2", "Stop3"],
    "AE": ["Airport", "Station"]
}

Notes

Ensure lignes.py is present in the same directory as the main script.

Modify lignes.py to add or update bus lines and stops.

License

This project is open-source and free to use.

