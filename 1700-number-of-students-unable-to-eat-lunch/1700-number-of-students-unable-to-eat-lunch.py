class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(students!=[]):
            for i in sandwiches:
                if i not in students: 
                    return len(students)
                else:
                    students.pop(students.index(i))
        return 0