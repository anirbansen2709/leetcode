"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def get_total_imp(self, employee_dict, id):
        employee_id = employee_dict[id]
        importance = employee_id.importance
        for sub in employee_id.subordinates:
            importance += self.get_total_imp(employee_dict, sub)
        return importance

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = dict()
        for employee in employees:
            employee_dict[employee.id] = employee
        return self.get_total_imp(employee_dict, id)
