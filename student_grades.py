class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):

        score = self.scores[index]

        if score >= 90:
            return f"A ({score} bodů)"
        elif score >= 80:
            return f"B ({score} bodů)"
        elif score >= 70:
            return f"C ({score} bodů)"
        elif score >= 60:
            return f"D ({score} bodů)"
        elif score >= 50:
            return f"E ({score} bodů)"
        else:
            return f"F ({score} bodů)"

    def find(self, target_score):
        students = []

        for i in range(len(self.scores)):
            if self.scores[i] == target_score:
                students.append(i)

        return students

    def get_sorted(self):
        scores = self.scores[:]
        n = len(scores)

        for i in range(n):
            for j in range(0, n-1-1):
                if scores[j] > scores[j+1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]
        return scores


if __name__ == '__main__':
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())          # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print()
    print("--- Udělení známky ---")
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print()
    print("--- Vyhledávání studentů s konkrétním počtem bodů ---")
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print()
    print("--- Seřazení výsledků ---")
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    print()
    print("--- Demonstrace třídy ---")
    print(f"Test psalo {results.count()} studentů.")

    # for i in range(results.count()):
    #
    #     points = results[i]
    #     grade = results.get_grade(points)
    #     print(f"Student {i}: {points} points – {grade}")
    # top_students = [i for i, p in enumerate(data) if p == 100]
    # print(f"Indexy studentů s plným počtem bodů: {top_students}")
    #
    # print(f"Seřazené výsledky (od nejhoršího): {results.get_sorted()}")
    # print("\n")
    #
    #
    # print("--- Demonstrace s náhodnými daty ---")
    #
    #
    # random_results = StudentsGrades(random_numbers(30, 0, 100))
    #
    # print(f"Počet studentů v náhodném testu: {random_results.count()}")
    # print(f"Seřazené náhodné výsledky: {random_results.get_sorted()}")