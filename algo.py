import random
# for inputing data from the available files
def read_data():
    courses=pd.read_csv("courses.csv")
    df=courses.drop_duplicates()
    df=pd.concat([df.iloc[-1:],df.iloc[:-1]])
    df.to_csv('courses_new.csv', index=False)
    # courses
    courses=pd.read_csv("courses_new.csv")
    teachers=pd.read_csv("teachers.csv")
    studentCourses=pd.read_csv("studentCourse.csv")
    df1=studentCourses.drop_duplicates()
#     merging different csv files.
    df1=pd.concat([df.iloc[-1:],df1.iloc[:-1]])
    df1.to_csv('StudentCourses_new.csv', index=False)
    studentCourses=pd.read_csv("StudentCourses_new.csv")
    studentName=pd.read_csv("studentNames.csv")
    
#     now arrange it such that the marketing courses are settled before.
def custom_sort(course_code):
        if course_code.startswith("MG"):
            return 0  # Management courses first
        else:
            return 1
#to generate population according to the restrictions.
def generate_population():
    read_data()
    #List of allowed classrooms
    allowed_classrooms = ["C301", "C302", "C303", "C304", "C305", "C306", "C307", "C308", "C309", "C310"]
    #Week days.
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # Generate exam schedule
    exam_schedule = []
    for day in days:
        start_hours = [9.00, 10.30, 12.00, 1.30, 3.00]  # Start hours of exams
        for hour in start_hours:
            classroom = random.choice(allowed_classrooms)
            exam_day = random.choice(days)
            if exam_day=='Friday':
                start_hours = [9.00, 10.30, 12.00, 2.30, 3.30]
            start_time = random.choice(start_hours)
            exam_schedule.append((classroom, exam_day, start_time))
    # Generate data for each exam
    exam_data = []
    for exam_slot in exam_schedule:
        classroom, exam_day, start_time = exam_slot
        # Randomly select course code, course name, and teacher from loaded data
        course = random.choice(courses["Course Code"])
        course_name = courses.loc[courses["Course Code"] == course, "Course Name"].iloc[0]
        teacher = random.choice(teachers["Names"])
        # Construct exam data
        exam_data.append((classroom, exam_day, start_time, course, course_name, teacher))
    # Generate DataFrame from exam_data
    exam_df = pd.DataFrame(exam_data, columns=["Classroom", "Exam Day", "Start Time", "Course Code", "Course Name", "Invigilating Teacher"])
#  sort the dataframes such that each exam has marketing programs first.
    exam_df["Sort_Key"] = exam_df["Course Code"].apply(custom_sort)
    exam_df_sorted = exam_df.sort_values(by=["Sort_Key"])
    exam_df_sorted.drop(columns=["Sort_Key"], inplace=True)
    exam_df_sorted.to_csv("Sorted_Exam.csv", index=False)
    return exam_df_sorted
def initial_population():
    # Generate two generations
    population1 = generate_population()
    population2= generate_population()
    return population1,population2

def fitness(individual):
    # Variables to track violations
    violations = {
        "no_exam_weekends": 0,
        "exam_time_range": 0,
        "teacher_conflict": 0
    }
    
    # Dictionary to track scheduled exams per course and teacher
    scheduled_exams_per_course = {}
    scheduled_exams_per_teacher = {}
    
    # Iterate over each exam in the individual
    for _, exam in individual.iterrows():
        # Constraint 1: Each course should have at least one exam scheduled
        course_code = exam["Course Code"]
        scheduled_exams_per_course[course_code] = scheduled_exams_per_course.get(course_code, 0) + 1

        # Constraint 2: Exam will not be held on weekends
        exam_day = exam["Exam Day"]
        if exam_day in ["Saturday", "Sunday"]:
            violations["no_exam_weekends"] += 1

        # Constraint 3: Each exam must be held between 9 am and 5 pm
        start_time = exam["Start Time"]
        if start_time < 9.00 or start_time > 17.00:
            violations["exam_time_range"] += 1

        # Constraint 4: Each exam must be invigilated by a teacher
        teacher = exam["Invigilating Teacher"]
        if teacher in scheduled_exams_per_teacher:
            # Check for teacher conflict
            last_exam_time = scheduled_exams_per_teacher[teacher]
            if last_exam_time == start_time:
                violations["teacher_conflict"] += 1
        scheduled_exams_per_teacher[teacher] = start_time
    
    # Calculate fitness score based on violations
    fitness_score= 100
    total_violations = sum(violations.values())
    fitness_score -= total_violations   # Invert the score so that higher fitness is better
    
    return fitness_score

# def roulette_wheel_selection(population, fitness_values):
#     total_fitness = sum(fitness_values)
#     selection_probs = [fit / total_fitness for fit in fitness_values]
#     return random.choices(population, weights=selection_probs)[0]

# def one_point_crossover(parent1, parent2):
#     crossover_point = random.randint(1, NUM_GENES - 1)
#     child1 = parent1[:crossover_point] + parent2[crossover_point:]
#     child2 = parent2[:crossover_point] + parent1[crossover_point:]
#     return child1, child2

# def swap_mutation(individual):
#     idx1, idx2 = random.sample(range(NUM_GENES), 2)
#     individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
#     return individual

# Genetic Algorithm

p1,p2= initial_population()
print(p2)
print(p1)
score1= fitness(p1)
print(score1)
score2 = fitness(p2)
score2
