import datetime
import functools

@functools.total_ordering
class Time_interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'Slot: {self.start} - {self.end}'

    def __repr__(self):
        return f'Slot: {self.start} - {self.end}'

    def __lt__(self, other):
        return self.start < other.start

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class Working_hours(Time_interval):
    pass

class Slot(Time_interval):
    pass

class Employee():

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

class Employee_handler():

    SOD = datetime.time(0,0) # start of dat
    EOD = datetime.time(23,59) # end of day

    def __init__(self, employee):
        self.employee = employee

    def get_working_hours(self):
        return self.__read_working_hours()

    def get_free_slots(self):
        unavailable_slots = self.__unavailable_slots()
        free_slots = []
        for s in unavailable_slots:
            if len(free_slots) > 0:
                free_slots[-1].end = s.start
            if s.end != self.EOD:
                free_slots.append(Slot(s.end, self.EOD))
        free_slots = list(filter((lambda x: x.start != x.end), free_slots))
        return free_slots


    def set_slot(self, slot):
        if self.check_slot_availability(slot):
            __write_slot(slot)
        else:
            print(f'Slot {slot} is already busy with another slot. Try to set another time')

    def __unavailable_slots(self):

        working_hours = self.get_working_hours()

        s = list(self.__read_busy_slots())
        s.sort()
        s.insert(0
            , Slot(self.SOD, working_hours.start)
        )
        s.append(
            Slot(working_hours.end, self.EOD)
        )
        return s

    def check_slot_availability(self, slot):
        busy_slots = self.__read_busy_slots()
        working_hours = self.get_working_hours()

        return slot.start >= working_hours.start \
            and slot.end <= working_hours.end \
            and not any(map(lambda s: self.__slots_intersects(s, slot), busy_slots))

    def __slots_intersects(self, s1, s2):
        return s1.start < s2.end and s1.end > s2.start

    def __read_busy_slots(self):
        # TODO: database access
        pass

    def __read_working_hours(self):
        # TODO: database access
        pass

    def __write_new_slot(self, slot):
        # TODO: database access
        pass

def get_free_slots_of_empls(employees):
    res = []
    for e in employees:
        e_handler = Employee_handler(e)
        res.extend(e_handler.get_free_slots())
    return res