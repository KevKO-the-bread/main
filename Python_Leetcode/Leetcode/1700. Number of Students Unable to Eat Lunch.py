url= https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

class Solution:
    def countStudents(self, students, sandwiches):
        if not sandwiches:
            return 0

        while sandwiches and students:
            matched = False
            for i in range(len(students)):
                if sandwiches[0] == students[i]:
                    sandwiches.pop(0)
                    students.pop(i)
                    matched = True
                    break

            if not matched:
                return len(students)

        return 0
