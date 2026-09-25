from datetime import datetime

class StudentQueue:
    def __init__(self):
        self.queue = []  # List to store waiting students
        self.ticket_counter = 1001
        self.avg_service_time = 5  # 5 mins per student

    def joinQueue(self, student_id, is_emergency=False):
        # Test 2: Duplicate Prevention
        for student in self.queue:
            if student['id'] == student_id and student['status'] == 'Waiting':
                print(f"Error: Student {student_id} already in queue.")
                return

        ticket = f"#{self.ticket_counter}"
        self.ticket_counter += 1
        
        student_data = {
            'id': student_id,
            'ticket': ticket,
            'status': 'Waiting',
            'join_time': datetime.now(),
            'is_emergency': is_emergency
        }

        # Test 3: Emergency Priority
        if is_emergency:
            self.queue.insert(0, student_data)
            position = 1
        else:
            self.queue.append(student_data)
