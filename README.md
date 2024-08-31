# Automatic Timetable Generation with Genetic Algorithm

This Python project implements an automatic timetable generation system using a genetic algorithm. The program generates timetables based on a set of hard and soft constraints, achieving an accuracy rate of at least 93%. All functionalities are implemented from scratch, including file handling and the genetic algorithm.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
  - [Data Input](#data-input)
  - [Genetic Algorithm](#genetic-algorithm)
  - [Function Definitions](#function-definitions)
- [Contributing](#contributing)
- [License](#license)

## Overview

This program aims to automate the process of timetable generation, considering various constraints such as classroom availability, course scheduling, and teacher assignments. By employing a genetic algorithm, the system optimizes the timetable generation process to meet these constraints efficiently.

## Usage

To use the program, follow these steps:
1. Ensure all input data files (`courses.csv`, `teachers.csv`, `studentCourse.csv`, `studentNames.csv`) are correctly formatted.
2. Run the Python script to execute the automatic timetable generation.
3. Review the generated timetable output for accuracy and efficiency.

## Implementation Details

### Data Input

The program reads input data from CSV files containing information about courses, teachers, and student enrollment. Data preprocessing is performed to handle duplicates and ensure data consistency.

### Genetic Algorithm

The genetic algorithm is employed to generate timetables based on the input data and defined constraints. Two generations of populations are generated, and selection, crossover, and mutation operations are performed to evolve the population and optimize the timetable generation process.

### Function Definitions

1. **`read_data()`**:
   - This function reads data from CSV files containing information about courses, teachers, student courses, and student names.
   - It performs preprocessing to handle duplicates and ensure data consistency.
   - Finally, it arranges the data such that marketing courses are scheduled before others.

2. **`custom_sort(course_code)`**:
   - This is a helper function used for custom sorting based on the course code.
   - It returns 0 if the course code starts with "MG" (for management courses) and 1 otherwise.

3. **`generate_population()`**:
   - This function generates a population of exam schedules.
   - It randomly selects classrooms, exam days, and start times for each exam based on predefined constraints.
   - The generated data includes details such as classroom, exam day, start time, course code, course name, and invigilating teacher.

4. **`initial_population()`**:
   - This function generates two initial populations of exam schedules using the `generate_population()` function.

5. **`fitness(individual)`**:
   - This function calculates the fitness score for a given exam schedule (individual).
   - It evaluates adherence to various constraints such as no exams on weekends, exam time range, and teacher conflicts.
   - The fitness score is calculated based on the number of violations of these constraints.

6. **`roulette_wheel_selection(population, fitness_values)`**:
   - This function performs roulette wheel selection to choose individuals from the population based on their fitness values.
   - Individuals with higher fitness values have a higher probability of being selected.

7. **`one_point_crossover(parent1, parent2)`**:
   - This function performs one-point crossover between two parent individuals.
   - It randomly selects a crossover point and swaps the exam schedules of the parents to create two new child individuals.

8. **`swap_mutation(individual)`**:
   - This function performs swap mutation on an individual's exam schedule.
   - It randomly selects two distinct exams and swaps their positions to introduce diversity in the population.


## Contributing

Its a pair project done with collaboration of Mahnoor Mehmood and Zoha Wajahat

