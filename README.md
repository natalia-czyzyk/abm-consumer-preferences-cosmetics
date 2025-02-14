# An agent-based analysis of consumer preferences in the introduction of novel sustainable cosmetics

This repository contains the implementation of an agent-based model designed as part of a master's thesis to simulate the adoption and spread of sustainable cosmetics within a network of potential buyers. The model is intended to be a customizable, user-friendly tool for companies aiming to evaluate the impact of various product characteristics and marketing strategies on consumer behavior.

## Project Overview

The project is based on a comprehensive literature review and a consumer survey conducted in Poland, with 281 respondents providing insights into their preferences and behaviors related to sustainable cosmetics. Data analysis was performed using Python, and the model was built in NetLogo.


## Key Components

- **Survey Data Analysis**: Conducted with Python (Pandas library), analyzing correlations between consumer preferences and behaviors.

- **Agent-Based Model**: Implemented in NetLogo, simulating consumer interactions, product adoption, and marketing impact.

- **Product Value Configuration**: Customizable through price, quality, and attributes such as cruelty-free, natural, and recycled packaging.

- **Agent Characteristic**s: Agents have attributes like influence status, intent to buy, and participation status.

- **Marketing Campaign Simulation**: Configurable frequency and reach to assess campaign effectiveness.


## Features

- **Customizable Parameters**: Adjust product value, agent count, influencer percentage, and marketing campaign details.

- **Dynamic Interactions**: Agents interact based on status and influence, simulating real-world recommendation dynamics.

- **Comprehensive Analysis**: Supports evaluation of various product attributes and marketing strategies.


## Project Structure

All files are stored in the main directory for simplicity.

**data.csv** – Survey data collected from 281 respondents

**data_analysis.py** – Python script for analyzing the survey data

**sustainable_cosmetics.nlogo** – NetLogo agent-based model

**README.md** – Project documentation (this file)

**results.pdf** – Document with results


## Setup and Usage

Prerequisites:

- Python 3.x for data analysis scripts

- NetLogo 6.x for running the agent-based model


## Installation

Clone the repository:

**git clone https://github.com/username/sustainable-cosmetics-abm.git**


## Running the Model

**Data Analysis:**

- Run **data_analysis.py** to reproduce the survey data analysis.


**NetLogo Model:**

- Open **sustainable_cosmetics_model.nlogo** in NetLogo.

- Configure parameters via the interface sliders.

- Run simulations and observe product adoption dynamics.


## Results

The model helps in understanding:

- Influence of product attributes on adoption

- Effectiveness of marketing campaigns

- Dynamics of consumer behavior in the sustainable cosmetics market


## Contributors

Natalia Czyżyk - Master's thesis author

Prof. Anna Kowalska - Pyzalska - Master's thesis supervisor at Wrocław University of Science and Technology


## Acknowledgments

Survey respondents and contributors

Supervisors and academic mentors

Open-source tools: Python, Pandas, NetLogo
