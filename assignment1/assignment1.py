# Task 1: Hello

def hello():
    return "Hello!"

print(hello())


# Task 2: Greet with a Formatted String

def greet(name):
    return f"Hello, {name}!"

print(greet("Boris"))


# Task 3: Calculator

def calc(x, y, operator = "multiply"):
    try:
        match operator:
            case "add":
                return x + y
            case "subtract":
                return x - y
            case "multiply":
                return x * y
            case "divide":
                if y == 0:
                    raise ZeroDivisionError
                return x / y
            case "modulo":
                return x % y
            case "int_divide":
                if y == 0:
                    raise ZeroDivisionError
                return x // y
            case "power":
                return x ** y
            case _:
                return "Error: Invalid operator"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(3,5, "add"))

# Task 4: Data Type Conversion

def  data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        else:
            raise ValueError
    except ValueError:
        return f"You can't convert {value} into a {type}."
   

print(data_type_conversion(5, "float"))
print(data_type_conversion(7.5, "int"))
print(data_type_conversion(5, "str"))
print(data_type_conversion("five", "float"))


# Task 5: Grading System, Using *args

def grade(*args):
    try:
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid data was provided."


print(grade(1, 3, 5, 17, 100))


# Task 6: Use a For Loop with a Range

def repeat(string, count):
    result = ""
    for word in range(count):
        result+=string
    return result
    

print(repeat("horray", 10))


# Task 7: Student Scores, Using **kwargs

def student_scores(par, **kwargs):
    if par == "best":
        bestStudent = None
        bestScore = 0
        for student, score in kwargs.items():
            if score > bestScore:
                bestScore = score
                bestStudent = student
        return bestStudent
    if par == "mean":
        total = 0
        numStudents = len(kwargs)
        for student, score in kwargs.items():
            total += score
        mean = total / numStudents
    return mean

print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))
print(student_scores("mean", Tom=75, Dick=89, Angela=91))


# Task 8: Titleize, with String and List Operations

def titleize(string):
    words = string.split()
    short_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            words[i] = word.capitalize()
        elif word not in short_words:
            words[i] = word.capitalize()
    text = " ".join(words)
    return text

print(titleize("after on"))


# Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    guessed_secret = ""
    for letter in secret:
        if letter in guess:
            guessed_secret += letter
        else:
            guessed_secret += "_"
    return guessed_secret


print(hangman("alphabet", "ab"))


# Task 10: Pig Latin, Another String Manipulation Exercise


def pig_latin(string):
    vowels = "aeiou"
    words = string.split()

    def transform_word(word):
       
        if "qu" in word:
            idx = word.index("qu")
            
            return word[idx+2:] + word[:idx+2] + "ay"
        
        
        if word[0] in vowels:
            return word + "ay"
        
        
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
    
    transformed_words = [transform_word(word) for word in words]

    return ' '.join(transformed_words)

print(pig_latin("apple"))
print(pig_latin("banana")) 
print(pig_latin("cherry")) 
print(pig_latin("quiet"))
print(pig_latin("square")) 
print(pig_latin("the quick brown fox"))
