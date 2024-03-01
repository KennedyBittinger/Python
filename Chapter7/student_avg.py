#!/usr/bin/env python3

"""program to read a CSV file filled with student names and scores"""

__author__ = 'Kennedy Bittinger'
__date__ = '2/28/2024'

import csv


def read_student_scores(csv_file):
    """Read student scores from a CSV file.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        student_scores (dict): student names as keys and list of scores.
    """
    student_scores = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            student_name = row[0]
            # convert score strings to integers
            scores = [int(score) for score in row[1:]]
            student_scores[student_name] = scores
    return student_scores


def calculate_average(scores):
    """Calculate the average score from a list of scores.

    Args:
        scores (list): List of scores.

    Returns:
        average (float): The average score rounded to one decimal place.
    """
    return round(sum(scores) / len(scores), 1) if scores else 0


def write_average_scores(student_scores, output_file):
    """Write the average scores to a text file and print the scores.

    Args:
        student_scores (dict): student names as keys and list of scores.
        output_file (str): Path to text file to write the average scores.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        for student, scores in student_scores.items():
            average_score = calculate_average(scores)
            file.write(f"{student}: {average_score:.1f}\n")
            print(f"{student}: {average_score:.1f}")


# Main function
def main():
    """Main function."""
    csv_file = input("Input file? ")  # Prompt for the input CSV file
    print()
    output_file = input("Output file? ")  # Prompt for the output text file
    print()
    student_scores = read_student_scores(csv_file)
    write_average_scores(student_scores, output_file)
    print()


if __name__ == '__main__':
    main()
